import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Elite Match Analytics Lab", page_icon="⚡", layout="wide"
)

# ----------------------------------------------------
# PALETA DE COLORES FUTURISTA DE ALTO IMPACTO
# ----------------------------------------------------
PRIMARY = "#00f5d4"  # Turquesa Neón
SECONDARY = "#7209b7"  # Púrpura Tecnológico
ACCENT = "#f72585"  # Magenta Vibrante
DARK = "#03045e"  # Azul Oscuro Profundo
LIGHT = "#f8f9fa"  # Fondo Claro

# Estilos CSS Modernos y Tarjetas
st.markdown(
    f"""
    <style>
    .metric-box {{
        background-color: {LIGHT};
        border-left: 6px solid {SECONDARY};
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }}
    .metric-val {{
        font-size: 26px;
        font-weight: 800;
        color: {DARK};
    }}
    .metric-lab {{
        font-size: 12px;
        color: #444;
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
    <div style="background: linear-gradient(45deg, {SECONDARY}, {ACCENT}); padding: 18px; border-radius: 10px; text-align: center;">
        <h2 style="color: white; margin: 0; font-size: 18px; font-weight: 800;">ELITE LAB</h2>
        <p style="color: #ffd166; font-size: 11px; margin: 4px 0 0 0; font-weight: 600;">Advanced Match Analytics</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
competicion = st.sidebar.selectbox(
    "🏆 Seleccionar Competición:",
    ["Liga Dimayor I 2026 (Análisis de Equipo)", "Copa Libertadores (Serie Táctica)"],
)

# ====================================================
# OPCIÓN 1: LIGA DIMAYOR I 2026 (ANÁLISIS PROFUNDO)
# ====================================================
if competicion == "Liga Dimayor I 2026 (Análisis de Equipo)":
  st.title("⚡ Elite Match Analytics - Liga Dimayor I 2026")
  st.markdown(
      "Plataforma avanzada de procesamiento de datos tácticos, físicos y"
      " condicionales por partido."
  )
  st.markdown("---")

  archivo_liga = "Liga_Dimayor_I_2026.xlsx"
  if os.path.exists(archivo_liga):
    df_liga = pd.read_excel(archivo_liga, header=1)
    team_df = df_liga[
        df_liga["Equipo"].astype(str).str.contains("Tolima", case=False, na=False)
    ].copy()

    if team_df.empty:
      team_df = df_liga.copy()  # Respaldo si no encuentra el filtro exacto

    if not team_df.empty:
      # Resumen Superior Rápido con tarjetas modernas
      col1, col2, col3, col4, col5 = st.columns(5)
      with col1:
        st.markdown(
            f'<div class="metric-box"><div'
            f' class="metric-lab">Registros</div><div'
            f' class="metric-val">{len(team_df)}</div></div>',
            unsafe_allow_html=True,
        )
      with col2:
        if "Goles" in team_df.columns:
          total_g = team_df["Goles"].sum()
          st.markdown(
              f'<div class="metric-box"><div class="metric-lab">Goles'
              f' Favor</div><div class="metric-val">{int(total_g)}</div></div>',
              unsafe_allow_html=True,
          )
      with col3:
        if "Goles (Rival)" in team_df.columns:
          total_gc = team_df["Goles (Rival)"].sum()
          st.markdown(
              f'<div class="metric-box"><div class="metric-lab">Goles'
              f' Contra</div><div class="metric-val">{int(total_gc)}</div></div>',
              unsafe_allow_html=True,
          )
      with col4:
        if "xG basado en la posición del rematador" in team_df.columns:
          xg_m = team_df["xG basado en la posición del rematador"].mean()
          st.markdown(
              f'<div class="metric-box"><div class="metric-lab">xG'
              f' Promedio</div><div class="metric-val">{xg_m:.2f}</div></div>',
              unsafe_allow_html=True,
          )
      with col5:
        if "Posesión y control" in team_df.columns:
          poss_m = team_df["Posesión y control"].mean() * 100
          st.markdown(
              f'<div class="metric-box"><div'
              f' class="metric-lab">Posesión</div><div'
              f' class="metric-val">{poss_m:.1f}%</div></div>',
              unsafe_allow_html=True,
          )

      st.markdown("---")

      # Pestañas profesionales de análisis
      tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
          "🧠 Identidad Táctica",
          "⚙️ Construcción & Pases",
          "⚔️ Duelos & Segundas Jugadas",
          "🛡️ Presión & Bloques",
          "🎯 Eficiencia & xG",
          "📋 Base Completa",
      ])

      with tab1:
        st.subheader(
            "🧠 Índices de Comportamiento Táctico Colectivo (Heavy Metal /"
            " Gegenpressing)"
        )
        st.markdown(
            "*(Nota técnica: El índice 'Heavy metal' cuantifica la intensidad"
            " del **Gegenpressing**, midiendo la contra-presión tras pérdida y"
            " la verticalidad inmediata en transición).* "
        )

        cols_estilo = [
            "Jornada",
            "Heavy metal",
            "Presión asfixiante",
            "Contra-ataque",
            "Seguridad lo primero",
            "Directo y Aéreo",
        ]
        cols_exist = [c for c in cols_estilo if c in team_df.columns]
        if len(cols_exist) > 1:
          fig_estilo = px.line(
              team_df,
              x="Jornada",
              y=cols_exist[1:],
              markers=True,
              title=(
                  "Evolución de Pilares Tácticos por Jornada (Incluyendo"
                  " Gegenpressing)"
              ),
              color_discrete_sequence=[
                  SECONDARY,
                  ACCENT,
                  PRIMARY,
                  "#3a86ff",
                  "#fb8500",
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
          if "Acierto en el pase" in team_df.columns:
            fig_pass = px.bar(
                team_df,
                x="Jornada",
                y="Acierto en el pase",
                title="Porcentaje de Éxito en Pases (%)",
                color_discrete_sequence=[SECONDARY],
                text_auto=".3f",
            )
            fig_pass.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_pass, use_container_width=True)
        with c2:
          if "Balones críticos perdidos" in team_df.columns:
            fig_perd = px.bar(
                team_df,
                x="Jornada",
                y="Balones críticos perdidos",
                title="Balones Críticos Perdidos en Salida",
                color_discrete_sequence=[ACCENT],
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
          if "Tasa de Éxito Duelos Aéreos" in team_df.columns:
            fig_aero = px.line(
                team_df,
                x="Jornada",
                y="Tasa de Éxito Duelos Aéreos",
                markers=True,
                title="Evolución - Tasa de Éxito en Duelos Aéreos",
                color_discrete_sequence=[PRIMARY],
            )
            fig_aero.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_aero, use_container_width=True)
        with c2:
          if "Tasa de victorias de segundas jugadas (%)" in team_df.columns:
            fig_seg = px.bar(
                team_df,
                x="Jornada",
                y="Tasa de victorias de segundas jugadas (%)",
                title="Tasa de Éxito en Segundas Jugadas (%)",
                color_discrete_sequence=[SECONDARY],
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
          if "Altura de presión promedio (m)" in team_df.columns:
            fig_alt = px.bar(
                team_df,
                x="Jornada",
                y="Altura de presión promedio (m)",
                title="Altura Promedio de Presión Defensiva (Metros)",
                color_discrete_sequence=[ACCENT],
                text_auto=True,
            )
            fig_alt.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_alt, use_container_width=True)
        with c2:
          if "Intervenciones Defensivas" in team_df.columns:
            fig_int = px.bar(
                team_df,
                x="Jornada",
                y="Intervenciones Defensivas",
                title="Volumen de Intervenciones Defensivas",
                color_discrete_sequence=[PRIMARY],
                text_auto=True,
            )
            fig_int.update_layout(
                plot_bgcolor="white", paper_bgcolor="white"
            )
            st.plotly_chart(fig_int, use_container_width=True)

      with tab5:
        st.subheader("Eficiencia Ofensiva y xG (Goles Esperados)")
        if all(
            col in team_df.columns
            for col in [
                "Jornada",
                "Goles",
                "xG basado en la posición del rematador",
                "Tiros totales",
                "Disparos a portería",
            ]
        ):
          fig_xg_match = px.bar(
              team_df,
              x="Jornada",
              y=["Goles", "xG basado en la posición del rematador"],
              barmode="group",
              title="Comparativa Goles Reales vs xG por Partido",
              color_discrete_sequence=[SECONDARY, PRIMARY],
          )
          fig_xg_match.update_layout(
              plot_bgcolor="white", paper_bgcolor="white"
          )
          st.plotly_chart(fig_xg_match, use_container_width=True)

          fig_tiros = px.scatter(
              team_df,
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
                  SECONDARY,
                  ACCENT,
                  PRIMARY,
                  "#3a86ff",
                  "#fb8500",
              ],
          )
          fig_tiros.update_layout(
              plot_bgcolor="white", paper_bgcolor="white"
          )
          st.plotly_chart(fig_tiros, use_container_width=True)

      with tab6:
        st.subheader("📋 Base Completa de Datos Analíticos (Liga Dimayor)")
        st.dataframe(team_df, use_container_width=True)
    else:
      st.warning("No se encontraron registros en el archivo de Liga.")
  else:
    st.error("Archivo 'Liga_Dimayor_I_2026.xlsx' no encontrado en el directorio.")

# ====================================================
# OPCIÓN 2: COPA LIBERTADORES (SERIE TÁCTICA Y MÓDULOS)
# ====================================================
else:
  st.title("⚡ Copa Libertadores - Análisis de Serie Táctica")
  st.markdown(
      "Evaluación multidimensional de la eliminatoria con métricas avanzadas."
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

  # Resumen Superior Rápido para Libertadores
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.markdown(
        f'<div class="metric-box"><div class="metric-label">Control'
        f' Posesión</div><div class="metric-value">57%</div><div'
        f' style="color:{SECONDARY}; font-size:12px; font-weight:bold;">↑'
        " Control territorial pasivo</div></div>",
        unsafe_allow_html=True,
    )
  with col2:
    st.markdown(
        f'<div class="metric-box"><div class="metric-label">Contra-ataque'
        f' Rival</div><div class="metric-value">0.81</div><div'
        f' style="color:{ACCENT}; font-size:12px; font-weight:bold;">↑'
        " Vulnerabilidad crítica</div></div>",
        unsafe_allow_html=True,
    )
  with col3:
    st.markdown(
        f'<div class="metric-box"><div class="metric-label">xG Rematador'
        f' (Vuelta)</div><div class="metric-value">3.42</div><div'
        f' style="color:{PRIMARY}; font-size:12px; font-weight:bold;">↑'
        " Exposición defensiva</div></div>",
        unsafe_allow_html=True,
    )
  with col4:
    st.markdown(
        f'<div class="metric-box"><div class="metric-label">Éxito Duelos'
        f' Aéreos</div><div class="metric-value">39.7%</div><div'
        f' style="color:{ACCENT}; font-size:12px; font-weight:bold;">↑ Déficit'
        " estructural</div></div>",
        unsafe_allow_html=True,
    )

  st.markdown("---")
  st.subheader(f"Módulo Activo: {modulo}")

  if modulo == "Radar Multivariable General":
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
            r=[78, 85, 62, 70, 72],
            theta=categories,
            fill="toself",
            name="Equipo Principal",
            line_color=SECONDARY,
            fillcolor="rgba(114, 9, 183, 0.2)",
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=[68, 90, 75, 88, 65],
            theta=categories,
            fill="toself",
            name="Oponente (IDV)",
            line_color=ACCENT,
            fillcolor="rgba(247, 37, 133, 0.15)",
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
    col_d1, col_d2 = st.columns(2)
    with col_d1:
      st.markdown(
          f"<div style='background-color:#f5f3ff; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {SECONDARY};'><h3>🟢 Debilidades</h3><p>- Bajo porcentaje de"
          " éxito en duelos aéreos (39.7%).<br>- Pérdidas críticas en salida en"
          " zona baja.</p></div>",
          unsafe_allow_html=True,
      )
      st.markdown(
          f"<div style='background-color:#e0f2fe; padding:15px;"
          f" border-radius:8px; border-left:5px solid {PRIMARY};"
          " margin-top:15px;'><h3>🔵 Oportunidades</h3><p>- Explotar las espaldas"
          " de los carrileros rivales en transiciones ofensivas.</p></div>",
          unsafe_allow_html=True,
      )
    with col_d2:
      st.markdown(
          f"<div style='background-color:#fdf4ff; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {ACCENT};'><h3>🟡 Fortalezas</h3><p>- Superioridad en control de"
          " posesión (57% promedio).<br>- Consistencia en la generación de"
          " xG.</p></div>",
          unsafe_allow_html=True,
      )
      st.markdown(
          f"<div style='background-color:#fff1f2; padding:15px;"
          f" border-radius:8px; border-left:5px solid"
          f" {DARK};'><h3>🔴 Amenazas</h3><p>- Vulnerabilidad ante"
          " contra-ataques verticales con alta velocidad del rival.</p></div>",
          unsafe_allow_html=True,
      )

  else:
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
        color_discrete_sequence=[SECONDARY, ACCENT],
    )
    fig_m.update_layout(
        plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
    )
    st.plotly_chart(fig_m, use_container_width=True)

    st.markdown(
        f"<div style='background-color:{LIGHT}; padding:15px;"
        f" border-left:4px solid {PRIMARY}; border-radius:4px;'>"
        f"<strong>Nota de Dirección Táctica:</strong> Este módulo evalúa los"
        f" patrones de comportamiento estructural y métricas avanzadas de"
        f" rendimiento para la toma de decisiones del cuerpo técnico.</div>",
        unsafe_allow_html=True,
    )

# Pie de página
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='text-align:center; color:#777; font-size:11px;'>Elite Match"
    " Analytics Lab</p>",
    unsafe_allow_html=True,
)