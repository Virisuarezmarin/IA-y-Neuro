import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Neurología e IA", layout="wide")

# ---------------- HEADER ----------------
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    <h1 style='text-align: center; font-size: 40px;'>
    El Algoritmo del Olvido y el Paso del Tiempo:
    <br>Cómo la IA y la Ética Redefinen la Neurología
    </h1>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='text-align: right; font-size:18px; font-style: italic; margin-top:40px;'>
    Como sociedad, el reto es asegurar que, mientras las máquinas aprenden a diagnosticarnos,
    nosotros no olvidemos la importancia de cuidar el contexto humano que nos rodea.
    </div>
    """, unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navegación")

secciones = [
    "Introducción",
    "1. Más allá de los números",
    "2. Detectando el Alzheimer",
    "3. El Parkinson bajo la lupa",
    "4. Neurología Digital",
    "Conclusión",
    "Referencias"
]

seleccion = st.sidebar.selectbox("Selecciona una sección", secciones)

# ---------------- CONTENIDO ----------------

if seleccion == "Introducción":
    st.header("Introducción")
    st.write("""La medicina moderna se encuentra en un punto de inflexión...
    (mantén aquí TODO tu texto completo original sin recortar)""")

elif seleccion == "1. Más allá de los números":
    st.header("1. Más allá de los números")
    st.write("""(contenido completo aquí)""")

elif seleccion == "2. Detectando el Alzheimer":
    st.header("2. Detectando el Alzheimer")
    st.write("""(contenido completo aquí)""")

elif seleccion == "3. El Parkinson bajo la lupa":
    st.header("3. El Parkinson bajo la lupa")
    st.write("""(contenido completo aquí)""")

elif seleccion == "4. Neurología Digital":
    st.header("4. Neurología Digital")
    st.write("""(contenido completo aquí)""")

elif seleccion == "Conclusión":
    st.header("Conclusión")
    st.write("""(contenido completo aquí)""")

# ---------------- REFERENCIAS CON BOTONES ----------------
elif seleccion == "Referencias":
    st.header("Referencias")

    # 🔍 BUSCADOR
    busqueda = st.text_input("🔍 Buscar referencia (autor, año, tema):")

    # 📚 DICCIONARIO COMPLETO
    referencias = {
        "Rehman et al. (2019)": """Rehman, R. Z. U., Del Din, S., Guan, Y., Yarnall, A. J., Shi, J. Q., & Rochester, L. (2019)...
Resumen: Estudio que usa machine learning...""",

        "Aich et al. (2020)": """Aich, S., Youn, J., Chakraborty, S...
Resumen: Propone un algoritmo...""",

        "Salles & Farisco (2024)": """Salles, A., & Farisco, M. (2024)...
Resumen: Argumenta que la convergencia...""",

        "Tuena et al. (2024)": """Tuena, C., Pupillo, C...
Resumen: Estudio retrospectivo...""",

        "Ferreira et al. (2022)": """Ferreira, M. I. A. S. N...
Resumen: Machine learning para Parkinson...""",

        "Farisco et al. (2022)": """Farisco, M., Salles, A...
Resumen: Neuroética y regulación IA...""",

        "Serafimovska et al. (2025)": """Serafimovska A...
Resumen: Punto de inflexión IA...""",

        "Resseguier & Rodrigues (2021)": """Resseguier, A...
Resumen: Ética contextual...""",

        "Javid & Feghhi (2021)": """Javid, S. A...
Resumen: Deep learning Alzheimer...""",

        "Hurley et al. (2024)": """Hurley, M...
Resumen: Riesgos éticos...""",

        "Ramos (2024)": """Ramos, R...
Resumen: Neurociberética...""",

        "Lavazza & Giorgi (2023)": """Lavazza, A...
Resumen: Integridad mental...""",

        "Berger & Rossi (2022)": """Berger, S. E...
Resumen: Ética en empresas...""",

        "Ahluwalia (2021)": """Ahluwalia, M...
Resumen: Gobernanza datos cerebrales...""",

        "Cazzolli et al. (2025)": """Cazzolli, C...
Resumen: Predicción demencia...""",

        "Onciul et al. (2025)": """Onciul, R...
Resumen: IA y neurociencia...""",

        "Merlin et al. (2024)": """Merlin, M...
Resumen: Retos éticos...""",

        "Ligthart et al. (2023)": """Ligthart, S...
Resumen: Neurorights...""",

        "Botes et al. (2025)": """Botes, M...
Resumen: Consentimiento cognitivo...""",

        "McCulloch & Pitts (2022)": """McCulloch, W. S...
Resumen: Derechos humanos..."""
    }

    # 🔎 FILTRO
    referencias_filtradas = {
        k: v for k, v in referencias.items()
        if busqueda.lower() in k.lower() or busqueda.lower() in v.lower()
    }

    # 📌 BOTONES
    if "ref_seleccionada" not in st.session_state:
        st.session_state.ref_seleccionada = None

    st.subheader("Selecciona una referencia:")

    for ref in referencias_filtradas.keys():
        if st.button(ref):
            st.session_state.ref_seleccionada = ref

    # 📄 MOSTRAR CONTENIDO
    if st.session_state.ref_seleccionada:
        st.markdown("---")
        st.subheader(st.session_state.ref_seleccionada)
        st.text_area(
            "Contenido",
            referencias[st.session_state.ref_seleccionada],
            height=300
        )
