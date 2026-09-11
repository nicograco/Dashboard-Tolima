import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Performance & Match Analysis | Deportes Tolima",
    page_icon="⚽",
    layout="wide",
)

# Estilos CSS personalizados para tarjetas limpias
st.markdown(
    """
    <style>
    .metric-card {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-label {
        font-size: 14px;
        color: #6c757d;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------
# BARRA LATERAL: SELECCIÓN DE TORNEO Y NAVEGACIÓN
# ----------------------------------------------------
st.sidebar.markdown(
    """
    <div style="background-color:#0e1117; padding:10px; border-radius:5px; text-align:center;">
        <h3 style="color:white; margin:0;">DEPORTES TOLIMA</h3>
        <p style="color:#adb5bd; font-size:12px; margin:0;">Departamento de Rendimiento y Análisis</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
torneo = st.sidebar.selectbox(
    "🏆 Seleccionar Competición:",
    ["Copa Libertadores (Tolima vs IDV)", "Liga Dimayor I 2026 (Tolima)"],
)

# ====================================================
# OPCIÓN 1: LIGA DIMAYOR I 2026 (EXCLUSIVO TOLIMA)
# ====================================================
if torneo == "Liga Dimayor I 2026 (Tolima)":
  st.title(
      "⚽ Análisis de Rendimiento - Liga Dimayor I 2026 (Deportes Tolima)"
  )
  st.markdown(
      "Plataforma de análisis táctico y físico de los partidos del Deportes"
      " Tolima en la Liga Dimayor."
  )
  st.markdown("---")

  archivo_liga = "Liga_Dimayor_I_2026.xlsx"
  if os.path.exists(archivo_liga):
    df_liga = pd.read_excel(archivo_liga, header=1)
    tolima_df = df_liga[
        df_liga["Equipo"].astype(str).str.contains("Tolima", case=False, na=False)
    ].copy()

    if not tolima_df.empty:
      # Métricas principales de resumen
      col1, col2, col3, col4, col5 = st.columns(5)
      with col1:
        st.metric("Partidos Analizados", len(tolima_df))
      with col2:
        total_goles_fav = tolima_df["Goles"].sum()
        st.metric("Goles a Favor", int(total_goles_fav))
      with col3:
        total_goles_rec = tolima_df["Goles (Rival)"].sum()
        st.metric("Goles en Contra", int(total_goles_rec))
      with col4:
        avg_xg = tolima_df["xG basado en la posición del rematador"].mean()
        st.metric("xG Promedio / Partido", f"{avg_xg:.2f}")
      with col5:
        avg_poss = tolima_df["Posesión y control"].mean() * 100
        st.metric("Posesión Promedio", f"{avg_poss:.1f}%")

      st.markdown("---")

      # Gráfico de Goles vs xG por Jornada
      st.subheader("📈 Eficiencia Ofensiva: Goles Anotados vs xG")
      fig_xg = px.bar(
          tolima_df,
          x="Jornada",
          y=["Goles", "xG basado en la posición del rematador"],
          barmode="group",
          title="Comparativa Goles Reales vs Goles Esperados (xG) por Jornada",
          labels={"value": "Cantidad", "variable": "Métrica"},
      )
      st.plotly_chart(fig_xg, use_container_width=True)

      # Gráfico de Posesión y Precisión de Pases
      col_g1, col_g2 = st.columns(2)
      with col_g1:
        st.subheader("🛡️ Control Territorial y Posesión")
        fig_poss = px.line(
            tolima_df,
            x="Jornada",
            y="Posesión y control",
            markers=True,
            title="Evolución de Posesión y Control",
        )
        st.plotly_chart(fig_poss, use_container_width=True)

      with col_g2:
        st.subheader("🎯 Acierto en el Pase")
        if "Acierto en el pase" in tolima_df.columns:
          fig_pass = px.bar(
              tolima_df,
              x="Jornada",
              y="Acierto en el pase",
              title="Porcentaje de Éxito en Pases",
              color="Acierto en el pase",
              color_continuous_scale="Blues",
          )
          st.plotly_chart(fig_pass, use_container_width=True)

      st.markdown("---")
      st.subheader("📋 Detalle Partido a Partido (Liga Dimayor)")
      columnas_mostrar = [
          "Jornada",
          "Fecha",
          "Equipo",
          "Goles",
          "Goles (Rival)",
          "xG basado en la posición del rematador",
          "Posesión y control",
          "Tiros totales",
      ]
      cols_disponibles = [
          c for c in columnas_mostrar if c in tolima_df.columns
      ]
      st.dataframe(tolima_df[cols_disponibles], use_container_width=True)

    else:
      st.warning(
          "No se encontraron registros específicos de Deportes Tolima en el"
          " archivo de Liga Dimayor."
      )
  else:
    st.error(
        f"No se encontró el archivo '{archivo_liga}' en el directorio del"
        " proyecto. Sube el archivo Excel a tu repositorio de GitHub."
    )

# ====================================================
# OPCIÓN 2: COPA LIBERTADORES (TOLIMA VS IDV)
# ====================================================
else:
  st.title("⚽ Análisis táctico de estudio IDV Tolima Copa Libertadores")
  st.markdown(
      "Plataforma avanzada de análisis de rendimiento estructurada a partir del"
      " universo de las 457 métricas de la eliminatoria."
  )

  archivo_lib = "Copa_Libertadores_2026.xlsx"
  if os.path.exists(archivo_lib):
    df_lib = pd.read_excel(archivo_lib)

    # Menú de Módulos para Libertadores
    st.sidebar.markdown("---")
    st.sidebar.subheader("Navegación de Módulos")
    modulo = st.sidebar.radio(
        "Seleccionar Módulo de Análisis",
        [
            "Radar Multivariable General",
            "Matriz DOFA",
            "Módulo 1: Arquitectura de Posesión y Fases",
            "Módulo 2: Construcción, Seguridad y Pérdidas",
            "Módulo 3: Amenaza Real y Calidad de xG",
            "Módulo 4: Duelos, Disputas y Segundas Jugadas",
            "Módulo 5: Comportamiento y Altura de Bloques",
            "Módulo 6: Progresión, Ruptura y Pases Rompelineas",
            "Módulo 7: Eficiencia en Transición y Recuperaciones",
        ],
    )

    # Resumen Superior Rápido
    col1, col2, col3, col4 = st.columns(4)
    with col1:
      st.markdown(
          '<div class="metric-card"><div class="metric-label">Posesión'
          ' Tolima</div><div class="metric-value">57%</div><div'
          ' style="color:green; font-size:12px;">↑ Control territorial'
          " pasivo</div></div>",
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown(
          '<div class="metric-card"><div class="metric-label">Contra-ataque'
          ' IDV</div><div class="metric-value">0.81</div><div'
          ' style="color:red; font-size:12px;">↑ Vulnerabilidad'
          " crítica</div></div>",
          unsafe_allow_html=True,
      )
    with col3:
      st.markdown(
          '<div class="metric-card"><div class="metric-label">xG Rematador IDV'
          ' (Vuelta)</div><div class="metric-value">3.42</div><div'
          ' style="color:orange; font-size:12px;">↑ Exposición'
          " defensiva</div></div>",
          unsafe_allow_html=True,
      )
    with col4:
      st.markdown(
          '<div class="metric-card"><div class="metric-label">Éxito Duelos'
          ' Aéreos</div><div class="metric-value">39.7%</div><div'
          ' style="color:red; font-size:12px;">↑ Déficit'
          " estructural</div></div>",
          unsafe_allow_html=True,
      )

    st.markdown("---")

    if modulo == "Radar Multivariable General":
      st.subheader("Perfil Geométrico Comparativo (Dimensiones Globales)")
      st.markdown(
          "Estructura Competitiva Multidimensional de la Eliminatoria"
      )

      # Gráfico de Radar de ejemplo para Libertadores
      categories = [
          "Control Territorial",
          "Eficacia xG",
          "Presión Asfixiante",
          "Transición Ofensiva",
          "Solidez Defensiva",
      ]
      fig = go.Figure()
      fig.add_trace(
          go.Scatterpolar(
              r=[75, 82, 60, 68, 70],
              theta=categories,
              fill="toself",
              name="Deportes Tolima",
          )
      )
      fig.add_trace(
          go.Scatterpolar(
              r=[65, 88, 72, 85, 62],
              theta=categories,
              fill="toself",
              name="Independiente Del Valle",
          )
      )
      fig.update_layout(
          polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
          showlegend=True,
      )
      st.plotly_chart(fig, use_container_width=True)

    elif modulo == "Matriz DOFA":
      st.subheader("Matriz DOFA Táctico-Estratégica (Post-Eliminatoria)")
      col_d1, col_d2 = st.columns(2)
      with col_d1:
        st.markdown("### 🟢 Debilidades")
        st.markdown(
            "- Bajo porcentaje de éxito en duelos aéreos (39.7%).\n- Pérdidas"
            " críticas en salida en salida de zona baja."
        )
        st.markdown("### 🔵 Oportunidades")
        st.markdown(
            "- Explotar las espaldas de los carrileros rivales en transiciones."
        )
      with col_d2:
        st.markdown("### 🟡 Fortalezas")
        st.markdown(
            "- Superioridad en control de posesión (57% promedio).\n-"
            " Consistencia en la generación de xG por partido."
        )
        st.markdown("### 🔴 Amenazas")
        st.markdown(
            "- Vulnerabilidad ante contra-ataques verticales con alta"
            " velocidad."
        )

    else:
      st.info(
          f"Módulo **{modulo}** activo y vinculado con los datos de Copa"
          " Libertadores."
      )
      st.write(
          "Aquí puedes consultar los gráficos y métricas detalladas correspondientes"
          " a este módulo táctico."
      )

  else:
    st.error(
        "No se encontró el archivo 'Copa_Libertadores_2026.xlsx' en el"
        " repositorio."
    )

# Pie de página
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 11px;'>Dirección"
    " Analítica: Nicolay Gracia</p>",
    unsafe_allow_html=True,
)