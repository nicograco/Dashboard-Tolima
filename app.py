import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de página con diseño ancho
st.set_page_config(page_title="Análisis táctico IDV vs Tolima", layout="wide", page_icon="⚽")

# ==========================================
# ESTILOS CSS PERSONALIZADOS (ALTO CONTRASTE Y VISIBILIDAD)
# ==========================================
st.markdown("""
    <style>
    .metric-card {
        background-color: #1e293b;
        padding: 22px;
        border-radius: 12px;
        border: 1px solid #334155;
        color: #f8fafc !important;
        margin-bottom: 10px;
    }
    .metric-card h4 {
        color: #38bdf8 !important;
        margin-top: 0px;
        margin-bottom: 10px;
        font-size: 18px;
    }
    .metric-card ul, .metric-card li, .metric-card p, .metric-card b {
        color: #f8fafc !important;
        font-size: 14px;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# Paleta de colores: Azul Oscuro para Tolima y Rojo para IDV
COLOR_TOLIMA = "#1e40af"  # Azul Oscuro Profesional
COLOR_IDV = "#dc2626"     # Rojo Intenso

st.title("⚽ Análisis táctico de estudio IDV Tolima copa libertadores")
st.markdown("Plataforma avanzada de análisis de rendimiento estructurada a partir del universo de las **457 métricas** de la eliminatoria.")

@st.cache_data
def load_data():
    df = pd.read_excel('Copa_Libertadores_2026.xlsx', sheet_name='data')
    return df

try:
    df = load_data()
except Exception as e:
    st.warning("Verifique que el archivo 'Copa_Libertadores_2026.xlsx' se encuentre en el directorio de trabajo.")

# ==========================================
# PANEL LATERAL (SIDEBAR) CON NAVEGACIÓN RADIO
# ==========================================
st.sidebar.markdown(
    "<div style='text-align: center; padding: 12px; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: #38bdf8; border: 1px solid #38bdf8; border-radius: 10px; margin-bottom: 20px;'>"
    "<b>CONMEBOL LIBERTADORES</b><br><span style='font-size: 11px; color: #94a3b8;'>Performance & Match Analysis</span>"
    "</div>", 
    unsafe_allow_html=True
)

st.sidebar.header("🎛️ Navegación de Módulos")

bloque_sel = st.sidebar.radio("Seleccionar Módulo de Análisis", [
    "Radar Multivariable General",
    "Matriz DOFA",
    "Módulo 1: Arquitectura de Posesión y Fases", 
    "Módulo 2: Construcción, Seguridad y Pérdidas", 
    "Módulo 3: Amenaza Real y Calidad de xG", 
    "Módulo 4: Duelos, Disputas y Segundas Jugadas",
    "Módulo 5: Comportamiento y Altura de Bloques",
    "Módulo 6: Progresión, Ruptura y Pases Rompelíneas",
    "Módulo 7: Eficiencia en Transición y Recuperaciones"
])

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='text-align: center; color: #94a3b8; font-size: 12px;'>"
    "<b>Dirección Analítica:</b><br>Nicolay Gracia"
    "</div>", 
    unsafe_allow_html=True
)

# KPIs Principales de Impacto
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Posesión Tolima", "57%", "Control territorial pasivo")
with col2:
    st.metric("Contra-ataque IDV", "0.81", "Vulnerabilidad crítica")
with col3:
    st.metric("xG Rematador IDV (Vuelta)", "3.42", "Exposición defensiva")
with col4:
    st.metric("Éxito Duelos Aéreos", "39.7%", "Déficit estructural")

st.markdown("---")

if bloque_sel == "Radar Multivariable General":
    st.subheader("🕸️ Perfil Geométrico Comparativo (Dimensiones Globales)")
    
    categories = ['Control Territorial', 'Presión Asfixiante', 'Eficacia xG', 'Éxito Duelos Suelo', 'Estabilidad en Transición']
    
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[85, 90, 45, 75, 40],
        theta=categories,
        fill='toself',
        name='Deportes Tolima',
        line_color=COLOR_TOLIMA,
        opacity=0.85
    ))
    fig.add_trace(go.Scatterpolar(
        r=[70, 50, 95, 50, 90],
        theta=categories,
        fill='toself',
        name='Independiente del Valle',
        line_color=COLOR_IDV,
        opacity=0.85
    ))
    
    fig.update_layout(
        polar=dict(
            bgcolor='white',
            radialaxis=dict(visible=True, range=[0, 100], color='#1e293b', gridcolor='#cbd5e1'),
            angularaxis=dict(gridcolor='#cbd5e1', color='#1e293b')
        ),
        showlegend=True,
        height=600,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(color='#1e293b', size=14),
        title="<b>Estructura Competitiva Multidimensional de la Eliminatoria</b>"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Análisis Cruzado del Perfil Táctico:**
    * El diagrama revela la divergencia de modelos de la eliminatoria: Tolima sobresalió en las dimensiones de iniciativa y control territorial, mientras que el rival maximizó la eficacia en conversión de xG y estabilidad en transición.
    """)

elif bloque_sel == "Matriz DOFA":
    st.subheader("📋 Matriz DOFA (Estudio Post-Eliminatoria)")
    st.markdown("Análisis retrospectivo para comprender qué hicimos bien y qué debemos mejorar frente a un rival que nos sacó ventaja.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class='metric-card'>
        <h4>🟢 FORTALEZAS (Lo que hicimos bien)</h4>
        <ul>
            <li><b>Control Territorial:</b> Superioridad en posesión (57%) y capacidad para instalar un bloque de presión alto (68.45 metros de altura promedio).</li>
            <li><b>Volumen de Elaboración:</b> Solidez en la circulación inicial con 132.5 toques promedio en fase de construcción.</li>
        </ul>
        </div>
        
        <div class='metric-card'>
        <h4>🔴 DEBILIDADES (Lo que debemos mejorar)</h4>
        <ul>
            <li><b>Déficit en Duelos Aéreos:</b> Apenas 39.7% de éxito, impidiendo ganar segundas jugadas.</li>
            <li><b>Sobrecarga de Pases de Seguridad:</b> 92.5 pases hacia atrás por partido, facilitando el repliegue rival.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
        st.markdown("""
        <div class='metric-card'>
        <h4>🟡 OPORTUNIDADES (Aprendizajes estructurales)</h4>
        <ul>
            <li><b>Verticalización de la Posesión:</b> Reducir la horizontalidad para premiar la ruptura rápida entre líneas.</li>
            <li><b>Optimización de Transiciones:</b> Calibrar coberturas defensivas posteriores a la pérdida en campo rival.</li>
        </ul>
        </div>
        
        <div class='metric-card'>
        <h4>⚠️ AMENAZAS (Ventaja que sacó el rival)</h4>
        <ul>
            <li><b>Transiciones Letales:</b> Equipos con alta eficiencia en contraataque (índice 0.81 de IDV) que castigan los espacios a espaldas de la defensa.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif bloque_sel == "Módulo 1: Arquitectura de Posesión y Fases":
    st.subheader("Módulo 1: Relación entre Posesión, Presión y Contraataque Concedido")
    
    data_b1 = pd.DataFrame({
        'Métrica': ['Posesión y control', 'Presión asfixiante', 'Directo y Aéreo', 'Contra-ataque'],
        'Deportes Tolima': [0.57, 0.60, 0.22, 0.30],
        'Independiente del Valle': [0.52, 0.37, 0.43, 0.81]
    })
    fig = px.bar(data_b1, x='Métrica', y=['Deportes Tolima', 'Independiente del Valle'], 
                 barmode='group', title="Comparativa de Estilos y Comportamientos Sistémicos",
                 color_discrete_map={'Deportes Tolima': COLOR_TOLIMA, 'Independiente del Valle': COLOR_IDV})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **🔍 Análisis de Relación Profunda (Causa - Efecto entre Métricas):**
    * *Interacción de Variables:* El alto índice de **Presión Asfixiante (0.60)** ejercido por Tolima forzó al rival a un **Juego Directo (0.43)** superior. Sin embargo, al no consolidar el éxito en los duelos posteriores, esa presión se convirtió en un bumerán que disparó el **Índice de Contra-ataque del rival (0.81)**.
    * *Lección de Estudio:* No separar la presión alta de la estructura de coberturas defensivas.
    """)

elif bloque_sel == "Módulo 2: Construcción, Seguridad y Pérdidas":
    st.subheader("Módulo 2: Relación entre Elaboración, Pases Atrás y Pérdidas Ofensivas")
    
    data_b2 = pd.DataFrame({
        'Métrica': ['Control Elaboración', 'Balones Perdidos (Ofensiva)', 'Pases Atrás / Sup. Negativa'],
        'Deportes Tolima': [132.5, 93.0, 92.5],
        'Independiente del Valle': [114.0, 59.0, 54.5]
    })
    fig = px.bar(data_b2, x='Métrica', y=['Deportes Tolima', 'Independiente del Valle'], 
                 barmode='group', title="Volumen de Elaboración y Pérdidas Críticas",
                 color_discrete_map={'Deportes Tolima': COLOR_TOLIMA, 'Independiente del Valle': COLOR_IDV})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **🔍 Análisis de Relación Profunda (Causa - Efecto entre Métricas):**
    * *Interacción de Variables:* El elevado **Control de Balón en Elaboración (132.5)** correlacionó con la acumulación masiva de **Pases Hacia Atrás (92.5)**. Esto desaceleró el ritmo, permitiendo que el rival se reorganizara en bloque bajo y provocara un volumen crítico de **Balones Perdidos (93.0)**.
    * *Lección de Estudio:* Penalizar el pase de retorno horizontal excesivo en campo rival.
    """)

elif bloque_sel == "Módulo 3: Amenaza Real y Calidad de xG":
    st.subheader("Módulo 3: Relación entre Volumen de Remates y Calidad de xG")
    
    data_b3 = pd.DataFrame({
        'Métrica': ['xG Rematador', 'xG post-Tiros', 'Tiros a Portería'],
        'Deportes Tolima': [0.83, 0.68, 3.5],
        'Independiente del Valle': [2.35, 2.36, 4.5]
    })
    fig = px.bar(data_b3, x='Métrica', y=['Deportes Tolima', 'Independiente del Valle'], 
                 barmode='group', title="Calidad de Ocasiones y Rentabilidad de Remates",
                 color_discrete_map={'Deportes Tolima': COLOR_TOLIMA, 'Independiente del Valle': COLOR_IDV})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **🔍 Análisis de Relación Profunda (Causa - Efecto entre Métricas):**
    * *Interacción de Variables:* A pesar de registrar una cantidad similar de remates totales (13.5 vs 14.5), la brecha en el **xG Rematador (0.83 vs 2.35)** evidencia que generamos disparos de baja probabilidad estadística.
    * *Lección de Estudio:* Priorizar la ocupación racional del área y los desmarques de ruptura por encima del volumen de remates lejanos.
    """)

elif bloque_sel == "Módulo 4: Duelos, Disputas y Segundas Jugadas":
    st.subheader("Módulo 4: Relación entre Duelos Aéreos y Control de Segundas Jugadas")
    
    data_b4 = pd.DataFrame({
        'Métrica': ['Duelos en Suelo (%)', 'Duelos Aéreos (%)', 'Intercepciones Defensivas'],
        'Deportes Tolima': [58.0, 39.7, 70.0],
        'Independiente del Valle': [42.0, 60.3, 84.5]
    })
    fig = px.bar(data_b4, x='Métrica', y=['Deportes Tolima', 'Independiente del Valle'], 
                 barmode='group', title="Efectividad en Disputas y Control Aéreo",
                 color_discrete_map={'Deportes Tolima': COLOR_TOLIMA, 'Independiente del Valle': COLOR_IDV})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **🔍 Análisis de Relación Profunda (Causa - Efecto entre Métricas):**
    * *Interacción de Variables:* La baja efectividad en **Duelos Aéreos (39.7% vs 60.3% del rival)** destruyó la estabilidad defensiva. Al perder el control de las segundas jugadas tras envíos largos, IDV superó la presión con facilidad.
    * *Lección de Estudio:* Mejorar la lectura de trayectorias en balones largos y la postura corporal en disputa física.
    """)

elif bloque_sel == "Módulo 5: Comportamiento y Altura de Bloques":
    st.subheader("Módulo 5: Relación entre Altura de Bloque y Vulnerabilidad Defensiva")
    
    data_b5 = pd.DataFrame({
        'Métrica': ['Altura Promedio Bloque (m)', 'Pases Altos Forzados (%)', 'Contra-Presión'],
        'Deportes Tolima': [68.45, 34.0, 28.64],
        'Independiente del Valle': [53.90, 17.0, 29.45]
    })
    fig = px.bar(data_b5, x='Métrica', y=['Deportes Tolima', 'Independiente del Valle'], 
                 barmode='group', title="Comportamiento Dinámico de la Presión",
                 color_discrete_map={'Deportes Tolima': COLOR_TOLIMA, 'Independiente del Valle': COLOR_IDV})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **🔍 Análisis de Relación Profunda (Causa - Efecto entre Métricas):**
    * *Interacción de Variables:* Fijar la **Altura del Bloque en 68.45 metros** forzó errores rivales (34% de pases altos), pero la falta de coberturas expuso el espacio a espaldas, facilitando el pico de **3.42 en xG en contra**.
    * *Lección de Estudio:* Sincronizar el momento de presión colectiva con criterios claros de repliegue estratégico.
    """)

elif bloque_sel == "Módulo 6: Progresión, Ruptura y Pases Rompelíneas":
    st.subheader("Módulo 6: Progresión y Pases Rompelíneas (Análisis de Ruptura)")
    
    data_b6 = pd.DataFrame({
        'Métrica': ['Pases Progresivos (Media)', 'Recuperaciones Progresivas', 'Acc. Balón Parado Progr.'],
        'Deportes Tolima': [1.09, 0.53, 0.03],
        'Independiente del Valle': [1.45, 0.47, 0.09]
    })
    fig = px.bar(data_b6, x='Métrica', y=['Deportes Tolima', 'Independiente del Valle'], 
                 barmode='group', title="Capacidad de Progresión y Ruptura de Líneas",
                 color_discrete_map={'Deportes Tolima': COLOR_TOLIMA, 'Independiente del Valle': COLOR_IDV})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **🔍 Análisis de Relación Profunda (Causa - Efecto entre Métricas):**
    * *Interacción de Variables:* La menor tasa de **Pases Progresivos (1.09 vs 1.45 del rival)** explica por qué la superioridad del 57% en posesión se tornó estéril. Al faltar la capacidad de conectar pases rompelíneas hacia el espacio interior, el equipo dependió de circulaciones laterales que facilitaron el repliegue defensivo de IDV.
    * *Lección de Estudio:* Diseñar tareas metodológicas enfocadas en el juego interior entre líneas de mediocentros y centrales para elevar el índice de progresión limpia.
    """)

else:
    st.subheader("Módulo 7: Eficiencia en Transición y Recuperaciones")
    
    data_b7 = pd.DataFrame({
        'Métrica': ['Índice Contra-ataque', 'Balones Perdidos Ofensiva', 'xG Post-Tiros (Vuelta)'],
        'Deportes Tolima': [0.30, 197.0, 4.05],
        'Independiente del Valle': [0.81, 152.5, 4.05]
    })
    fig = px.bar(data_b7, x='Métrica', y=['Deportes Tolima', 'Independiente del Valle'], 
                 barmode='group', title="Vulnerabilidad y Eficiencia en Transiciones",
                 color_discrete_map={'Deportes Tolima': COLOR_TOLIMA, 'Independiente del Valle': COLOR_IDV})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **🔍 Análisis de Relación Profunda (Causa - Efecto entre Métricas):**
    * *Interacción de Variables:* El alto volumen de **Balones Perdidos en Fase Ofensiva (197.0 acumulados)** conectado con la letalidad del rival en transición (**Índice de Contra-ataque de 0.81**) detonó las situaciones de máximo peligro, culminando en picos de **4.05 en xG post-tiros** en el partido de vuelta.
    * *Lección de Estudio:* Establecer protocolos estrictos de contrapresión en los primeros 3 segundos posteriores a la pérdida en campo rival para frenar la progresión del contraataque adversario.
    """)

st.markdown("---")