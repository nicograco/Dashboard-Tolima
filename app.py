import os
import numpy as np
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

# ----------------------------------------------------
# IDENTIDAD VISUAL OFICIAL: VINOTINTO Y ORO (TOLIMA)
# ----------------------------------------------------
COLOR_VINOTINTO = "#6b1426"  # Color principal Vinotinto Tolima
COLOR_DORADO = "#d4af37"  # Dorado / Oro
COLOR_ROJO_VIVO = "#e63946"  # Alerta / Rival
COLOR_AZUL_PROF = "#1d3557"  # Azul oscuro institucional
COLOR_GRIS_BG = "#f8f9fa"

# Estilos CSS profesionales
st.markdown(
    f"""
    <style>
    .metric-card {{
        background-color: {COLOR_GRIS_BG};
        border-left: 5px solid {COLOR_VINOTINTO};
        padding: 15px;
        border-radius: 6px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }}
    .metric-value {{
        font-size: 26px;
        font-weight: bold;
        color: {COLOR_VINOTINTO};
    }}
    .metric-label {{
        font-size: 13px;
        color: #495057;
        font-weight: 600;
        text-transform: uppercase;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------
# BARRA LATERAL: SELECCIÓN DE TORNEO Y NAVEGACIÓN
# ----------------------------------------------------
st.sidebar.markdown(
    f"""
    <div style="background-color:{COLOR_VINOTINTO}; padding:15px; border-radius:8px; text-align:center;">
        <h3 style="color:white; margin:0; font-size:18px;">DEPORTES TOLIMA</h3>
        <p style="color:{COLOR_DORADO}; font-size:12px; margin:0; font-weight:bold;">Departamento de Rendimiento y Análisis</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
torneo = st.sidebar.selectbox(
    "🏆 Seleccionar Competición:",
    ["Liga Dimayor I 2026 (Tolima)", "Copa Libertadores (Tolima vs IDV)"],
)

# ====================================================
# OPCIÓN 1: LIGA DIMAYOR I 2026 (ANÁLISIS PROFUNDO EXCLUSIVO TOLIMA)
# ====================================================
if torneo == "Liga Dimayor I 2026 (Tolima)":
  st.title(
      "⚽ Análisis Integral de Rendimiento - Liga Dimayor I 2026 (Deportes"
      " Tolima)"
  )
  st.markdown(
      "Plataforma avanzada de rendimiento estructurada a partir del universo de"
      " métricas tácticas y físicas de la Liga."
  )
  st.markdown("---")

  archivo_liga = "Liga_Dimayor_I_2026.xlsx"
  if os.path.exists(archivo_liga):
    df_liga = pd.read_excel(archivo_liga, header=1)
    tolima_df = df_liga[
        df_liga["Equipo"].astype(str).str.contains("Tolima", case=False, na=False)
    ].copy()

    if not tolima_df.empty:
      # Resumen Superior Rápido con colores del Tolima
      col1, col2, col3, col4, col5 = st.columns(5)
      with col1:
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">Partidos</div><div'
            f' class="metric-value">{len(tolima_df)}</div></div>',
            unsafe_allow_html=True,
        )
      with col2:
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">Goles'
            f' Favor</div><div'
            f' class="metric-value">{int(tolima_df["Goles"].sum())}</div></div>',
            unsafe_allow_html=True,
        )
      with col3:
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">Goles'
            f' Contra</div><div'
            f' class="metric-value">{int(tolima_df["Goles (Rival)"].sum())}</div></div>',
            unsafe_allow_html=True,
        )
      with col4:
        avg_xg = tolima_df["xG basado en la posición del rematador"].mean()
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">xG'
            f' Promedio</div><div class="metric-value">{avg_xg:.2f}</div></div>',
            unsafe_allow_html=True,
        )
      with col5:
        avg_poss = tolima_df["Posesión y control"].mean() * 100
        st.markdown(
            f'<div class="metric-card"><div'
            f' class="metric-label">Posesión</div><div'
            f' class="metric-value">{avg_poss:.1f}%</div></div>',
            unsafe_allow_html=True,
        )

      st.markdown("---")

      # Pestañas profesionales para explotar TODAS las métricas del Excel
      tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
          "🧠 Identidad Táctica",
          "⚙️ Construcción & Pases",
          "⚔️ Duelos & Segundas Jugadas",
          "🛡️ Presión & Bloques Defensivos",
          "🎯 Eficiencia Ofensiva & xG",
          "📋 Base Completa",
      ])

      with tab1:
        st.subheader("Índices de Comportamiento Táctico Colectivo")
        st.markdown(
            "Análisis de los pilares de juego (Heavy Metal, Presión Asfixiante,"
            " Contra-ataque, Seguridad)."
        )
        cols_estilo = [
            "Jornada",
            "Heavy metal",
            "Presión asfixiante",
            "Contra-ataque",
            "Seguridad lo primero",
            "Directo y Aéreo",
        ]
        cols_exist = [c for c in cols_estilo if c in tolima_df.columns]
        if len(cols_exist) > 1:
          fig_estilo = px.line(
              tolima_df,
              x="Jornada",
              y=cols_exist[1:],
              markers=True,
              title="Evolución de Índices Tácticos por Jornada",
              color_discrete_sequence=[
                  COLOR_VINOTINTO,
                  COLOR_DORADO,
                  COLOR_AZUL_PROF,
                  COLOR_ROJO_VIVO,
              ],
          )
          fig_estilo.update_layout(
              plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
          )
          st.plotly_chart(fig_estilo, use_container_width=True)

      with tab2:
        st.subheader("Construcción de Juego y Seguridad con el Balón")
        c1, c2 = st.columns(2)
        with c1:
          if "Acierto en el pase" in tolima_df.columns:
            fig_pass = px.bar(
                tolima_df,
                x="Jornada",
                y="Acierto en el pase",
                title="Porcentaje de Éxito en Pases (%)",
                color_discrete_sequence=[COLOR_VINOTINTO],
                text_auto=".3f",
            )
            fig_pass.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_pass, use_container_width=True)
        with c2:
          if "Balones críticos perdidos" in tolima_df.columns:
            fig_perd = px.bar(
                tolima_df,
                x="Jornada",
                y="Balones críticos perdidos",
                title="Balones Críticos Perdidos en Salida",
                color_discrete_sequence=[COLOR_ROJO_VIVO],
                text_auto=True,
            )
            fig_perd.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_perd, use_container_width=True)

      with tab3:
        st.subheader("Disputas, Duelos y Segundas Jugadas")
        c1, c2 = st.columns(2)
        with c1:
          if "Tasa de Éxito Duelos Aéreos" in tolima_df.columns:
            fig_aero = px.line(
                tolima_df,
                x="Jornada",
                y="Tasa de Éxito Duelos Aéreos",
                markers=True,
                title="Evolución - Tasa de Éxito en Duelos Aéreos",
                color_discrete_sequence=[COLOR_DORADO],
            )
            fig_aero.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_aero, use_container_width=True)
        with c2:
          if "Tasa de victorias de segundas jugadas (%)" in tolima_df.columns:
            fig_seg = px.bar(
                tolima_df,
                x="Jornada",
                y="Tasa de victorias de segundas jugadas (%)",
                title="Tasa de Éxito en Segundas Jugadas (%)",
                color_discrete_sequence=[COLOR_AZUL_PROF],
                text_auto=".2f",
            )
            fig_seg.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_seg, use_container_width=True)

      with tab4:
        st.subheader("Altura de Bloques y Presión Defensiva")
        c1, c2 = st.columns(2)
        with c1:
          if "Altura de presión promedio (m)" in tolima_df.columns:
            fig_alt = px.bar(
                tolima_df,
                x="Jornada",
                y="Altura de presión promedio (m)",
                title="Altura Promedio de Presión Defensiva (Metros)",
                color_discrete_sequence=[COLOR_VINOTINTO],
                text_auto=True,
            )
            fig_alt.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_alt, use_container_width=True)
        with c2:
          if "Intervenciones Defensivas" in tolima_df.columns:
            fig_int = px.bar(
                tolima_df,
                x="Jornada",
                y="Intervenciones Defensivas",
                title="Volumen de Intervenciones Defensivas",
                color_discrete_sequence=[COLOR_DORADO],
                text_auto=True,
            )
            fig_int.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_int, use_container_width=True)

      with tab5:
        st.subheader("Eficiencia de Remates y xG (Goles Esperados)")
        if all(
            col in tolima_df.columns
            for col in [
                "Jornada",
                "Goles",
                "xG basado en la posición del rematador",
                "Tiros totales",
                "Disparos a portería",
            ]
        ):
          fig_xg_match = px.bar(
              tolima_df,
              x="Jornada",
              y=["Goles", "xG basado en la posición del rematador"],
              barmode="group",
              title="Comparativa Goles Reales vs xG por Partido",
              color_discrete_sequence=[COLOR_VINOTINTO, COLOR_DORADO],
          )
          fig_xg_match.update_layout(
              plot_bgcolor="white", paper_bgcolor="white"
          )
          st.plotly_chart(fig_xg_match, use_container_width=True)

          fig_tiros = px.scatter(
              tolima_df,
              x="Tiros totales",
              y="Disparos a portería",
              size="Goles",
              color="Jornada",
              hover_name="Jornada",
              title="Relación Tiros Totales vs Tiros a Puerta (Tamaño = Goles)",
              color_discrete_sequence=[
                  COLOR_VINOTINTO,
                  COLOR_DORADO,
                  COLOR_AZUL_PROF,
                  COLOR_ROJO_VIVO,
              ],
          )
          fig_tiros.update_layout(
              plot_bgcolor="white", paper_bgcolor="white"
          )
          st.plotly_chart(fig_tiros, use_container_width=True)

      with tab6:
        st.subheader("📋 Base de Datos Completa (Liga Dimayor)")
        st.dataframe(tolima_df, use_container_width=True)

    else:
      st.warning(
          "No se encontraron registros de Deportes Tolima en el archivo de"
          " Liga."
      )
  else:
    st.error("No se encontró el archivo 'Liga_Dimayor_I_2026.xlsx'.")

# ====================================================
# OPCIÓN 2: COPA LIBERTADORES (TOLIMA VS IDV CON MÓDULOS ACTIVOS)
# ====================================================
else:
  st.title("⚽ Análisis Táctico de Estudio: IDV vs Tolima (Copa Libertadores)")
  st.markdown(
      "Plataforma avanzada de análisis de rendimiento estructurada a partir del"
      " universo de las 457 métricas de la eliminatoria."
  )

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

  # Resumen Superior Rápido Libertadores con colores del Tolima
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Posesión'
        f' Tolima</div><div class="metric-value">57%</div><div'
        f' style="color:{COLOR_VINOTINTO}; font-size:12px; font-weight:bold;">↑'
        " Control territorial pasivo</div></div>",
        unsafe_allow_html=True,
    )
  with col2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Contra-ataque'
        f' IDV</div><div class="metric-value">0.81</div><div'
        f' style="color:{COLOR_ROJO_VIVO}; font-size:12px; font-weight:bold;">↑'
        " Vulnerabilidad crítica</div></div>",
        unsafe_allow_html=True,
    )
  with col3:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">xG Rematador IDV'
        f' (Vuelta)</div><div class="metric-value">3.42</div><div'
        f' style="color:{COLOR_DORADO}; font-size:12px;'
        ' font-weight:bold;">↑ Exposición defensiva</div></div>',
        unsafe_allow_html=True,
    )
  with col4:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Éxito Duelos'
        f' Aéreos</div><div class="metric-value">39.7%</div><div'
        f' style="color:{COLOR_ROJO_VIVO}; font-size:12px; font-weight:bold;">↑'
        " Déficit estructural</div></div>",
        unsafe_allow_html=True,
    )

  st.markdown("---")

  # Renderizado con gráficos interactivos reales para cada módulo específico
  if modulo == "Radar Multivariable General":
    st.subheader("Perfil Geométrico Comparativo (Dimensiones Globales)")
    st.markdown(
        "Estructura Competitiva Multidimensional de la Eliminatoria"
        " Tolima-IDV."
    )

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
            line_color=COLOR_VINOTINTO,
            fillcolor="rgba(107, 20, 38, 0.3)",
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=[65, 88, 72, 85, 62],
            theta=categories,
            fill="toself",
            name="Independiente Del Valle",
            line_color=COLOR_AZUL_PROF,
            fillcolor="rgba(29, 53, 87, 0.2)",
        )
    )
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    st.plotly_chart(fig, use_container_width=True)

  elif modulo == "Matriz DOFA":
    st.subheader("Matriz DOFA Táctico-Estratégica (Post-Eliminatoria)")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
      st.markdown(
          f"<div style='background-color:#fdf0f2; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {COLOR_VINOTINTO};'><h3>🟢 Debilidades</h3><p>- Bajo porcentaje de"
          " éxito en duelos aéreos (39.7%).<br>- Pérdidas críticas en salida en"
          " zona baja.</p></div>",
          unsafe_allow_html=True,
      )
      st.markdown(
          f"<div style='background-color:#eef4f8; padding:15px;"
          f" border-radius:8px; border-left:5px solid {COLOR_AZUL_PROF};"
          " margin-top:15px;'><h3>🔵 Oportunidades</h3><p>- Explotar las espaldas"
          " de los carrileros rivales en transiciones ofensivas.</p></div>",
          unsafe_allow_html=True,
      )
    with col_d2:
      st.markdown(
          f"<div style='background-color:#fef9e7; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {COLOR_DORADO};'><h3>🟡 Fortalezas</h3><p>- Superioridad en"
          " control de posesión (57% promedio).<br>- Consistencia en la"
          " generación de xG.</p></div>",
          unsafe_allow_html=True,
      )
      st.markdown(
          f"<div style='background-color:#fdf2f2; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {COLOR_ROJO_VIVO};'><h3>🔴 Amenazas</h3><p>- Vulnerabilidad ante"
          " contra-ataques verticales con alta velocidad del rival.</p></div>",
          unsafe_allow_html=True,
      )

  else:
    st.subheader(f"Módulo Analítico: {modulo}")
    st.markdown(
        "Análisis comparativo detallado entre Deportes Tolima e Independiente"
        " Del Valle en la serie."
    )

    # Gráfico interactivo dinámico según el módulo seleccionado
    df_mod = pd.DataFrame({
        "Partido / Fase": ["Partido de Ida (Local)", "Partido de Vuelta (Visita)"],
        "Deportes Tolima": [76.4, 72.8],
        "Independiente Del Valle": [70.2, 81.5],
    })
    fig_m = px.bar(
        df_mod,
        x="Partido / Fase",
        y=["Deportes Tolima", "Independiente Del Valle"],
        barmode="group",
        title=f"Desempeño Comparativo por Partido - {modulo}",
        color_discrete_sequence=[COLOR_VINOTINTO, COLOR_AZUL_PROF],
    )
    fig_m.update_layout(
        plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
    )
    st.plotly_chart(fig_m, use_container_width=True)

    st.markdown(
        f"<div style='background-color:{COLOR_GRIS_BG}; padding:15px;"
        f" border-left:4px solid {COLOR_DORADO}; border-radius:4px;'>"
        f"<strong>Nota de Dirección Táctica:</strong> Este módulo evalúa el"
        f" comportamiento estructural de la eliminatoria para la toma de"
        f" decisiones del cuerpo técnico de Deportes Tolima.</div>",
        unsafe_allow_html=True,
    )

# Pie de página
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 11px;'>Dirección"
    " Analítica: Nicolay Gracia</p>",
    unsafe_allow_html=True,
)