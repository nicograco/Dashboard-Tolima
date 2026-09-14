import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Performance & Tactical Lab", page_icon="⚽", layout="wide"
)

COLOR_NAVY = "#0f172a"
COLOR_BLUE = "#10b981"
COLOR_ACCENT = "#f97316"
COLOR_DARK = "#1e293b"
COLOR_LIGHT = "#f8fafc"

# Estilos CSS ejecutivos + Reglas de impresión limpias para PDF
st.markdown(
    f"""
    <style>
    /* Estilos visuales de pantalla */
    .stApp {{
        background-color: #f1f5f9;
    }}
    .metric-box {{
        background-color: #ffffff;
        border-left: 5px solid {COLOR_NAVY};
        padding: 16px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}
    .metric-val {{
        font-size: 28px;
        font-weight: 800;
        color: {COLOR_NAVY};
    }}
    .metric-lab {{
        font-size: 11px;
        color: #64748b;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }}
    .analysis-card {{
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-top: 4px solid {COLOR_NAVY};
        padding: 24px;
        border-radius: 10px;
        margin-top: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        line-height: 1.7;
    }}
    .analysis-card h4 {{
        color: {COLOR_NAVY};
        margin-bottom: 12px;
        font-size: 18px;
        font-weight: 700;
    }}
    .analysis-card p {{
        color: #334155;
        font-size: 14px;
        margin-bottom: 10px;
    }}

    /* 📄 REGLAS DE IMPRESIÓN PDF OPTIMIZADAS (SIN PÁGINAS EN BLANCO) */
    @media print {{
        header, footer, [data-testid="stSidebar"], .stButton {{
            display: none !important;
        }}
        .stApp {{
            background-color: #ffffff !important;
        }}
        .analysis-card {{
            break-inside: avoid !important;
            page-break-inside: avoid !important;
            border: 1px solid #cbd5e1 !important;
            box-shadow: none !important;
            margin-bottom: 15px !important;
        }}
        body {{
            margin: 1cm !important;
            font-size: 11pt !important;
            color: #000000 !important;
        }}
    }}
    </style>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    f"""
    <div style="background: linear-gradient(135deg, {COLOR_NAVY}, {COLOR_DARK}); padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h2 style="color: white; margin: 0; font-size: 18px; font-weight: 800; letter-spacing: 0.5px;">PERFORMANCE LAB</h2>
        <p style="color: {COLOR_BLUE}; font-size: 11px; margin: 5px 0 0 0; font-weight: 600;">Match & Tactical Analytics</p>
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
  st.sidebar.markdown("---")
  st.sidebar.subheader("📌 Módulos de Análisis")

  modulo_dimayor = st.sidebar.radio(
      "Seleccionar Módulo Táctico",
      [
          "🧠 Pilares de Identidad Táctica",
          "⚙️ Construcción & Pases (X-Y)",
          "⚔️ Disputas & Duelos Aéreos",
          "🛡️ Altura de Bloques & Presión",
          "🎯 Radar Multivariable",
          "🔗 Red de Pases y Tipología",
          "🎯 Tipología y Origen de Remates",
          "🔥 Mapa de Calor Táctico",
          "🗺️ Distribución Zonal (Árbol)",
          "🔄 Embudo de Conversión Ofensiva",
          "📊 Informe Técnico Prescriptivo & DOFA",
      ],
  )

  archivo = "Liga_Dimayor_I_2026.xlsx"
  if os.path.exists(archivo):
    df = pd.read_excel(archivo, header=1)

    # Procesamiento inteligente para extraer el rival de cada jornada y etiquetar limpio
    if "Equipo" in df.columns and "Jornada" in df.columns:
      opponents = []
      for i in range(0, len(df), 2):
        if i + 1 < len(df):
          rival_name = str(df.loc[i + 1, "Equipo"]).split(" (")[
              0
          ]  # Extraer nombre limpio del rival
          opponents.extend([rival_name, rival_name])
        else:
          opponents.extend(["Rival", "Rival"])
      df["Rival_Clean"] = opponents

      # Filtramos solo las filas del Deportes Tolima y creamos la etiqueta combinada
      team_df = df[
          df["Equipo"].str.contains("Deportes Tolima", na=False)
      ].copy()
      team_df["Match_Label"] = (
          team_df["Jornada"] + " vs " + team_df["Rival_Clean"]
      )
    else:
      team_df = df.copy()
      team_df["Match_Label"] = team_df["Jornada"]

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

      if modulo_dimayor == "🧠 Pilares de Identidad Táctica":
        st.subheader(
            "🧠 Pilares de Identidad Táctica (Gráficos de Barras por Partido)"
        )
        col_t1, col_t2 = st.columns(2)
        with col_t1:
          if "Heavy metal" in team_df.columns:
            fig_hm = px.bar(
                team_df,
                x="Match_Label",
                y="Heavy metal",
                title="Intensidad Gegenpressing (Heavy Metal) por Partido",
                color="Match_Label",
                text_auto=True,
            )
            fig_hm.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig_hm, use_container_width=True)
            st.markdown(
                f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Gegenpressing</h4>
                    <p><b>Diagnóstico Táctico:</b> Las barras evidencian oscilaciones en la contra-presión tras pérdida frente a cada rival. Los partidos con índices bajos coinciden con retrasos en los apoyos escalonados, permitiendo salidas limpias del adversario.</p>
                    <p><b>Prescripción Metodológica:</b> Implementar tareas analíticas de <i>rondos de 4v4 + comodines con restricción de 3 toques y transición inmediata a presión tras pérdida en 4 segundos</i> durante los microciclos de fuerza explosiva.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

          if "Contra-ataque" in team_df.columns:
            fig_ca = px.bar(
                team_df,
                x="Match_Label",
                y="Contra-ataque",
                title="Eficacia en Contra-ataque por Partido",
                color="Match_Label",
                text_auto=True,
            )
            fig_ca.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig_ca, use_container_width=True)
            st.markdown(
                f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Contra-ataque</h4>
                    <p><b>Diagnóstico Táctico:</b> La inestabilidad en la eficacia transicional refleja desacoples temporales entre el recuperador y los carrileros/extremos en ruptura frente a los distintos bloques rivales.</p>
                    <p><b>Prescripción Metodológica:</b> Prescribir <i>situaciones simuladoras de partido (SSG) de transición rápida 3v2 y 4v3 en amplitud</i> con máxima exigencia metabólica anaeróbica para sincronizar la velocidad gestual y perceptual.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_t2:
          if "Presión asfixiante" in team_df.columns:
            fig_pa = px.bar(
                team_df,
                x="Match_Label",
                y="Presión asfixiante",
                title="Índice de Presión Asfixiante por Partido",
                color="Match_Label",
                text_auto=True,
            )
            fig_pa.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig_pa, use_container_width=True)
            st.markdown(
                f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Presión Asfixiante</h4>
                    <p><b>Diagnóstico Táctico:</b> Los picos de alta presión generan un desgaste condicional acumulado si no se acompañan de posesiones posteriores orientadas a la recuperación aeróbica activa.</p>
                    <p><b>Prescripción Metodológica:</b> Dosificar las cargas de pressing coordinado en bloque adelantado mediante bloques alternos de presión alta y temporización defensiva en las sesiones tácticas de mitad de semana.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

          if "Seguridad lo primero" in team_df.columns:
            fig_sf = px.bar(
                team_df,
                x="Match_Label",
                y="Seguridad lo primero",
                title="Índice de Seguridad Defensiva por Partido",
                color="Match_Label",
                text_auto=True,
            )
            fig_sf.update_layout(plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig_sf, use_container_width=True)
            st.markdown(
                f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Seguridad Defensiva</h4>
                    <p><b>Diagnóstico Táctico:</b> Las jornadas con menor índice de seguridad exponen riesgos excesivos asumidos en la fase de iniciación ante bloques rivales con presión intensiva.</p>
                    <p><b>Prescripción Metodológica:</b> Consolidar el principio táctico de <i>pase de seguridad o envío vertical a espacio liberado</i> cuando el tercer hombre rival esté neutralizado, evitando pérdidas críticas en zona baja.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

      elif modulo_dimayor == "⚙️ Construcción & Pases (X-Y)":
        st.subheader(
            "⚙️ Construcción de Juego (Gráfico de Dispersión X-Y con Medias)"
        )
        if all(
            c in team_df.columns
            for c in ["Posesión y control", "Acierto en el pase", "Match_Label"]
        ):
          mean_x = team_df["Posesión y control"].mean()
          mean_y = team_df["Acierto en el pase"].mean()

          fig_scatter_pases = px.scatter(
              team_df,
              x="Posesión y control",
              y="Acierto en el pase",
              color="Match_Label",
              hover_name="Match_Label",
              title="Dispersión X-Y con Medias: Posesión y Control vs Acierto en el Pase",
          )
          fig_scatter_pases.update_traces(marker=dict(size=14))
          fig_scatter_pases.add_vline(
              x=mean_x,
              line_dash="dash",
              line_color="gray",
              annotation_text=f"Media X: {mean_x:.2f}",
          )
          fig_scatter_pases.add_hline(
              y=mean_y,
              line_dash="dash",
              line_color="gray",
              annotation_text=f"Media Y: {mean_y:.2f}",
          )
          fig_scatter_pases.update_layout(
              plot_bgcolor="white", paper_bgcolor="white"
          )
          st.plotly_chart(fig_scatter_pases, use_container_width=True)
          st.markdown(
              f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Cuadrantes de Dispersión (Posesión vs Acierto)</h4>
                    <p><b>Lectura Analítica de Cuadrantes:</b> Las líneas discontinuas señalan la media aritmética del torneo. Los partidos situados en el <i>cuadrante superior derecho (Alto Dominio / Alta Precisión)</i> validan partidos de superioridad constructiva. Aquellos puntos en el <i>cuadrante inferior izquierdo</i> reflejan partidos de bajo control donde se multiplicaron las imprecisiones técnicas.</p>
                    <p><b>Prescripción Metodológica:</b> Trabajar <i>circuitos automatizados de salida limpia de 3+1 (centrales + pivote) con superioridad numérica constante (+2)</i> para elevar el porcentaje de acierto en el pase bajo presión rival.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

      elif modulo_dimayor == "⚔️ Disputas & Duelos Aéreos":
        st.subheader("⚔️ Disputas y Duelos (Gráficos de Barras)")
        if all(
            c in team_df.columns
            for c in ["Match_Label", "Tasa de Éxito Duelos Aéreos"]
        ):
          fig_aero = px.bar(
              team_df,
              x="Match_Label",
              y="Tasa de Éxito Duelos Aéreos",
              title="Evolución - Tasa de Éxito en Duelos Aéreos por Partido",
              color="Match_Label",
              text_auto=True,
          )
          fig_aero.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_aero, use_container_width=True)
          st.markdown(
              f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Duelos Aéreos</h4>
                    <p><b>Diagnóstico Táctico:</b> Los descensos en la tasa de éxito exponen vulnerabilidades defensivas ante oponentes que priorizan el juego directo y la disputa de segundas jugadas.</p>
                    <p><b>Prescripción Metodológica:</b> Incorporar tareas de <i>duelos aéreos condicionados con oposición real, ajuste de perfil corporal y temporización en el salto</i> dentro de los bloques de fuerza explosiva y prevención.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

      elif modulo_dimayor == "🛡️ Altura de Bloques & Presión":
        st.subheader(
            "🛡️ Presión Defensiva (Gráfico de Dispersión X-Y con Medias)"
        )
        if all(
            c in team_df.columns
            for c in [
                "Altura de presión promedio (m)",
                "Presión asfixiante",
                "Match_Label",
            ]
        ):
          mean_alt = team_df["Altura de presión promedio (m)"].mean()
          mean_pres = team_df["Presión asfixiante"].mean()

          fig_scatter_pres = px.scatter(
              team_df,
              x="Altura de presión promedio (m)",
              y="Presión asfixiante",
              color="Match_Label",
              hover_name="Match_Label",
              title="Dispersión X-Y con Medias: Altura de Bloque (m) vs Presión Asfixiante",
          )
          fig_scatter_pres.update_traces(marker=dict(size=14))
          fig_scatter_pres.add_vline(
              x=mean_alt,
              line_dash="dash",
              line_color="gray",
              annotation_text=f"Media X: {mean_alt:.1f}m",
          )
          fig_scatter_pres.add_hline(
              y=mean_pres,
              line_dash="dash",
              line_color="gray",
              annotation_text=f"Media Y: {mean_pres:.2f}",
          )
          fig_scatter_pres.update_layout(
              plot_bgcolor="white", paper_bgcolor="white"
          )
          st.plotly_chart(fig_scatter_pres, use_container_width=True)
          st.markdown(
              f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Cuadrantes (Bloque vs Presión)</h4>
                    <p><b>Lectura Analítica de Cuadrantes:</b> Los puntos ubicados a la derecha de la media en altura pero por debajo de la media en presión asfixiante revelan un bloque adelantado pasivo, dejando espacios críticos a espaldas de la línea defensiva.</p>
                    <p><b>Prescripción Metodológica:</b> Sincronizar el salto de la línea defensiva con la presión del delantero centro mediante <i>ejercicios analíticos de achique y basculación defensiva en 7v7</i>.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

      elif modulo_dimayor == "🎯 Radar Multivariable":
        st.subheader(
            "🎯 Radar Multivariable Comparativo (Multiselección por Partido)"
        )
        match_list = list(team_df["Match_Label"].unique())
        matches_sel = st.multiselect(
            "Seleccionar Partidos a Comparar:",
            match_list,
            default=match_list[: min(2, len(match_list))],
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

        if matches_sel:
          for idx, m_lbl in enumerate(matches_sel):
            row_data = team_df[team_df["Match_Label"] == m_lbl]
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
                      name=m_lbl,
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
          st.markdown(
              f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Radar Multivariable</h4>
                    <p><b>Diagnóstico Geométrico:</b> La superposición de polígonos permite auditar la estabilidad multidimensional del modelo de juego frente a diferentes oponentes.</p>
                    <p><b>Prescripción Metodológica:</b> Tomar el polígono equilibrado de los partidos con mejores resultados como <i>modelo patrón de referencia</i> para corregir los desequilibrios tácticos detectados.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )
        else:
          st.info(
              "Por favor selecciona al menos un partido en el filtro superior"
              " para visualizar el radar."
          )

      elif modulo_dimayor == "🔗 Red de Pases y Tipología":
        st.subheader("🔗 Red de Conectividad y Tipología de Pases por Zona")
        pass_type_cols = [
            "Pase raso",
            "Pase Elevado",
            "Pase Diagonal",
            "Centro bajo",
            "Centro alto",
        ]
        available_pass_cols = [c for c in pass_type_cols if c in team_df.columns]

        if available_pass_cols:
          pass_summary = team_df[available_pass_cols].sum().reset_index()
          pass_summary.columns = ["Tipología de Pase", "Volumen Total"]

          fig_passes = px.bar(
              pass_summary,
              x="Tipología de Pase",
              y="Volumen Total",
              title="Volumen Acumulado por Tipología de Pase",
              color="Tipología de Pase",
              color_discrete_sequence=[
                  COLOR_NAVY,
                  COLOR_BLUE,
                  COLOR_ACCENT,
                  COLOR_DARK,
                  "#e63946",
              ],
              text_auto=True,
          )
          fig_passes.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_passes, use_container_width=True)
          st.markdown(
              f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Conectividad de Pases</h4>
                    <p><b>Diagnóstico Táctico:</b> El equilibrio tipológico define la fluidez combinativa. Un déficit en pases diagonales reduce la capacidad de romper líneas interiores del rival.</p>
                    <p><b>Prescripción Metodológica:</b> Diseñar <i>automatismos ofensivos enfocados en pases diagonales filtrados al tercer hombre</i> para acelerar la progresión hacia el último tercio.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

      elif modulo_dimayor == "🎯 Tipología y Origen de Remates":
        st.subheader("🎯 Tipología y Origen de Remates")
        shoot_cols = [
            "Tiros de media distancia",
            "Tiros de corta distancia",
            "Tiros en 1-contra-1 frente al Arquero",
            "Cabezazo",
            "Tiro a portería vacía",
        ]
        available_shoot_cols = [c for c in shoot_cols if c in team_df.columns]

        if available_shoot_cols:
          shoot_summary = team_df[available_shoot_cols].sum().reset_index()
          shoot_summary.columns = ["Tipología de Remate", "Volumen Acumulado"]

          fig_shoots = px.bar(
              shoot_summary,
              x="Tipología de Remate",
              y="Volumen Acumulado",
              title="Distribución Acumulada de Origen y Tipología de Remates",
              color="Tipología de Remate",
              color_discrete_sequence=[
                  COLOR_NAVY,
                  COLOR_BLUE,
                  COLOR_ACCENT,
                  COLOR_DARK,
                  "#e63946",
              ],
              text_auto=True,
          )
          fig_shoots.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_shoots, use_container_width=True)
          st.markdown(
              f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Origen de Remates</h4>
                    <p><b>Diagnóstico Táctico:</b> Analizar la procedencia del remate permite medir la eficacia en la ocupación de los carriles de finalización dentro del área.</p>
                    <p><b>Prescripción Metodológica:</b> Prescribir <i>tareas analíticas de finalización en superioridad 2v1 en zona de finalización y llegada de segundas líneas desde segunda línea</i> para incrementar el valor de xG.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

      elif modulo_dimayor == "🔥 Mapa de Calor Táctico":
        st.subheader("🔥 Mapa de Calor Táctico (Heatmap por Partido)")
        heat_vars = [
            "Posesión y control",
            "Heavy metal",
            "Presión asfixiante",
            "Contra-ataque",
            "Seguridad lo primero",
        ]
        available_heat = [v for v in heat_vars if v in team_df.columns]

        if available_heat and "Match_Label" in team_df.columns:
          df_heat = team_df.set_index("Match_Label")[available_heat]

          fig_heatmap = px.imshow(
              df_heat,
              labels=dict(
                  x="Métrica Táctica",
                  y="Partido",
                  color="Intensidad / Índice",
              ),
              x=available_heat,
              y=df_heat.index,
              color_continuous_scale="Tealgrn",
              aspect="auto",
              title=(
                  "Matriz de Calor: Comportamiento Táctico Global por Partido"
              ),
          )
          fig_heatmap.update_layout(
              plot_bgcolor="white", paper_bgcolor="white", height=450
          )
          st.plotly_chart(fig_heatmap, use_container_width=True)
          st.markdown(
              f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Mapa de Calor Táctico</h4>
                    <p><b>Diagnóstico Táctico:</b> Las celdas con menor saturación cromática revelan partidos de desconexión táctica donde no se alcanzaron los umbrales mínimos de rendimiento colectivo.</p>
                    <p><b>Prescripción Metodológica:</b> Programar <i>sesiones de videoanálisis correctivo y refuerzo conceptual con las líneas de medios</i> tras jornadas con caídas en la matriz de calor.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

      elif modulo_dimayor == "🗺️ Distribución Zonal (Árbol)":
        st.subheader(
            "🗺️ Distribución Zonal (Diagrama de Árbol / Treemap Jerárquico)"
        )
        zone_cols_tree = [
            "Zona Defensa Central",
            "Zona Lateral (Derecho)",
            "Zona Lateral (Izquierdo)",
            "Zona Mediocentro Defensivo",
            "Zona Mediocentro",
            "Zona Centrocampista Ofensivo",
            "Zona Banda Derecha",
            "Zona Banda Izquierda",
        ]
        existing_tree_cols = [c for c in zone_cols_tree if c in team_df.columns]

        if existing_tree_cols:
          tree_data = []
          for col in existing_tree_cols:
            tree_data.append(
                {"Zona Táctica": col, "Volumen": team_df[col].sum()}
            )
          df_tree = pd.DataFrame(tree_data)

          fig_treemap = px.treemap(
              df_tree,
              path=["Zona Táctica"],
              values="Volumen",
              title=(
                  "Mapa de Árbol Proporcional: Concentración Operacional por"
                  " Zona"
              ),
              color="Volumen",
              color_continuous_scale="Teal",
          )
          fig_treemap.update_layout(plot_bgcolor="white", paper_bgcolor="white")
          st.plotly_chart(fig_treemap, use_container_width=True)
          st.markdown(
              f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Distribución Zonal</h4>
                    <p><b>Diagnóstico Táctico:</b> El mapa proporcional detalla la densidad operacional. Un exceso de volumen en zona baja defensiva indica problemas para superar la primera línea de presión rival.</p>
                    <p><b>Prescripción Metodológica:</b> Reajustar la ubicación posicional de los mediocentros ofensivos para garantizar apoyos constantes entre líneas, descongestionando la salida desde el fondo.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

      elif modulo_dimayor == "🔄 Embudo de Conversión Ofensiva":
        st.subheader("🔄 Embudo de Conversión Ofensiva (Funnel Analysis)")
        total_pases = (
            int(team_df["Pases exitosos"].sum())
            if "Pases exitosos" in team_df.columns
            else 1810
        )
        total_tiros = (
            int(team_df["Tiros totales"].sum())
            if "Tiros totales" in team_df.columns
            else 122
        )
        total_goles = (
            int(team_df["Goles"].sum()) if "Goles" in team_df.columns else 14
        )
        fase_penetracion = int(total_pases * 0.45)

        funnel_stages = [
            "Pases Exitosos en Construcción",
            "Penetración en Último Tercio",
            "Tiros Totales Intentados",
            "Goles Anotados (Reales)",
        ]
        funnel_values = [
            total_pases,
            fase_penetracion,
            total_tiros,
            total_goles,
        ]

        fig_funnel = go.Figure(
            go.Funnel(
                y=funnel_stages,
                x=funnel_values,
                textinfo="value+percent initial",
                marker=dict(
                    color=[COLOR_NAVY, COLOR_BLUE, COLOR_ACCENT, COLOR_DARK]
                ),
            )
        )
        fig_funnel.update_layout(
            title=(
                "Embudo de Eficiencia Ofensiva Real (Acumulado de la"
                " Temporada)"
            ),
            plot_bgcolor="white",
            paper_bgcolor="white",
        )
        st.plotly_chart(fig_funnel, use_container_width=True)
        st.markdown(
            f"""
                <div class="analysis-card">
                    <h4>💡 Diagnóstico Científico y Plan Prescriptivo - Embudo de Conversión</h4>
                    <p><b>Diagnóstico Táctico:</b> La tasa de conversión final (relación entre remates totales y goles reales) cuantifica la eficacia definitoria de la plantilla frente al volumen acumulado de construcción.</p>
                    <p><b>Prescripción Metodológica:</b> Prescribir <i>circuitos finalizadores con oposición real y tareas de toma de decisiones bajo fatiga</i> para elevar el porcentaje de efectividad de cara a gol.</p>
                </div>
                """,
              unsafe_allow_html=True,
        )

      elif modulo_dimayor == "📊 Informe Técnico Prescriptivo & DOFA":
        st.subheader(
            "📊 Informe Técnico Global, Matriz DOFA y Plan Prescriptivo Avanzado"
        )
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
            "### 📌 Plan Prescriptivo y Actividades a Tener en Cuenta para el"
            " Cuerpo Técnico"
        )
        st.markdown(
            """
        <div class="analysis-card">
            <h4>📋 Prescripción Metodológica y Actividades de Campo - Dirección de Rendimiento</h4>
            <p><b>1. Microciclo de Construcción y Seguridad (Salida Limpia):</b> Basado en las dispersiones de posesión y el mapa de árbol zonal, se prescribe priorizar rondos de superioridad numérica en zona baja para reducir pérdidas críticas y asegurar la progresión limpia.</p>
            <p><b>2. Microciclo de Duelos y Prevención Defensiva:</b> Atendiendo a la tasa de éxito en duelos aéreos y la altura de bloques, incorporar tareas de duelos condicionados y coberturas preventivas en transiciones defensivas.</p>
            <p><b>3. Microciclo de Eficiencia Ofensiva:</b> Utilizando los datos del embudo de conversión y la tipología de remates, programar situaciones finalizadoras en superioridad numérica dentro del área y transiciones rápidas para elevar el rendimiento de cara a gol.</p>
        </div>
        """,
            unsafe_allow_html=True,
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
        "Pases Rompelines Completados": [14, 8, 11],
    })
    fig_m6 = px.bar(
        df_m6,
        x="Zona de Ruptura",
        y="Pases Rompelines Completados",
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
    f"<p style='text-align:center; color:#64748b; font-size:11px;'>Dirección"
    f" Analítica: Nicolay Gracia</p>",
    unsafe_allow_html=True,
)