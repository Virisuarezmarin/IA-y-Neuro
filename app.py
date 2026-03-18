import streamlit as st

# ---------------- CONFIGURACIÓN GENERAL ----------------
st.set_page_config(page_title="Neurología e IA", layout="wide")

# ---------------- TÍTULO Y FRASE ----------------
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
    st.write("""
La medicina moderna se encuentra en un punto de inflexión. Imagine un escenario donde un reloj inteligente o una cámara de alta resolución puedan detectar los primeros signos de una enfermedad neurodegenerativa años antes de que aparezcan los síntomas evidentes. Esta no es una escena de ciencia ficción, sino el resultado de la convergencia entre la Inteligencia Artificial (IA) y las neurotecnologías.

Sin embargo, a medida que nuestras máquinas se vuelven más inteligentes para leer nuestro cerebro, surgen preguntas fundamentales: ¿Cómo protegemos nuestra privacidad mental? ¿Cómo garantizamos que estos algoritmos sean justos?

Este artículo explora cómo el aprendizaje automático y la ética se han unido para transformar el diagnóstico del Alzheimer y el Parkinson, basándose en una sólida estructura de investigación científica.
""")

elif seleccion == "1. Más allá de los números":
    st.header("1. Más allá de los números: Una ética con los pies en la tierra")
    st.write("""
Tradicionalmente, la ética en la tecnología se ha manejado mediante grandes principios abstractos, como "haz el bien" o "sé justo". No obstante, la realidad de los hospitales y los pacientes es mucho más compleja.

Por ello, expertos como Resseguier y Rodrigues (2021) proponen un cambio de visión: pasar de una ética teórica a una "ética como atención al contexto".

### El problema de la Caja Negra
El motor de este avance es el Aprendizaje Automático (machine learning), un sistema que permite a las computadoras aprender patrones a partir de datos masivos. El reto es que muchas veces estos sistemas funcionan como una "caja negra": sabemos qué resultado arrojan, pero no exactamente cómo llegaron a él.

Si no prestamos atención al contexto social, corremos el riesgo de que los algoritmos hereden prejuicios o ignoren las desigualdades de la vida real.

### Neuroética e IA: Una alianza necesaria
Cuando hablamos de enfermedades del cerebro, la ética de los datos se mezcla con la neuroética, que estudia las implicaciones de intervenir en la mente humana.

Esta unión permite entender mejor quiénes somos como seres humanos para crear reglas que realmente nos protejan. Incluso las grandes empresas tecnológicas pueden aportar experiencia para implementar ética en sistemas reales.
""")

elif seleccion == "2. Detectando el Alzheimer":
    st.header("2. Detectando el Alzheimer antes de que se pierdan los recuerdos")
    st.write("""
La enfermedad de Alzheimer es la causa más común de demencia en el mundo. Detectarla a tiempo es como intentar encontrar una aguja en un pajar de datos clínicos.

### Los ojos digitales de la medicina
Las Redes Neuronales Convolucionales (CNN) son ideales para analizar imágenes médicas. Investigaciones han logrado niveles de precisión del 98.67% en el diagnóstico temprano utilizando resonancias magnéticas.

### La marcha como espejo del cerebro
El cerebro también se "lee" en cómo nos movemos. La forma de caminar se convierte en un biomarcador digital.

Analizando la marcha junto con pruebas cognitivas, se puede predecir con gran exactitud quién podría desarrollar demencia.
""")

elif seleccion == "3. El Parkinson bajo la lupa":
    st.header("3. El Parkinson bajo la lupa de los algoritmos")
    st.write("""
El Parkinson es una enfermedad compleja y subjetiva. El aprendizaje automático permite una medición objetiva.

### Clasificación por estadios
Los modelos de IA pueden distinguir entre personas sanas y pacientes en diferentes fases analizando parámetros de sus pasos.

### Los cinco pilares del movimiento
- Velocidad media del paso  
- Longitud del paso  
- Variabilidad de la longitud  
- Ancho del paso  
- Variabilidad del ancho  

### Tecnología wearable
Gracias a sensores portátiles, el monitoreo puede ser continuo.

La IA puede detectar automáticamente cuándo la medicación está funcionando (On) y cuándo no (Off), permitiendo tratamientos personalizados.
""")

elif seleccion == "4. Neurología Digital":
    st.header("4. Hacia una Neurología Digital y Humana")
    st.write("""
La Neurología Digital busca una armonía entre tecnología y responsabilidad.

### Una visión integral
- Lo estructural: imágenes cerebrales analizadas por IA  
- Lo funcional: análisis de la marcha  

Esta visión permite detección temprana y precisa.

Sin embargo, es fundamental evitar que el monitoreo constante se convierta en vigilancia invasiva, asegurando un uso ético y equitativo.
""")

elif seleccion == "Conclusión":
    st.header("Conclusión")
    st.write("""
La inteligencia artificial tiene el potencial de devolvernos tiempo y calidad de vida frente a enfermedades neurodegenerativas.

El éxito real no se medirá solo por la precisión, sino por su capacidad para integrarse en un sistema que priorice la transparencia, la equidad y la dignidad humana.

Como sociedad, el reto es asegurar que, mientras las máquinas aprenden a diagnosticarnos, nosotros no olvidemos la importancia de cuidar el contexto humano que nos rodea.
""")

# ---------------- REFERENCIAS INTERACTIVAS ----------------
elif seleccion == "Referencias":
    st.header("Referencias")

    referencias = {
        "Rehman et al. (2019)": """Resumen: Estudio que usa machine learning para seleccionar las características de la marcha más relevantes y clínicamente interpretables para clasificar Parkinson temprano (PD) vs. controles sanos (HC), logrando alta precisión con solo 5 variables de marcha.""",

        "Aich et al. (2020)": """Resumen: Propone un algoritmo de machine learning supervisado para detectar automáticamente los estados "On" y "Off" en pacientes con Parkinson usando señales de marcha capturadas por acelerómetros.""",

        "Salles & Farisco (2024)": """Resumen: Argumenta que la convergencia entre neurociencia y IA requiere colaboración estrecha entre neuroética y ética de la IA para abordar mejor cuestiones éticas compartidas.""",

        "Tuena et al. (2024)": """Resumen: Estudio que usa machine learning para evaluar el poder predictivo de alteraciones en la marcha y medidas cognitivas en la progresión a Alzheimer.""",

        "Ferreira et al. (2022)": """Resumen: Modelos de machine learning para detección y clasificación de Parkinson basados en parámetros de la marcha.""",

        "Resseguier & Rodrigues (2021)": """Resumen: Propone un enfoque de ética como atención al contexto para hacer la ética de IA más práctica y sensible a entornos reales."""
    }

    ref_seleccion = st.selectbox("Selecciona una referencia", list(referencias.keys()))
    st.write(referencias[ref_seleccion])
