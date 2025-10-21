# hub_app/hub_app.py

import streamlit as st
from streamlit_card import card

st.set_page_config(
    page_title="Portafolio de Proyectos de IA - John",
    page_icon="🤖",
    layout="wide"
)

# --- Título y Descripción del Hub ---
st.title("🤖 Portafolio de Proyectos de IA")
st.markdown("### Por John A. Scripter") # Puedes cambiar esto por tu nombre real
st.markdown("""
Bienvenido a mi centro de aplicaciones de Inteligencia Artificial. Cada herramienta ha sido diseñada para resolver problemas específicos del mundo real, desde el análisis de medios hasta la transcripción de audio y la automatización de procesos de datos (ETL).
""")
st.write("---")

# --- Datos de los Proyectos ---
# Define cada proyecto aquí. Para las imágenes, puedes usar los enlaces que he puesto
# o subirlas a un servicio como imgur.com o al propio repositorio de GitHub.
PROYECTOS = [
    {
        "titulo": "📰 Sistema de Análisis de Noticias con IA",
        "descripcion": "Una potente aplicación que combina reglas heurísticas y LLMs para analizar dossieres de noticias. Realiza clasificación, resumen y análisis de sentimiento de forma automatizada.",
        "url": "https://api-hibrid-tono-tema.streamlit.app/",
        "imagen": "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80",
        "tags": ["PNL", "LLM", "OpenAI", "Análisis de Medios", "Streamlit"]
    },
    {
        "titulo": "🎧 Transcriptor Pro - Johnascriptor",
        "descripcion": "Análisis y transcripción de audio a velocidades récord utilizando la API de Groq. Ideal para convertir reuniones, entrevistas o cualquier archivo de audio en texto estructurado y analizable.",
        "url": "https://johnascriber.streamlit.app/",
        "imagen": "https://images.unsplash.com/photo-1590602847923-45c1363a233c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80",
        "tags": ["Transcripción de Audio", "Groq API", "Whisper", "PNL", "Streamlit"]
    },
    {
        "titulo": "✅ Herramienta de Clasificación - JohnAdmin",
        "descripcion": "Una solución ágil y segura para la clasificación inmediata de noticias desde un archivo Excel. Diseñada para eliminar demoras y cuellos de botella en flujos de trabajo editoriales.",
        "url": "https://johnadmin.streamlit.app/", # Asumí esta URL, ¡ajústala si es diferente!
        "imagen": "https://images.unsplash.com/photo-1516321497487-e288fb19713f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80",
        "tags": ["Clasificación", "Productividad", "Excel", "Gestión de Datos", "Streamlit"]
    },
    {
        "titulo": "🚗 Herramienta ETL para Nissan",
        "descripcion": "Una aplicación especializada para procesos de Extracción, Transformación y Carga (ETL) de datos. Automatiza y simplifica la manipulación de datos para análisis específicos de negocio.",
        "url": "https://nissan3-mu89mzqbp64tduunjbgdhx.streamlit.app/",
        "imagen": "https://images.unsplash.com/photo-1553440569-e3d8e5e1e15e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=774&q=80",
        "tags": ["ETL", "Automatización", "Pandas", "Análisis de Datos", "Streamlit"]
    },
]

# --- Renderizar las Tarjetas de Proyectos ---
# Dividimos en filas de 2 para un mejor aspecto visual en pantallas anchas
num_proyectos = len(PROYECTOS)
columnas_por_fila = 2

for i in range(0, num_proyectos, columnas_por_fila):
    # Selecciona los proyectos para la fila actual
    proyectos_fila = PROYECTOS[i:i+columnas_por_fila]
    
    # Crea las columnas para esta fila
    cols = st.columns(columnas_por_fila)
    
    for j, proyecto in enumerate(proyectos_fila):
        with cols[j]:
            # El componente card es clickeable en su totalidad
            has_clicked = card(
                title=proyecto["titulo"],
                text=proyecto["descripcion"],
                image=proyecto["imagen"],
                url=proyecto["url"],
                on_click=lambda: None, # Placeholder para la funcionalidad de click
                styles={
                    "card": {
                        "width": "100%",  # La tarjeta ocupa todo el ancho de la columna
                        "height": "450px",
                        "margin": "10px",
                        "box-shadow": "0 4px 8px 0 rgba(0,0,0,0.2)",
                        "transition": "0.3s"
                    },
                    "filter": {
                        "background-color": "rgba(0, 0, 0, 0.4)"  # Oscurece la imagen para que el texto resalte
                    },
                    "text": {
                        "font-family": "sans-serif",
                    }
                }
            )
            # Añadimos los tags debajo de la tarjeta para mayor claridad
            tags_html = " ".join([f"<span style='background-color: #2a3a57; color: white; padding: 4px 8px; border-radius: 12px; margin: 2px; display: inline-block; font-size: 0.8em;'>{tag}</span>" for tag in proyecto["tags"]])
            st.markdown(f"<div style='padding-left: 15px;'>{tags_html}</div>", unsafe_allow_html=True)


st.write("---")
st.markdown("Creado por Johanthan Cortés 🤖 usando [Streamlit](https://streamlit.io).")
