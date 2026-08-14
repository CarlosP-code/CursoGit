import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, GridUpdateMode

st.set_page_config(page_title="Dashboard Corporativo", layout="wide")

# 1. CONFIGURACIÓN DE AUTENTICACIÓN
credentials = {
    "usernames": {
        "admin": {"name": "Administrador", "password": "12345"},
        "oper": {"name": "Operativo", "password": "12345"},
        "ing": {"name": "Ingeniero", "password": "12345"}
    }
}

authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="dashboard_cookie",
    key="signature_key",
    cookie_expiry_days=30
)

authenticator.login(location='main')

# 2. CONTROL DE FLUJO Y SESIÓN
auth_status = st.session_state.get("authentication_status")

if auth_status is False:
    st.error('Usuario o contraseña incorrectos')
elif auth_status is None:
    st.warning('Por favor, ingrese su usuario y contraseña')
elif auth_status:
    name_usuario = st.session_state.get("name", "Usuario")
    
    st.sidebar.markdown(f"**Usuario conectado:** {name_usuario}")
    authenticator.logout('Cerrar sesión', 'sidebar')
    
    st.title("📊 Dashboard Corporativo")
    st.caption(f"Bienvenido de nuevo, **{name_usuario}**")
    st.divider()

    # 3. CARGA DE DATOS ORIGINALES
    data = {
        "producto": ["Pizza Margarita", "Pizza Peperoni", "Calzone", "Refresco", "Patatas fritas"],
        "categoria": ["Comida", "Comida", "Comida", "Bebida", "Acompañantes"],
        "ventas_eur": [12.50, 15.32, 13.45, 2.50, 3.75],
        "stock": [30, 25, 15, 80, 50]
    }
    df_original = pd.DataFrame(data)

    # ==========================================
    # 4. FILTRO EN LA BARRA LATERAL (SIDEBAR)
    # ==========================================
    st.sidebar.divider()
    st.sidebar.header("🔍 Filtros de Datos")
    
    # Obtener las categorías únicas disponibles
    categorias_disponibles = df_original["categoria"].unique().tolist()
    
    # Multiselect para elegir una o varias categorías
    categorias_seleccionadas = st.sidebar.multiselect(
        label="Seleccionar Categorías:",
        options=categorias_disponibles,
        default=categorias_disponibles  # Por defecto selecciona todas
    )

    # Filtrar el DataFrame según la selección
    if categorias_seleccionadas:
        df = df_original[df_original["categoria"].isin(categorias_seleccionadas)]
    else:
        # Si el usuario desmarca todas las opciones, mostramos el DF vacío o un aviso
        df = df_original.iloc[0:0]

    if df.empty:
        st.warning("⚠️ No hay productos para mostrar con los filtros seleccionados.")
    else:
        # 5. TARJETAS DE KPIS (Se recalculan según el filtro)
        st.subheader("📈 Indicadores Clave de Rendimiento (KPIs)")
        col1, col2, col3, col4 = st.columns(4)
        
        total_ventas = df['ventas_eur'].sum()
        total_stock = df['stock'].sum()
        prod_top = df.loc[df['ventas_eur'].idxmax()]['producto'] if not df.empty else "N/A"
        ticket_promedio = df['ventas_eur'].mean() if not df.empty else 0.0

        col1.metric("Ventas Totales", f"{total_ventas:.2f} €")
        col2.metric("Unidades en Stock", f"{total_stock} u.")
        col3.metric("Producto Top", prod_top)
        col4.metric("Venta Promedio", f"{ticket_promedio:.2f} €")

        st.divider()

        # 6. TABLA INTERACTIVA (AgGrid)
        st.subheader("📦 Gestión de Inventario")

        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination(paginationAutoPageSize=True)
        gb.configure_selection('multiple', use_checkbox=True)
        grid_options = gb.build()

        grid_response = AgGrid(
            df,
            gridOptions=grid_options,
            data_return_mode=DataReturnMode.AS_INPUT,
            update_mode=GridUpdateMode.MODEL_CHANGED,
            fit_columns_on_grid_load=True,
            height=200
        )

        selected_rows = grid_response['selected_rows']

        if selected_rows is not None and len(selected_rows) > 0:
            df_seleccionados = pd.DataFrame(selected_rows)
            st.success(f"🔎 Has seleccionado **{len(df_seleccionados)}** producto(s).")
            
            col_sel1, col_sel2 = st.columns(2)
            with col_sel1:
                st.dataframe(df_seleccionados[['producto', 'categoria', 'ventas_eur', 'stock']], use_container_width=True)
            with col_sel2:
                st.info(f"**Total Ventas Seleccionadas:** {df_seleccionados['ventas_eur'].sum():.2f} €")
                st.info(f"**Total Stock Seleccionado:** {df_seleccionados['stock'].sum()} unidades")

        st.divider()

        # 7. GRÁFICOS RECALCULADOS
        st.subheader("📊 Análisis Gráfico")
        col_g1, col_g2 = st.columns(2)
        
        with col_g1:
            st.markdown("**Ventas Totales por Categoría (€)**")
            df_cat_ventas = df.groupby("categoria")["ventas_eur"].sum().reset_index()
            st.bar_chart(df_cat_ventas, x="categoria", y="ventas_eur")
            
        with col_g2:
            st.markdown("**Nivel de Stock por Producto**")
            st.bar_chart(df, x="producto", y="stock")