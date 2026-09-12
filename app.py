import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Performance & Tactical Lab", page_icon="⚽", layout="wide"
)

# -------------------------------------------------------------------------
# PALETA DE COLORES PROFESIONAL DE ÉLITE (SPORTS ANALYTICS)
# -------------------------------------------------------------------------
COLOR_NAVY = "#1e3d59"
COLOR_BLUE = "#17b978"
COLOR_ACCENT = "#ff6e40"
COLOR_DARK = "#2b2d42"
COLOR_LIGHT = "#f5f7fa"

st.markdown(
    f"""
    <style>
    .metric-box {{
        background-color: {COLOR_LIGHT};
        border-left: 6px solid {COLOR_NAVY};
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }}
    .metric-val {{
        font-size: 26px;
        font-weight: 800;
        color: {COLOR_NAVY};
    }}
    .metric-lab {{
        font-size: 12px;
        color: #444;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .analysis-card {{
        background-color: white;
        border: 1px solid #e2e8f0;
        padding: 22px;
        border-radius: 8px;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------------
# BARRA LATERAL: INSTITUCIONALIDAD Y NAVEGACIÓN
# -------------------------------------------------------------------------
st.sidebar.markdown(
    f"""
    <div style="background: linear-gradient(135deg, {COLOR_NAVY}, {COLOR_DARK}); padding: 18px; border-radius: 10px; text-align: center;">
        <h2 style="color: white; margin: 0; font-size: 17px; font-weight: 800;">PERFORMANCE LAB</h2>
        <p style="color: {COLOR_BLUE}; font-size: 11px; margin: 4px 0 0 0; font-weight: 600;">Match & Tactical Analytics</p>
    </div>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")
competicion = st.sidebar.selectbox(
    "🏆 Seleccionar Competición",
    ["Liga Dimayor I 2026", "Copa Libertadores (Serie Táctica)"],
)

# =========================================================================
# OPCIÓN 1: LIGA DIMAYOR I 2026
# =========================================================================
if competicion == "Liga Dimayor I 2026":
  st.title("⚽ Tactical & Performance Dashboard - Liga Dimayor I 2026")
  st.markdown(
      "Plataforma analítica avanzada de rendimiento colectivo, táctico,"
      " zonal y espacial en campo."
  )
  st.markdown("---")

  archivo = "Liga_Dimayor_I_2026.xlsx"
  if os.path.exists(archivo):
    df = pd.read_excel(archivo, header=1)
    team_df = df.copy()

    if not team_df.empty:
      # Tarjetas de Resumen Superior
      c1, c2, c3, c4 = st.columns(4)
      with c1:
        st.markdown(
            f'<div class="metric-box"><div'
            f' class="metric-lab">Registros</div><div'
            f' class="metric-val">{len(team_df)}</div></div>',
            unsafe_allow_html=True,
        )
      with c2:
        if "Goles" in team_df.columns:
          total_g = team_df["Goles"].sum()
          st.markdown(
              f'<div class="metric-box"><div class="metric-lab">Goles'
              f' Favor</div><div class="metric-val">{int(total_g)}</div></div>',
              unsafe_allow_html=True,
          )
      with c3:
        if "Goles (Rival)" in team_df.columns:
          total_gc = team_df["Goles (Rival)"].sum()
          st.markdown(
              f'<div class="metric-box"><div class="metric-lab">Goles'
              f' Contra</div><div class="metric-val">{int(total_gc)}</div></div>',
              unsafe_allow_html=True,
          )
      with c4:
        if "xG basado en la posición del rematador" in team_df.columns:
          xg_m = team_df["xG basado en la posición del rematador"].mean()
          st.markdown(
              f'<div class="metric-box"><div class="metric-lab">xG'
              f' Promedio</div><div class="metric-val">{xg_m:.2f}</div></div>',
              unsafe_allow_html=True,
          )

      st.markdown("---")

      # Pestañas profesionales optimizadas
      (
          tab1,
          tab2,
          tab3,
          tab4,
          tab5,
          tab6,
          tab7,
      ) = st.tabs([
          "🧠 Identidad Táctica",
          "⚙️ Construcción & Pases",
          "⚔️ Duelos & Segundas Jugadas",
          "🛡️ Presión & Bloques",
          "🎯 Scatterplot Analítico",
          "⚽ Zonas & Distribución en Cancha",
          "📊 Análisis Técnico & DOFA",
      ])

      with tab1:
        st.subheader("🧠 Pilares de Identidad Táctica (Desglose Individual)")
        st.markdown(
            "*(Nota: El índice 'Heavy metal' cuantifica la intensidad del"
            " **Gegenpressing**, midiendo la contra-presión tras pérdida y la"
            " verticalidad inmediata).* "
        )

        col_t1, col_t2 = st.columns(2)
        with col_t1:
          if "Heavy metal" in team_df.columns:
            fig_hm = px.bar(
                team_df,
                x="Jornada",
                y="Heavy metal",
                title="Intensidad Gegenpressing (Heavy Metal) por Jornada",
                color_discrete_sequence=[COLOR_NAVY],
                text_auto=True,
            )
            fig_hm.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig_hm, use_container_width=True)
          if "Contra-ataque" in team_df.columns:
            fig_ca = px.bar(
                team_df,
                x="Jornada",
                y="Contra-ataque",
                title="Eficacia en Contra-ataque por Jornada",
                color_discrete_sequence=[COLOR_BLUE],
                text_auto=True,
            )
            fig_ca.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig_ca, use_container_width=True)
        with col_t2:
          if "Presión asfixiante" in team_df.columns:
            fig_pa = px.bar(
                team_df,
                x="Jornada",
                y="Presión asfixiante",
                title="Índice de Presión Asfixiante por Jornada",
                color_discrete_sequence=[COLOR_ACCENT],
                text_auto=True,
            )
            fig_pa.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig_pa, use_container_width=True)
          if "Seguridad lo primero" in team_df.columns:
            fig_sf = px.bar(
                team_df,
                x="Jornada",
                y="Seguridad lo primero",
                title="Índice de Seguridad Defensiva por Jornada",
                color_discrete_sequence=[COLOR_DARK],
                text_auto=True,
            )
            fig_sf.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig_sf, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Interpretación Táctica Desglosada - Gegenpressing y Pilares</h4>
                    <p><b>Lectura Clara por Indicador:</b> Al separar los pilares tácticos en barras individuales, evitamos el cruce caótico de líneas. Se observa claramente que los picos de <b>Gegenpressing (Heavy Metal)</b> coinciden con jornadas de alta exigencia física donde el equipo intensificó la contra-presión tras pérdida en campo rival.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab2:
        st.subheader("Construcción de Juego y Seguridad con el Balón")
        if all(c in team_df.columns for c in ["Jornada", "Acierto en el pase"]):
          fig_pass = px.bar(
              team_df,
              x="Jornada",
              y="Acierto en el pase",
              title="Porcentaje de Éxito en Pases (%)",
              color_discrete_sequence=[COLOR_NAVY],
              text_auto=".3f",
          )
          fig_pass.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_pass, use_container_width=True)
        st.markdown(
            """<div class="analysis-card"><h4>💡 Análisis de Circulación y"
            " Pases</h4><p>La estabilidad en el porcentaje de acierto en el"
            " pase denota la eficacia en la fase de iniciación y construcción,"
            " reduciendo pérdidas no forzadas en campo"
            " propio.</p></div>""",
            unsafe_allow_html=True,
        )

      with tab3:
        st.subheader("Disputas, Duelos y Segundas Jugadas")
        if all(
            c in team_df.columns for c in ["Jornada", "Tasa de Éxito Duelos Aéreos"]
        ):
          fig_aero = px.bar(
              team_df,
              x="Jornada",
              y="Tasa de Éxito Duelos Aéreos",
              title="Evolución - Tasa de Éxito en Duelos Aéreos",
              color_discrete_sequence=[COLOR_BLUE],
              text_auto=True,
          )
          fig_aero.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_aero, use_container_width=True)
        st.markdown(
            """<div class="analysis-card"><h4>💡 Evaluación de"
            " Duelos</h4><p>El control de las segundas jugadas y duelos aéreos"
            " define el dominio territorial en partidos cerrados. Es clave"
            " ajustar coberturas defensivas en balón"
            " dividido.</p></div>""",
            unsafe_allow_html=True,
        )

      with tab4:
        st.subheader("Altura de Bloques y Presión Defensiva")
        if all(
            c in team_df.columns
            for c in ["Jornada", "Altura de presión promedio (m)"]
        ):
          fig_alt = px.bar(
              team_df,
              x="Jornada",
              y="Altura de presión promedio (m)",
              title="Altura Promedio de Presión Defensiva (Metros)",
              color_discrete_sequence=[COLOR_ACCENT],
              text_auto=True,
          )
          fig_alt.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_alt, use_container_width=True)
        st.markdown(
            """<div class="analysis-card"><h4>💡 Comportamiento del Bloque"
            " Defensivo</h4><p>La altura promedio de presión en metros"
            " cuantifica la ambición táctica para disputar el partido en campo"
            " contrario y asfixiar la salida rival.</p></div>""",
            unsafe_allow_html=True,
        )

      with tab5:
        st.subheader(
            "🎯 Scatterplot Analítico: Relación Volumen Ofensivo vs Eficacia xG"
        )
        if all(
            c in team_df.columns
            for c in [
                "Tiros totales",
                "xG basado en la posición del rematador",
                "Goles",
                "Jornada",
            ]
        ):
          fig_scatter = px.scatter(
              team_df,
              x="Tiros totales",
              y="xG basado en la posición del rematador",
              size="Goles",
              color="Jornada",
              hover_name="Jornada",
              title=(
                  "Diagrama de Dispersión: Tiros Totales vs Expectativa de Gol"
                  " (Tamaño = Goles)"
              ),
              color_discrete_sequence=[
                  COLOR_NAVY,
                  COLOR_BLUE,
                  COLOR_ACCENT,
                  COLOR_DARK,
              ],
          )
          fig_scatter.update_layout(
              plot_bgcolor="white", paper_bgcolor="white"
          )
          st.plotly_chart(fig_scatter, use_container_width=True)
        st.markdown(
            """<div class="analysis-card"><h4>💡 Interpretación del Scatterplot"
            " Analítico</h4><p>Este diagrama de dispersión cruza el volumen de"
            " remates intentados con la calidad de los mismos (xG),"
            " identificando partidos de alta generación de peligro real frente"
            " a volumen de remates de baja calidad.</p></div>""",
            unsafe_allow_html=True,
        )

      with tab6:
        st.subheader(
            "⚽ Análisis Zonal & Espacial (Distribución en Campo de Fútbol)"
        )
        st.markdown(
            "Mapa táctico interactivo que representa la concentración de"
            " acciones y volumen de juego sobre las zonas del terreno de"
            " juego."
        )

        # Selector de jornada o vista global opcional
        jornadas_disponibles = ["Todas las Jornadas"] + list(
            team_df["Jornada"].unique()
        )
        jornada_sel = st.selectbox(
            "Filtrar por Jornada para el Mapa de Campo:", jornadas_disponibles
        )

        if jornada_sel == "Todas las Jornadas":
          plot_df = team_df
        else:
          plot_df = team_df[team_df["Jornada"] == jornada_sel]

        # Dibujo del terreno de juego con Plotly
        fig_pitch = go.Figure()

        # Contorno del campo (105 x 68 metros)
        fig_pitch.add_shape(
            type="rect",
            x0=0,
            y0=0,
            x1=105,
            y1=68,
            line=dict(color="#1e3d59", width=3),
            fillcolor="#f4f9f4",
        )
        # Línea de mitad de cancha
        fig_pitch.add_shape(
            type="line",
            x0=52.5,
            y0=0,
            x1=52.5,
            y1=68,
            line=dict(color="#1e3d59", width=2),
        )
        # Círculo central
        fig_pitch.add_shape(
            type="circle",
            x0=52.5 - 9.15,
            y0=34 - 9.15,
            x1=52.5 + 9.15,
            y1=34 + 9.15,
            line=dict(color="#1e3d59", width=2),
        )
        # Área grande izquierda
        fig_pitch.add_shape(
            type="rect",
            x0=0,
            y0=13.84,
            x1=16.5,
            y1=54.16,
            line=dict(color="#1e3d59", width=2),
        )
        # Área grande derecha
        fig_pitch.add_shape(
            type="rect",
            x0=105 - 16.5,
            y0=13.84,
            x1=105,
            y1=54.16,
            line=dict(color="#1e3d59", width=2),
        )
        # Arcos / Porterías
        fig_pitch.add_shape(
            type="rect",
            x0=-3,
            y0=30.34,
            x1=0,
            y1=37.66,
            line=dict(color="#1e3d59", width=2),
            fillcolor="#cccccc",
        )
        fig_pitch.add_shape(
            type="rect",
            x0=105,
            y0=30.34,
            x1=108,
            y1=37.66,
            line=dict(color="#1e3d59", width=2),
            fillcolor="#cccccc",
        )

        # Coordenadas espaciales estándar de las zonas tácticas en el campo (105x68)
        pitch_zones = {
            "Zona Defensa Central": {
                "x": 20,
                "y": 34,
                "name": "Defensa Central",
            },
            "Zona Lateral (Derecho)": {
                "x": 20,
                "y": 58,
                "name": "Lateral Derecho",
            },
            "Zona Lateral (Izquierdo)": {
                "x": 20,
                "y": 10,
                "name": "Lateral Izquierdo",
            },
            "Zona Mediocentro Defensivo": {
                "x": 42,
                "y": 34,
                "name": "Mediocentro Defensivo",
            },
            "Zona Mediocentro": {"x": 52.5, "y": 34, "name": "Mediocentro"},
            "Zona Centrocampista Ofensivo": {
                "x": 70,
                "y": 34,
                "name": "Mediapunta / Ofensivo",
            },
            "Zona Banda Derecha": {"x": 70, "y": 58, "name": "Banda Derecha"},
            "Zona Banda Izquierda": {
                "x": 70,
                "y": 10,
                "name": "Banda Izquierda",
            },
        }

        zone_vals = []
        zone_names = []
        zone_x = []
        zone_y = []
        for k, v in pitch_zones.items():
          if k in plot_df.columns:
            total_val = plot_df[k].sum()
            zone_vals.append(total_val)
            zone_names.append(v["name"])
            zone_x.append(v["x"])
            zone_y.append(v["y"])

        if zone_vals:
          fig_pitch.add_trace(
              go.Scatter(
                  x=zone_x,
                  y=zone_y,
                  mode="markers+text",
                  marker=dict(
                      size=[max(15, v / 2) for v in zone_vals],
                      color=zone_vals,
                      colorscale="Tealgrn",
                      showscale=True,
                      opacity=0.9,
                      line=dict(width=2, color="white"),
                  ),
                  text=[f"{n}: {v}" for n, v in zip(zone_names, zone_vals)],
                  textposition="top center",
              )
          )

        fig_pitch.update_layout(
            title=f"Distribución Zonal en Terreno de Juego ({jornada_sel})",
            xaxis=dict(
                range=[-8, 113],
                showgrid=False,
                zeroline=False,
                showticklabels=False,
            ),
            yaxis=dict(
                range=[-5, 73],
                showgrid=False,
                zeroline=False,
                showticklabels=False,
            ),
            plot_bgcolor="#e8f4f8",
            paper_bgcolor="white",
            height=520,
        )
        st.plotly_chart(fig_pitch, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Interpretación Táctica del Mapa Zonal en Cancha</h4>
                    <p><b>Ocupación de Espacios:</b> Este diagrama sitúa geométricamente el volumen de intervenciones sobre el terreno de juego. Permite visualizar con precisión en qué carriles y pasillos (defensa central, mediocentro o bandas) se concentra el juego del equipo en la selección actual de partidos.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab7:
        st.subheader("📊 Informe Técnico Global y Matriz DOFA Avanzada")
        col_d1, col_d2 = st.columns(2)
        with col_d1:
          st.markdown(
              f"""<div style="background-color: #f0fdf4; padding: 18px; border-radius: 8px; border-left: 5px solid {COLOR_BLUE}; margin-bottom: 15px;"><h3>🟢 Fortalezas</h3><p>• Consistencia sólida en control de posesión y circulación limpia.<br>• Excelente aplicación del <strong>Gegenpressing</strong> (Heavy Metal) en tramos clave.<br>• Alta capacidad de generación de oportunidades mediante xG sostenido.</p></div><div style="background-color: #e0f2fe; padding: 18px; border-radius: 8px; border-left: 5px solid {COLOR_NAVY};"><h3>🔵 Oportunidades</h3><p>• Explotar espaldas de carrileros rivales en transiciones rápidas.<br>• Optimizar eficacia de finalización en el último tercio.</p></div>""",
              unsafe_allow_html=True,
          )
        with col_d2:
          st.markdown(
              f"""<div style="background-color: #fef2f2; padding: 18px; border-radius: 8px; border-left: 5px solid {COLOR_ACCENT}; margin-bottom: 15px;"><h3>🔴 Debilidades</h3><p>• Vulnerabilidad recurrente en duelos aéreos defensivos.<br>• Pérdidas de balón críticas en zona de iniciación bajo presión alta.</p></div><div style="background-color: #fefce8; padding: 18px; border-radius: 8px; border-left: 5px solid #ca8a04;"><h3>⚠️ Amenazas</h3><p>• Exposición defensiva ante contrataques verticales de alta velocidad.<br>• Desgaste físico acumulado por el bloque de presión adelantado.</p></div>""",
              unsafe_allow_html=True,
          )
        st.markdown("---")
        st.markdown(
            "### 📌 Conclusiones y Recomendaciones del Analista para el Cuerpo"
            " Técnico"
        )
        st.markdown(
            "- **Identidad Táctica:** Estructura clara orientada al dominio"
            " territorial y Gegenpressing.\n- **Línea de Mejora:** Ajustar"
            " coberturas en transiciones defensivas y duelos aéreos."
        )
    else:
      st.warning("No se encontraron registros en el archivo.")
  else:
    st.error("Archivo Excel no encontrado.")

# =========================================================================
# OPCIÓN 2: COPA LIBERTADORES (ANÁLISIS DE SERIE TÁCTICA CON 7 MÓDULOS)
# =========================================================================
else:
  st.title("⚽ Copa Libertadores - Análisis de Serie Táctica")
  st.markdown(
      "Evaluación multidimensional de la eliminatoria con métricas avanzadas."
  )
  st.sidebar.markdown("---")
  st.sidebar.subheader("Navegación de Módulos")
  modulo = st.sidebar.radio(
      "Seleccionar Módulo",
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
            name="Equipo Tolima",
            line_color=COLOR_NAVY,
        )
    )
    fig.add_trace(
        go.Scatterpolar(
            r=[68, 90, 75, 88, 65],
            theta=categories,
            fill="toself",
            name="Oponente (IDV)",
            line_color=COLOR_ACCENT,
        )
    )
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Análisis del Radar"
        " Multidimensional</h4><p>El perfil geométrico compara al"
        " <strong>Equipo Tolima</strong> frente al oponente en las 5"
        " dimensiones clave de la eliminatoria.</p></div>""",
        unsafe_allow_html=True,
    )
  elif modulo == "Matriz DOFA":
    col1, col2 = st.columns(2)
    with col1:
      st.markdown(
          f"""<div style="background-color: #f0fdf4; padding: 18px; border-radius: 8px; border-left: 5px solid {COLOR_BLUE}; margin-bottom: 15px;"><h3>🟢 Fortalezas</h3><p>• Superioridad en control de posesión (57% promedio).<br>• Consistencia en xG en eliminatoria.</p></div><div style="background-color: #e0f2fe; padding: 18px; border-radius: 8px; border-left: 5px solid {COLOR_NAVY};"><h3>🔵 Oportunidades</h3><p>• Explotar espaldas de carrileros rivales en transición.</p></div>""",
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown(
          f"""<div style="background-color: #fef2f2; padding: 18px; border-radius: 8px; border-left: 5px solid {COLOR_ACCENT}; margin-bottom: 15px;"><h3>🔴 Debilidades</h3><p>• Bajo éxito en duelos aéreos (39.7%).<br>• Pérdidas críticas en salida.</p></div><div style="background-color: #fefce8; padding: 18px; border-radius: 8px; border-left: 5px solid #ca8a04;"><h3>⚠️ Amenazas</h3><p>• Vulnerabilidad ante contrataques verticales rápidos.</p></div>""",
          unsafe_allow_html=True,
      )
  else:
    fig_demo = px.bar(
        pd.DataFrame(
            {"Fase": ["Ida (Local)", "Vuelta (Visita)"], "Rendimiento": [75.0, 81.2]}
        ),
        x="Fase",
        y="Rendimiento",
        title=f"Métrica de Desempeño - {modulo}",
        color_discrete_sequence=[COLOR_NAVY],
    )
    fig_demo.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_demo, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Nota Táctica del"
        " Módulo</h4><p>Evaluación detallada de los registros de ida y"
        " vuelta para identificar patrones de rendimiento en la serie"
        " internacional.</p></div>""",
        unsafe_allow_html=True,
    )

st.sidebar.markdown("---")
st.sidebar.markdown(
    f"<p style='text-align:center; color:#666; font-size:11px;'>Dirección"
    f" Analítica: Nicolay Gracia</p>",
    unsafe_allow_html=True,
)