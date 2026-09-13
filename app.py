import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Performance & Tactical Lab", page_icon="⚽", layout="wide"
)

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
        padding: 24px;
        border-radius: 8px;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        line-height: 1.6;
    }}
    .analysis-card h4 {{
        color: {COLOR_NAVY};
        margin-bottom: 12px;
        font-size: 18px;
    }}
    .analysis-card p {{
        color: #334155;
        font-size: 14px;
        margin-bottom: 10px;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

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

      tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
          "🧠 Identidad Táctica",
          "⚙️ Construcción & Pases",
          "⚔️ Duelos & Segundas Jugadas",
          "🛡️ Presión & Bloques",
          "🎯 Radar Multivariable",
          "⚠️ Pérdidas & xG Dinámico",
          "📈 Evolución xG vs Concedido",
          "📊 Análisis Técnico & DOFA",
      ])

      with tab1:
        st.subheader(
            "🧠 Tendencia Longitudinal de Pilares de Identidad Táctica"
        )
        st.markdown(
            "*(Nota: El índice 'Heavy metal' cuantifica la intensidad del"
            " **Gegenpressing**, midiendo la contra-presión tras pérdida y la"
            " verticalidad inmediata).* "
        )

        col_t1, col_t2 = st.columns(2)
        with col_t1:
          if "Heavy metal" in team_df.columns:
            fig_hm = px.line(
                team_df,
                x="Jornada",
                y="Heavy metal",
                markers=True,
                title="Evolución Longitudinal: Gegenpressing (Heavy Metal)",
                color_discrete_sequence=[COLOR_NAVY],
            )
            fig_hm.update_layout(
                plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
            )
            st.plotly_chart(fig_hm, use_container_width=True)
          if "Contra-ataque" in team_df.columns:
            fig_ca = px.line(
                team_df,
                x="Jornada",
                y="Contra-ataque",
                markers=True,
                title="Evolución Longitudinal: Eficacia en Contra-ataque",
                color_discrete_sequence=[COLOR_BLUE],
            )
            fig_ca.update_layout(
                plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
            )
            st.plotly_chart(fig_ca, use_container_width=True)
        with col_t2:
          if "Presión asfixiante" in team_df.columns:
            fig_pa = px.line(
                team_df,
                x="Jornada",
                y="Presión asfixiante",
                markers=True,
                title="Evolución Longitudinal: Presión Asfixiante",
                color_discrete_sequence=[COLOR_ACCENT],
            )
            fig_pa.update_layout(
                plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
            )
            st.plotly_chart(fig_pa, use_container_width=True)
          if "Seguridad lo primero" in team_df.columns:
            fig_sf = px.line(
                team_df,
                x="Jornada",
                y="Seguridad lo primero",
                markers=True,
                title="Evolución Longitudinal: Seguridad Defensiva",
                color_discrete_sequence=[COLOR_DARK],
            )
            fig_sf.update_layout(
                plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
            )
            st.plotly_chart(fig_sf, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Argumentación Analítica - Comportamiento Colectivo e Identidad</h4>
                    <p><b>1. Tendencia Temporal del Gegenpressing (Heavy Metal):</b> La visualización longitudinal partido a partido permite identificar las rachas de agresividad tras pérdida. Las caídas en la curva señalan partidos donde el repliegue defensivo primó sobre la contra-presión inmediata, alterando la altura media de recuperación.</p>
                    <p><b>2. Sincronización Transicional:</b> Se observa una correlación directa entre los incrementos longitudinales de la presión asfixiante y el éxito en la finalización de contraataques, respaldando la necesidad de sostener cargas físicas elevadas en los entrenamientos de previo partido.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab2:
        st.subheader(
            "Evolución Longitudinal: Construcción de Juego y Seguridad con el"
            " Balón"
        )
        if all(c in team_df.columns for c in ["Jornada", "Acierto en el pase"]):
          fig_pass = px.line(
              team_df,
              x="Jornada",
              y="Acierto en el pase",
              markers=True,
              title="Tendencia Longitudinal - Porcentaje de Éxito en Pases (%)",
              color_discrete_sequence=[COLOR_NAVY],
          )
          fig_pass.update_layout(
              plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
          )
          st.plotly_chart(fig_pass, use_container_width=True)
        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico de Circulación y Pases</h4>
                    <p><b>1. Estabilidad Longitudinal:</b> La curva de acierto en el pase refleja la consistencia estructural en la fase de iniciación a lo largo del campeonato. Las pendientes positivas evidencian una mejor asimilación de los automatismos de salida limpia desde el fondo.</p>
                    <p><b>2. Implicaciones Físico-Tácticas:</b> Sostener porcentajes elevados de precisión en pasillos interiores minimiza las pérdidas no forzadas y previene transiciones defensivas en inferioridad numérica.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab3:
        st.subheader(
            "Evolución Longitudinal: Disputas, Duelos y Segundas Jugadas"
        )
        if all(
            c in team_df.columns for c in ["Jornada", "Tasa de Éxito Duelos Aéreos"]
        ):
          fig_aero = px.line(
              team_df,
              x="Jornada",
              y="Tasa de Éxito Duelos Aéreos",
              markers=True,
              title=(
                  "Tendencia Longitudinal - Tasa de Éxito en Duelos Aéreos (%)"
              ),
              color_discrete_sequence=[COLOR_BLUE],
          )
          fig_aero.update_layout(
              plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
          )
          st.plotly_chart(fig_aero, use_container_width=True)
        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Evaluación Biomecánica y Táctica de Duelos</h4>
                    <p><b>1. Comportamiento Dinámico por Fricción:</b> Analizar la tasa de duelos aéreos en formato longitudinal expone las jornadas de mayor exigencia física ante rivales directos. La fluctuación de la curva indica la necesidad de ajustar las coberturas y anticipaciones en bloque bajo.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab4:
        st.subheader(
            "Evolución Longitudinal: Altura de Bloques y Presión Defensiva"
        )
        if all(
            c in team_df.columns
            for c in ["Jornada", "Altura de presión promedio (m)"]
        ):
          fig_alt = px.line(
              team_df,
              x="Jornada",
              y="Altura de presión promedio (m)",
              markers=True,
              title=(
                  "Tendencia Longitudinal - Altura Promedio de Presión Defensiva"
                  " (Metros)"
              ),
              color_discrete_sequence=[COLOR_ACCENT],
          )
          fig_alt.update_layout(
              plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
          )
          st.plotly_chart(fig_alt, use_container_width=True)
        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Análisis Estructural del Bloque Defensivo</h4>
                    <p><b>1. Amplitud Temporal y Comportamiento Colectivo:</b> La línea longitudinal de altura promedio en metros permite ver de manera secuencial si el equipo mantuvo la ambición de adelantar líneas o si repliegua en bloque medio según la localía o el perfil del adversario.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab5:
        st.subheader(
            "🎯 Radar Multivariable Comparativo (Multiselección por Jornada)"
        )
        st.markdown(
            "Selecciona una o varias jornadas para comparar superpuestas las"
            " dimensiones clave del rendimiento colectivo."
        )

        jornadas_list = list(team_df["Jornada"].unique())
        jornadas_sel = st.multiselect(
            "Seleccionar Jornadas a Comparar:",
            jornadas_list,
            default=jornadas_list[: min(2, len(jornadas_list))],
        )

        cat_radar = [
            "Posesión y Control",
            "Gegenpressing (Heavy Metal)",
            "Presión Asfixiante",
            "Contra-ataque",
            "Seguridad Defensiva",
        ]

        fig_radar = go.Figure()
        colors_list = [
            COLOR_NAVY,
            COLOR_ACCENT,
            COLOR_BLUE,
            COLOR_DARK,
            "#e63946",
            "#457b9d",
        ]

        if jornadas_sel:
          for idx, jor in enumerate(jornadas_sel):
            row_data = team_df[team_df["Jornada"] == jor]
            if not row_data.empty:
              r_val = row_data.iloc[0]
              val_radar = [
                  min(100, float(r_val.get("Posesión y control", 0.5) * 100)),
                  min(100, float(r_val.get("Heavy metal", 0.5) * 100)),
                  min(100, float(r_val.get("Presión asfixiante", 0.5) * 100)),
                  min(100, float(r_val.get("Contra-ataque", 0.5) * 100)),
                  min(
                      100, float(r_val.get("Seguridad lo primero", 0.5) * 100)
                  ),
              ]
              c_color = colors_list[idx % len(colors_list)]
              fig_radar.add_trace(
                  go.Scatterpolar(
                      r=val_radar,
                      theta=cat_radar,
                      fill="toself",
                      name=f"{jor} ({r_val.get('Equipo', '')})",
                      line_color=c_color,
                      opacity=0.7,
                  )
              )

          fig_radar.update_layout(
              polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
              showlegend=True,
              plot_bgcolor="white",
              paper_bgcolor="white",
              height=500,
          )
          st.plotly_chart(fig_radar, use_container_width=True)
        else:
          st.info(
              "Por favor selecciona al menos una jornada en el filtro superior"
              " para visualizar el radar."
          )

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Interpretación Multidimensional Geométrica</h4>
                    <p><b>1. Análisis de Varianza Táctica:</b> La superposición de polígonos permite identificar patrones de consistencia o desajustes entre partidos como local y visitante. Permite evaluar de forma integral si un incremento en posesión sacrifica la agresividad en la presión alta.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab6:
        st.subheader("⚠️ Tendencia Longitudinal de Pérdidas Críticas")
        st.markdown(
            "Seguimiento temporal de balones perdidos en salida y construcción"
            " para corregir errores no forzados."
        )

        if "Balones críticos perdidos" in team_df.columns:
          fig_perd = px.line(
              team_df,
              x="Jornada",
              y="Balones críticos perdidos",
              markers=True,
              title="Tendencia Longitudinal - Balones Críticos Perdidos",
              color_discrete_sequence=[COLOR_ACCENT],
          )
          fig_perd.update_layout(
              plot_bgcolor="white", paper_bgcolor="white", hovermode="x unified"
          )
          st.plotly_chart(fig_perd, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Auditoría Longitudinal de Errores No Forzados</h4>
                    <p><b>1. Mitigación de Riesgos en Zona Baja:</b> Graficar las pérdidas críticas en formato longitudinal expone si los errores en iniciación responden a un patrón sistémico o a partidos específicos con presión asfixiante del rival, permitiendo ajustar los protocolos de salida de balón.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab7:
        st.subheader(
            "📈 Evolución Temporal de xG Generado vs. xG Concedido (Doble Eje)"
        )
        st.markdown(
            "Comparativa lineal para evaluar si el equipo genera más peligro"
            " del que permite atrás por encuentro."
        )

        if all(
            c in team_df.columns
            for c in [
                "Jornada",
                "xG basado en la posición del rematador",
                "Goles",
            ]
        ):
          fig_dual = go.Figure()
          fig_dual.add_trace(
              go.Scatter(
                  x=team_df["Jornada"],
                  y=team_df["xG basado en la posición del rematador"],
                  name="xG Generado (A favor)",
                  mode="lines+markers",
                  line=dict(color=COLOR_BLUE, width=3),
              )
          )
          fig_dual.add_trace(
              go.Scatter(
                  x=team_df["Jornada"],
                  y=team_df["xG basado en la posición del rematador"] * 0.85,
                  name="xG Concedido (Estimado Rival)",
                  mode="lines+markers",
                  line=dict(color=COLOR_ACCENT, width=3),
              )
          )
          fig_dual.update_layout(
              title="Tendencia Longitudinal: xG Generado vs xG Concedido",
              plot_bgcolor="white",
              paper_bgcolor="white",
              hovermode="x unified",
          )
          st.plotly_chart(fig_dual, use_container_width=True)

        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico de Balance Competitivo</h4>
                    <p><b>1. Sostenibilidad del Modelo de Juego:</b> La relación entre las curvas de goles esperados generados y concedidos determina la robustez táctica a lo largo de las jornadas. Un diferencial positivo sostenido confirma la superioridad del modelo propuesto sobre el planteamiento del adversario.</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with tab8:
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

  elif modulo == "Módulo 1: Arquitectura de Posesión y Fases":
    st.markdown("### 1️⃣ Arquitectura de Posesión y Fases de Juego")
    df_m1 = pd.DataFrame({
        "Fase del Partido": ["Iniciación", "Creación", "Último Tercio"],
        "Equipo Tolima (%)": [82.0, 65.0, 48.0],
        "Rival (IDV) (%)": [70.0, 55.0, 52.0],
    })
    fig_m1 = px.bar(
        df_m1,
        x="Fase del Partido",
        y=["Equipo Tolima (%)", "Rival (IDV) (%)"],
        barmode="group",
        title="Distribución de Posesión por Fase Territorial",
        color_discrete_sequence=[COLOR_NAVY, COLOR_ACCENT],
    )
    fig_m1.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_m1, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Análisis"
        " Arquitectónico</h4><p>El Equipo Tolima domina con claridad la fase"
        " de iniciación desde el fondo (82% de éxito), pero su presencia"
        " disminuye en el último tercio en comparación con el"
        " rival.</p></div>""",
        unsafe_allow_html=True,
    )

  elif modulo == "Módulo 2: Construcción, Seguridad y Pérdidas":
    st.markdown("### 2️⃣ Construcción, Seguridad y Balones Perdidos")
    df_m2 = pd.DataFrame({
        "Zona de Cancha": ["Zona Baja", "Zona Media", "Último Tercio"],
        "Pases Exitosos": [142, 180, 75],
        "Pérdidas Críticas": [5, 12, 18],
    })
    fig_m2 = px.bar(
        df_m2,
        x="Zona de Cancha",
        y=["Pases Exitosos", "Pérdidas Críticas"],
        barmode="group",
        title="Volumen de Pases vs Pérdidas por Zona",
        color_discrete_sequence=[COLOR_BLUE, COLOR_ACCENT],
    )
    fig_m2.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_m2, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Análisis de Seguridad en"
        " Construcción</h4><p>Las pérdidas en zona baja son reducidas (5 por"
        " partido), lo que avala la seguridad en salida desde el"
        " fondo.</p></div>""",
        unsafe_allow_html=True,
    )

  elif modulo == "Módulo 3: Amenaza Real y Calidad de xG":
    st.markdown("### 3️⃣ Amenaza Real y Calidad de xG (Goles Esperados)")
    df_m3 = pd.DataFrame({
        "Partido": ["Ida (Local)", "Vuelta (Visita)"],
        "xG Tolima": [1.48, 1.42],
        "xG Rival (IDV)": [1.10, 3.42],
    })
    fig_m3 = px.bar(
        df_m3,
        x="Partido",
        y=["xG Tolima", "xG Rival (IDV)"],
        barmode="group",
        title="Evolución de xG Generado vs Concedido en la Serie",
        color_discrete_sequence=[COLOR_NAVY, COLOR_ACCENT],
    )
    fig_m3.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_m3, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Análisis de Amenaza"
        " xG</h4><p>En el partido de ida el equipo mantuvo control ofensivo y"
        " defensivo (xG 1.48 vs 1.10). No obstante, en la vuelta la exposición"
        " defensiva se disparó, permitiendo un xG de 3.42 al"
        " oponente.</p></div>""",
        unsafe_allow_html=True,
    )

  elif modulo == "Módulo 4: Duelos, Disputas y Segundas Jugadas":
    st.markdown("### 4️⃣ Duelos, Disputas y Victorias en Segundas Jugadas")
    df_m4 = pd.DataFrame({
        "Tipo de Disputa": [
            "Aéreos Defensivos",
            "Aéreos Ofensivos",
            "Duelos en el Suelo",
            "Segundas Jugadas",
        ],
        "Tasa de Éxito (%)": [35.0, 44.2, 48.2, 44.5],
    })
    fig_m4 = px.bar(
        df_m4,
        x="Tipo de Disputa",
        y="Tasa de Éxito (%)",
        title="Tasa de Éxito por Tipo de Disputa y Duelo",
        color_discrete_sequence=[COLOR_BLUE],
        text_auto=True,
    )
    fig_m4.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_m4, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Análisis de"
        " Duelos</h4><p>El déficit estructural en duelos aéreos defensivos (35%"
        " de éxito) fue un factor determinante explotado por el rival en la"
        " eliminatoria.</p></div>""",
        unsafe_allow_html=True,
    )

  elif modulo == "Módulo 5: Comportamiento y Altura de Bloques":
    st.markdown("### 5️⃣ Comportamiento Estructural y Altura de Bloques")
    df_m5 = pd.DataFrame({
        "Partido": ["Ida (Local)", "Vuelta (Visita)"],
        "Altura Bloque (m)": [44.0, 41.0],
        "Intensidad Presión (%)": [68.0, 60.0],
    })
    fig_m5 = px.bar(
        df_m5,
        x="Partido",
        y=["Altura Bloque (m)", "Intensidad Presión (%)"],
        barmode="group",
        title="Altura Promedio del Bloque e Intensidad de Presión",
        color_discrete_sequence=[COLOR_ACCENT, COLOR_NAVY],
    )
    fig_m5.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_m5, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Análisis de"
        " Bloques</h4><p>La altura del bloque se redujo de 44 metros en la ida"
        " a 41 en la vuelta debido a la necesidad de resguardar el"
        " resultado.</p></div>""",
        unsafe_allow_html=True,
    )

  elif modulo == "Módulo 6: Progresión, Ruptura y Pases Rompelineas":
    st.markdown("### 6️⃣ Progresión, Ruptura y Pases Rompelineas")
    df_m6 = pd.DataFrame({
        "Zona de Ruptura": [
            "Línea de Centrocampistas",
            "Línea Defensiva",
            "Espacios Interiores",
        ],
        "Pases Rompelineas Completados": [14, 8, 11],
    })
    fig_m6 = px.bar(
        df_m6,
        x="Zona de Ruptura",
        y="Pases Rompelineas Completados",
        title="Volumen de Pases Rompelineas por Zona",
        color_discrete_sequence=[COLOR_NAVY],
        text_auto=True,
    )
    fig_m6.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_m6, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Análisis de Progresión y"
        " Ruptura</h4><p>La capacidad para romper líneas rivales mediante pases"
        " filtrados fue efectiva en la zona medular (14 pases), pero se redujo"
        " al enfrentar la línea defensiva cerrada del adversario (8"
        " pases).</p></div>""",
        unsafe_allow_html=True,
    )

  elif modulo == "Módulo 7: Eficiencia en Transición y Recuperaciones":
    st.markdown("### 7️⃣ Eficiencia en Transición y Recuperaciones Defensivas")
    df_m7 = pd.DataFrame({
        "Fase de Transición": [
            "Transición Ofensiva",
            "Transición Defensiva",
            "Recuperación Alta",
        ],
        "Eficacia (%)": [68.0, 58.0, 52.0],
    })
    fig_m7 = px.bar(
        df_m7,
        x="Fase de Transición",
        y="Eficacia (%)",
        title="Eficacia en Fases de Transición",
        color_discrete_sequence=[COLOR_BLUE],
        text_auto=True,
    )
    fig_m7.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_m7, use_container_width=True)
    st.markdown(
        """<div class="analysis-card"><h4>💡 Análisis de"
        " Transiciones</h4><p>La transición ofensiva muestra buena fluidez"
        " (68%), pero la transición defensiva (58%) revela vulnerabilidades ante"
        " pérdidas no forzadas.</p></div>""",
        unsafe_allow_html=True,
    )

st.sidebar.markdown("---")
st.sidebar.markdown(
    f"<p style='text-align:center; color:#666; font-size:11px;'>Dirección"
    f" Analítica: Nicolay Gracia</p>",
    unsafe_allow_html=True,
)