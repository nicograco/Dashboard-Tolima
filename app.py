import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Elite Match & Tactical Analytics Lab", page_icon="⚡", layout="wide"
)

# ----------------------------------------------------
# PALETA DE COLORES MODERNA Y LLAMATIVA (HIGH-TECH SPORTS)
# ----------------------------------------------------
COLOR_PRIMARY = "#3a86ff"  # Azul Eléctrico
COLOR_SECONDARY = "#ff006e"  # Magenta / Rosa Vibrante
COLOR_ACCENT = "#8338ec"  # Púrpura Tecnológico
COLOR_SUCCESS = "#38b000"  # Verde Neón
COLOR_WARNING = "#fb8500"  # Naranja Ámbar
COLOR_DARK = "#111827"  # Fondo oscuro elegante
COLOR_LIGHT_BG = "#f8f9fa"

# Estilos CSS con tarjetas y efectos modernos
st.markdown(
    f"""
    <style>
    .metric-card {{
        background-color: {COLOR_LIGHT_BG};
        border-left: 5px solid {COLOR_PRIMARY};
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.06);
    }}
    .metric-value {{
        font-size: 28px;
        font-weight: 800;
        color: {COLOR_PRIMARY};
    }}
    .metric-label {{
        font-size: 13px;
        color: #4b5563;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------
# BARRA LATERAL: NAVEGACIÓN Y BRANDING ANALÍTICO
# ----------------------------------------------------
st.sidebar.markdown(
    f"""
    <div style="background: linear-gradient(135deg, {COLOR_PRIMARY}, {COLOR_ACCENT}); padding:18px; border-radius:10px; text-align:center;">
        <h3 style="color:white; margin:0; font-size:18px; font-weight:800;">ELITE PERFORMANCE LAB</h3>
        <p style="color:#e0f2fe; font-size:11px; margin:4px 0 0 0; font-weight:600;">Advanced Match & Tactical Analysis</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
torneo = st.sidebar.selectbox(
    "🏆 Seleccionar Módulo de Competición:",
    ["Liga Dimayor I 2026 (Análisis de Equipo)", "Copa Libertadores (Serie Táctica)"],
)

# ====================================================
# OPCIÓN 1: LIGA DIMAYOR I 2026 (ANÁLISIS PROFUNDO)
# ====================================================
if torneo == "Liga Dimayor I 2026 (Análisis de Equipo)":
  st.title("⚡ Dashboard Analítico de Rendimiento - Liga Dimayor I 2026")
  st.markdown(
      "Plataforma avanzada de procesamiento de datos tácticos, físicos y"
      " condicionales por partido."
  )
  st.markdown("---")

  archivo_liga = "Liga_Dimayor_I_2026.xlsx"
  if os.path.exists(archivo_liga):
    df_liga = pd.read_excel(archivo_liga, header=1)
    tolima_df = df_liga[
        df_liga["Equipo"].astype(str).str.contains("Tolima", case=False, na=False)
    ].copy()

    if not tolima_df.empty:
      # Resumen Superior Rápido con diseño moderno
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

      # Pestañas profesionales con paleta vibrante
      tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
          "🧠 Identidad Táctica",
          "⚙️ Construcción & Pases",
          "⚔️ Duelos & Segundas Jugadas",
          "🛡️ Presión & Bloques",
          "🎯 Eficiencia & xG",
          "📋 Base Completa",
      ])

      with tab1:
        st.subheader("Índices de Comportamiento Táctico Colectivo")
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
              title="Evolución de Pilares Tácticos por Jornada",
              color_discrete_sequence=[
                  COLOR_PRIMARY,
                  COLOR_SECONDARY,
                  COLOR_ACCENT,
                  COLOR_SUCCESS,
                  COLOR_WARNING,
              ],
          )
          fig_estilo.update_layout(
              plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
          )
          st.plotly_chart(fig_estilo, use_container_width=True)

      with tab2:
        st.subheader("Construcción de Juego y Seguridad con Balón")
        c1, c2 = st.columns(2)
        with c1:
          if "Acierto en el pase" in tolima_df.columns:
            fig_pass = px.bar(
                tolima_df,
                x="Jornada",
                y="Acierto en el pase",
                title="Porcentaje de Éxito en Pases (%)",
                color_discrete_sequence=[COLOR_PRIMARY],
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
                color_discrete_sequence=[COLOR_SECONDARY],
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
                title="Evolución - Tasa Éxito Duelos Aéreos",
                color_discrete_sequence=[COLOR_ACCENT],
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
                color_discrete_sequence=[COLOR_SUCCESS],
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
                color_discrete_sequence=[COLOR_WARNING],
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
                color_discrete_sequence=[COLOR_PRIMARY],
                text_auto=True,
            )
            fig_int.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_int, use_container_width=True)

      with tab5:
        st.subheader("Eficiencia Ofensiva y xG (Goles Esperados)")
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
              color_discrete_sequence=[COLOR_PRIMARY, COLOR_SECONDARY],
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
              title=(
                  "Relación Tiros Totales vs Tiros a Puerta (Tamaño = Goles"
                  " Anotados)"
              ),
              color_discrete_sequence=[
                  COLOR_PRIMARY,
                  COLOR_SECONDARY,
                  COLOR_ACCENT,
                  COLOR_SUCCESS,
              ],
          )
          fig_tiros.update_layout(
              plot_bgcolor="white", paper_bgcolor="white"
          )
          st.plotly_chart(fig_tiros, use_container_width=True)

      with tab6:
        st.subheader("📋 Base Completa de Datos (Liga Dimayor)")
        st.dataframe(tolima_df, use_container_width=True)

    else:
      st.warning("No se encontraron registros de partidos en la Liga.")
  else:
    st.error("No se encontró el archivo 'Liga_Dimayor_I_2026.xlsx'.")

# ====================================================
# OPCIÓN 2: COPA LIBERTADORES (SERIE TÁCTICA)
# ====================================================
else:
  st.title("⚡ Análisis Táctico de Estudio: IDV vs Rival (Copa Libertadores)")
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

  # Resumen Superior Rápido con colores vibrantes
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Control'
        f' Posesión</div><div class="metric-value">57%</div><div'
        f' style="color:{COLOR_PRIMARY}; font-size:12px; font-weight:bold;">↑'
        " Control territorial pasivo</div></div>",
        unsafe_allow_html=True,
    )
  with col2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Contra-ataque'
        f' Rival</div><div class="metric-value">0.81</div><div'
        f' style="color:{COLOR_SECONDARY}; font-size:12px;'
        ' font-weight:bold;">↑ Vulnerabilidad crítica</div></div>',
        unsafe_allow_html=True,
    )
  with col3:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">xG Rematador'
        f' (Vuelta)</div><div class="metric-value">3.42</div><div'
        f' style="color:{COLOR_WARNING}; font-size:12px; font-weight:bold;">↑'
        " Exposición defensiva</div></div>",
        unsafe_allow_html=True,
    )
  with col4:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Éxito Duelos'
        f' Aéreos</div><div class="metric-value">39.7%</div><div'
        f' style="color:{COLOR_SECONDARY}; font-size:12px;'
        ' font-weight:bold;">↑ Déficit estructural</div></div>',
        unsafe_allow_html=True,
    )

  st.markdown("---")

  # Renderizado con gráficos interactivos dinámicos para cada módulo
  if modulo == "Radar Multivariable General":
    st.subheader("Perfil Geométrico Comparativo (Dimensiones Globales)")
    st.markdown(
        "Estructura Competitiva Multidimensional de la Serie de Eliminatoria."
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
            name="Equipo Principal",
            line_color=COLOR_PRIMARY,
            fillcolor="rgba(58, 134, 255, 0.25)",
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=[65, 88, 72, 85, 62],
            theta=categories,
            fill="toself",
            name="Oponente (IDV)",
            line_color=COLOR_SECONDARY,
            fillcolor="rgba(255, 0, 110, 0.15)",
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
          f"<div style='background-color:#eff6ff; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {COLOR_PRIMARY};'><h3>🟢 Debilidades</h3><p>- Bajo porcentaje de"
          " éxito en duelos aéreos (39.7%).<br>- Pérdidas críticas en salida en"
          " zona baja.</p></div>",
          unsafe_allow_html=True,
      )
      st.markdown(
          f"<div style='background-color:#f5f3ff; padding:15px;"
          f" border-radius:8px; border-left:5px solid {COLOR_ACCENT};"
          " margin-top:15px;'><h3>🔵 Oportunidades</h3><p>- Explotar las espaldas"
          " de los carrileros rivales en transiciones ofensivas.</p></div>",
          unsafe_allow_html=True,
      )
    with col_d2:
      st.markdown(
          f"<div style='background-color:#fef3c7; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {COLOR_WARNING};'><h3>🟡 Fortalezas</h3><p>- Superioridad en"
          " control de posesión (57% promedio).<br>- Consistencia en la"
          " generación de xG.</p></div>",
          unsafe_allow_html=True,
      )
      st.markdown(
          f"<div style='background-color:#fdf2f8; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {COLOR_SECONDARY};'><h3>🔴 Amenazas</h3><p>- Vulnerabilidad ante"
          " contra-ataques verticales con alta velocidad del rival.</p></div>",
          unsafe_allow_html=True,
      )

  else:
    st.subheader(f"Módulo Analítico: {modulo}")
    st.markdown(
        "Análisis comparativo detallado de rendimiento estructural de la"
        " eliminatoria."
    )

    # Gráfico interactivo con colores vibrantes
    df_mod = pd.DataFrame({
        "Partido / Fase": ["Partido de Ida (Local)", "Partido de Vuelta (Visita)"],
        "Equipo Principal": [76.4, 72.8],
        "Oponente (IDV)": [70.2, 81.5],
    })
    fig_m = px.bar(
        df_mod,
        x="Partido / Fase",
        y=["Equipo Principal", "Oponente (IDV)"],
        barmode="group",
        title=f"Desempeño Comparativo por Partido - {modulo}",
        color_discrete_sequence=[COLOR_PRIMARY, COLOR_SECONDARY],
    )
    fig_m.update_layout(
        plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
    )
    st.plotly_chart(fig_m, use_container_width=True)

    st.markdown(
        f"<div style='background-color:{COLOR_LIGHT_BG}; padding:15px;"
        f" border-left:4px solid {COLOR_SUCCESS}; border-radius:4px;'>"
        f"<strong>Nota de Dirección Táctica:</strong> Este módulo evalúa los"
        f" patrones de comportamiento estructural y métricas avanzadas de"
        f" rendimiento para la toma de decisiones.</div>",
        unsafe_allow_html=True,
    )

# Pie de página
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 11px;'>Dirección"
    " Analítica: Nicolay Gracia</p>",
    unsafe_allow_html=True,
)