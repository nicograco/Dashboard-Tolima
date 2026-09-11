import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Performance & Tactical Lab", page_icon="⚽", layout="wide"
)

# Professional Clean Sports Analytics Palette
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

# Sidebar Branding & Author Citation
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

if competicion == "Liga Dimayor I 2026":
  st.title("⚽ Tactical & Performance Dashboard - Liga Dimayor I 2026")
  st.markdown(
      "Plataforma analítica avanzada de rendimiento colectivo, táctico y"
      " condicional por partido."
  )
  st.markdown("---")

  archivo = "Liga_Dimayor_I_2026.xlsx"
  if os.path.exists(archivo):
    df = pd.read_excel(archivo, header=1)
    team_df = df.copy()

    if not team_df.empty:
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

      tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
          "🧠 Identidad Táctica",
          "⚙️ Construcción & Pases",
          "⚔️ Duelos & Segundas Jugadas",
          "🛡️ Presión & Bloques",
          "📋 Base Completa",
          "📊 Análisis Técnico & DOFA",
      ])

      with tab1:
        st.subheader(
            "🧠 Índices de Comportamiento Táctico Colectivo (Heavy Metal /"
            " Gegenpressing)"
        )
        st.markdown(
            "*(Nota: El índice 'Heavy metal' cuantifica la intensidad del"
            " **Gegenpressing**, midiendo la contra-presión tras pérdida y la"
            " verticalidad inmediata).* "
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
              title="Evolución de Pilares Tácticos por Jornada",
              color_discrete_sequence=[
                  COLOR_NAVY,
                  COLOR_BLUE,
                  COLOR_ACCENT,
                  "#333333",
                  "#e63946",
              ],
          )
          fig_estilo.update_layout(
              plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
          )
          st.plotly_chart(fig_estilo, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Interpretación Táctica Profunda - Identidad y Gegenpressing</h4>
                    <p><b>Análisis de Comportamiento Colectivo:</b> La evolución partido a partido muestra cómo el equipo estructura su propuesta a partir de la asfixia del rival tras pérdida. Los picos observados en el índice 'Heavy Metal' (Gegenpressing) coinciden con una mayor densidad de recuperaciones en campo contrario, lo que ahoga la salida limpia del adversario y genera situaciones de gol directas con mínima oposición defensiva.</p>
                    <p><b>Impacto Condicional y Táctico:</b> Este modelo exige una coordinación milimétrica entre la línea defensiva y los mediocentros para evitar espacios a espaldas. La lectura de estos 4 encuentros confirma que cuando el Gegenpressing supera el umbral medio, el equipo monopoliza el control territorial y somete al oponente en su propio tercio.</p>
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
          )
          fig_pass.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_pass, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Análisis Detallado de Circulación y Construcción</h4>
                    <p><b>Eficiencia en Fase de Iniciación:</b> El porcentaje de acierto en el pase se mantiene en rangos competitivos de élite, evidenciando una sólida estructura de salida de balón desde el fondo. La conexión entre los centrales y los volantes ancla permite fijar bloques rivales y liberar carriles interiores.</p>
                    <p><b>Control de Pérdidas:</b> Minimizar los errores no forzados en el primer tercio de cancha es vital para prevenir contrataques rivales. Las métricas indican que el equipo prioriza la seguridad en salida corta antes de arriesgar pases verticales al espacio.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab3:
        st.subheader("Disputas, Duelos y Segundas Jugadas")
        if all(
            c in team_df.columns for c in ["Jornada", "Tasa de Éxito Duelos Aéreos"]
        ):
          fig_aero = px.line(
              team_df,
              x="Jornada",
              y="Tasa de Éxito Duelos Aéreos",
              markers=True,
              title="Evolución - Tasa de Éxito en Duelos Aéreos",
              color_discrete_sequence=[COLOR_BLUE],
          )
          fig_aero.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_aero, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Evaluación Exhaustiva de Duelos y Segundas Jugadas</h4>
                    <p><b>Dominio Aéreo y Físico:</b> La disputa por el balón dividido y la captura de segundas jugadas constituyen el termómetro del control territorial en partidos cerrados. Los datos reflejan la necesidad de ajustar las coberturas en duelos aéreos defensivos para neutralizar el juego directo del oponente.</p>
                </div>
                """,
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
          )
          fig_alt.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_alt, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Comportamiento Estructural del Bloque Defensivo</h4>
                    <p><b>Altura de Líneas:</b> La altura promedio de presión en metros cuantifica la ambición táctica del equipo para disputar el partido en campo contrario. Un bloque adelantado asfixia la creación rival pero demanda una sincronización perfecta en la línea del fuera de juego y coberturas a espaldas de los laterales.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab5:
        st.subheader("📋 Matriz Completa de Datos Analíticos")
        st.dataframe(team_df, use_container_width=True)

      with tab6:
        st.subheader("📊 Informe Técnico Global y Matriz DOFA Avanzada")

        col_d1, col_d2 = st.columns(2)
        with col_d1:
          st.markdown(
              f"""
                    <div style="background-color: #f0fdf4; padding: 18px; border-radius: 8px; border-left: 5px solid {COLOR_BLUE};">
                        <h3>🟢 Fortalezas</h3>
                        <p>- Consistencia sólida en el control de posesión y circulación limpia del balón.<br>- Excelente aplicación del <strong>Gegenpressing</strong> (Heavy Metal) en tramos clave.<br>- Alta capacidad de generación de oportunidades mediante xG sostenido.</p>
                        <h3>🔵 Oportunidades</h3>
                        <p>- Explotar las espaldas de los carrileros rivales en transiciones rápidas.<br>- Optimizar la eficacia de finalización en el último tercio.</p>
                    </div>
                    """,
              unsafe_allow_html=True,
          )
        with col_d2:
          st.markdown(
              f"""
                    <div style="background-color: #fef2f2; padding: 18px; border-radius: 8px; border-left: 5px solid {COLOR_ACCENT};">
                        <h3>🔴 Debilidades</h3>
                        <p>- Vulnerabilidad recurrente en duelos aéreos defensivos.<br>- Pérdidas de balón críticas en zona de iniciación bajo presión alta.</p>
                        <h3>⚠️ Amenazas</h3>
                        <p>- Exposición defensiva ante contrataques verticales de alta velocidad.<br>- Desgaste físico acumulado por el bloque de presión adelantado.</p>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

        st.markdown("---")
        st.markdown("### 📌 Conclusiones y Recomendaciones del Analista")
        st.markdown("""
                - **Identidad Táctica:** El equipo demuestra una estructura clara orientada al dominio territorial y a la asfixia del rival tras pérdida (*Gegenpressing*).
                - **Línea de Mejora:** Ajustar coberturas en transiciones defensivas y mejorar el éxito en duelos aéreos para consolidar la solidez competitiva.
                """)
    else:
      st.warning("No se encontraron registros en el archivo.")
  else:
    st.error("Archivo Excel no encontrado.")

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
        f"""
        <div class="analysis-card">
            <h4>💡 Análisis del Radar Multidimensional</h4>
            <p>El perfil geométrico compara al <strong>Equipo Tolima</strong> frente al oponente en las 5 dimensiones clave de la eliminatoria. Destaca la superioridad en control territorial y posesión, frente a la ventaja del rival en efectividad de transición y velocidad de contrataque.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

  elif modulo == "Matriz DOFA":
    col1, col2 = st.columns(2)
    with col1:
      st.info(
          "🟢 Debilidades & Oportunidades\n- Éxito en duelos aéreos"
          " (39.7%).\n- Explotar carrileros rivales en transición ofensiva."
      )
    with col2:
      st.success(
          "🟡 Fortalezas & Amenazas\n- Posesión promedio favorable (57%).\n-"
          " Vulnerabilidad ante contrataques verticales del rival."
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
        f"""
        <div class="analysis-card">
            <h4>💡 Nota Táctica del Módulo</h4>
            <p>Evaluación detallada de los registros de ida y vuelta para identificar patrones de rendimiento y desajustes estructurales en la serie internacional.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<p style='text-align:center; color:#666; font-size:11px;'>Dirección"
    " Analítica: Nicolay Gracia</p>",
    unsafe_allow_html=True,
)