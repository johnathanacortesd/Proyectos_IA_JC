# hub_app/hub_app.py

import streamlit as st
from streamlit_card import card # Necesitarás instalar streamlit-card

st.set_page_config(
    page_title="Hub de Proyectos de IA",
    page_icon="🧠",
    layout="wide"
)

# --- Título y Descripción del Hub ---
st.title("🧠 Mi Hub de Proyectos de IA")
st.markdown("""
Bienvenido a mi portafolio de herramientas y cuadernos de Inteligencia Artificial.
Aquí encontrarás una colección de aplicaciones interactivas y análisis detallados.
¡Explora, experimenta y no dudes en contactarme!
""")

# --- Datos de los Proyectos ---
# Aquí es donde defines cada proyecto. Añade un nuevo diccionario a esta lista para cada nuevo proyecto.
PROYECTOS = [
    {
        "titulo": "📊 Analizador de Tono y Tema",
        "descripcion": "Una aplicación web para analizar el sentimiento y clasificar por temas textos extraídos de archivos Excel. Ideal para analizar comentarios de clientes, encuestas o redes sociales.",
        "tipo": "App de Streamlit",
        "url": "https://tu-nombre-de-app.streamlit.app", # <-- ¡REEMPLAZA ESTA URL!
        "imagen": "https://cdn-icons-png.flaticon.com/512/7165/7165511.png",
        "tags": ["PNL", "Análisis de Sentimiento", "Clasificación", "Streamlit"]
    },
    {
        "titulo": "🖼️ Clasificador de Imágenes (ResNet)",
        "descripcion": "Un cuaderno de Google Colab que utiliza un modelo pre-entrenado (ResNet50) para clasificar el contenido de imágenes. Incluye visualizaciones y explicaciones del proceso.",
        "tipo": "Cuaderno de Colab",
        "url": "https://colab.research.google.com/github/tu-usuario/mi-hub-de-proyectos/blob/main/proyecto_cuaderno_vision/analisis_imagenes.ipynb", # <-- ¡REEMPLAZA ESTA URL!
        "imagen": "https://cdn-icons-png.flaticon.com/512/1048/1048953.png",
        "tags": ["Visión por Computadora", "Deep Learning", "PyTorch", "Colab"]
    },
    {
        "titulo": "📈 Dashboard de Ventas Interactivo",
        "descripcion": "Una aplicación que visualiza datos de ventas desde un archivo CSV, permitiendo filtrar por fecha, producto y región para un análisis dinámico.",
        "tipo": "App de Streamlit",
        "url": "https://tu-otra-app.streamlit.app", # <-- ¡REEMPLAZA ESTA URL!
        "imagen": "https://cdn-icons-png.flaticon.com/512/138/138343.png",
        "tags": ["Visualización de Datos", "Pandas", "Streamlit", "Business Intelligence"]
    },
    # --- Añade más proyectos aquí ---
]


# --- Renderizar las Tarjetas de Proyectos ---
st.header("🚀 Aplicaciones Interactivas")
cols_apps = st.columns(3) # Crear 3 columnas para las apps
i = 0
for p in PROYECTOS:
    if p["tipo"] == "App de Streamlit":
        with cols_apps[i % 3]:
            card(
                title=p["titulo"],
                text=p["descripcion"],
                image=p["imagen"],
                url=p["url"],
                styles={
                    "card": { "margin": "10px", "height": "400px" },
                    "text": { "font-family": "sans-serif" }
                }
            )
        i += 1

st.header("🔬 Cuadernos de Análisis en Colab")
cols_notebooks = st.columns(3) # Crear 3 columnas para los cuadernos
j = 0
for p in PROYECTOS:
    if p["tipo"] == "Cuaderno de Colab":
        with cols_notebooks[j % 3]:
            # Usamos un botón para el enlace "Abrir en Colab"
            st.image(p["imagen"], width=100)
            st.subheader(p["titulo"])
            st.write(p["descripcion"])
            st.markdown(f"**Tags:** `{'`, `'.join(p['tags'])}`")
            st.link_button("Abrir en Google Colab", p["url"])
        j += 1
