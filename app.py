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
       Rehman, R. Z. U., Del Din, S., Guan, Y., Yarnall, A. J., Shi, J. Q., & Rochester, L. (2019). Selecting clinically relevant gait characteristics for classification of early Parkinson’s Disease: A comprehensive machine learning approach. Scientific Reports, 9(1), 17269. https://doi.org/10.1038/s41598-019-53656-7 
Resumen: Estudio que usa machine learning para seleccionar las características de la marcha más relevantes y clínicamente interpretables para clasificar Parkinson temprano (PD) vs. controles sanos (HC), logrando alta precisión con solo 5 variables de marcha.
Aich, S., Youn, J., Chakraborty, S., Pradhan, P. M., Park, J. H., Park, S., & Park, J. (2020). A supervised machine learning approach to detect the On/Off state in Parkinson’s disease using wearable based gait signals. Diagnostics, 10(7), 421. https://doi.org/10.3390/diagnostics10070421
Resumen: Propone un algoritmo de machine learning supervisado para detectar automáticamente los estados "On" (medicación efectiva) y "Off" (medicación inefectiva) en pacientes con Parkinson (PD) usando señales de marcha capturadas por acelerómetros en rodilla. Logra alta precisión objetiva frente a diarios subjetivos de pacientes.
Salles, A., & Farisco, M. (2024). Neuroethics and AI ethics: a proposal for collaboration. BMC Neuroscience, 25(1), 41. https://doi.org/10.1186/s12868-024-00888-7
Resumen: Argumenta que la creciente convergencia entre neurociencia y IA (e.g., AI en investigación cerebral, BCI, organoides cerebrales, neurotech asistida por IA) requiere colaboración estrecha entre neuroética y ética de la IA para abordar mejor cuestiones éticas compartidas (privacidad, autonomía, sesgos, conciencia, gobernanza). Los enfoques aislados son limitados; la cross-fertilization mejora reflexión conceptual, sensibilidad cultural y regulación integrada.
Tuena, C., Pupillo, C., Stramba-Badiale, C., Stramba-Badiale, M., & Riva, G. (2024). Predictive power of gait and gait-related cognitive measures in amnestic mild cognitive impairment: a machine learning analysis. Frontiers in Human Neuroscience, 17, 1328713. https://doi.org/10.3389/fnhum.2023.1328713
Resumen: Estudio retrospectivo que usa machine learning para evaluar el poder predictivo de alteraciones en la marcha (clasificadas visualmente como normal/anormal) y medidas cognitivas relacionadas (MMSE, DSST, TMT-B) en la conversión de mild cognitive impairment amnésico (aMCI) a Alzheimer (AD) en 36 meses. Integra biomarcadores motores y cognitivos para mejorar detección temprana de progresión.
Ferreira, M. I. A. S. N., Barbieri, F. A., Moreno, V. C., Penedo, T., & Tavares, J. M. R. S. (2022). Machine learning models for Parkinson’s disease detection and stage classification based on spatial-temporal gait parameters. Gait & Posture, 98, 49-55. https://doi.org/10.1016/j.gaitpost.2022.08.01
Resumen: Desde la perspectiva de una gran empresa tech (IBM), se analizan lecciones aprendidas en la implementación práctica de ética en IA para acelerar la traducción de principios neuroéticos a prácticas escalables en neurotecnologías (neurotech) y neurodatos, evitando "ethics washing" y promoviendo gobernanza responsable en un sector dominado por el privado.
Farisco, M., Salles, A., & Evers, K. (2022). On the contribution of neuroethics to the ethics and regulation of artificial intelligence. Neuroethics, 15(1), 4. https://doi.org/10.1007/s12152-022-09484-0
Resumen: Las guías éticas de IA actuales (e.g., EU, OECD) son abstractas y centradas en principios aplicados (transparencia, accountability), pero descuidan cuestiones fundamentales como inteligencia, conciencia y estatus ontológico humano. El artículo propone que la neuroética (especialmente su enfoque "fundamental") contribuya con análisis conceptual profundo y metodologías interdisciplinarias para enriquecer la ética y regulación de IA, evitando malentendidos y mejorando la acción práctica.
Serafimovska A, Challinor KL, Florio T. (2025). The AI inflection point in clinical neuropsychology: a call to action. J Clin Exp Neuropsycholy. 47(6):594-600. doi: 10.1080/13803395.2025.2561162 
Resumen: Comentario/perspectiva que identifica un "punto de inflexión" en la neuropsicología clínica por el rápido avance de la IA (e.g., automatización de evaluaciones cognitivas, detección temprana de demencia vía speech/imaging). Discute miedos comunes (pérdida de juicio clínico, erosión de la profesión) vs. riesgos reales (seguridad, privacidad, sesgos diagnósticos, falta de transparencia). Propone un marco crítico para integración responsable de IA, enfatizando innovación ética, validación rigurosa y acción proactiva de la disciplina para liderar el cambio en lugar de resistirlo.
Resseguier, A., & Rodrigues, R. (2021). Ethics as attention to context: recommendations for the ethics of artificial intelligence. Open Research Europe, 1(27). https://doi.org/10.12688/openreseurope.13260.2
Resumen: El artículo critica que las guías éticas actuales de IA se centran excesivamente en principios abstractos (transparencia, justicia, etc.) y descuidan el contexto específico de aplicación. Propone un enfoque de "ética como atención al contexto" para hacer la ética de IA más práctica, actionable y sensible a dominios reales (e.g., salud, justicia, empleo).
Javid, S. A., & Feghhi, M. M. (2021). Early diagnosis of Alzheimer's disease from MRI images with deep learning model. IEEE Access, 9, 90319-90329.
Resumen: Propone un modelo de deep learning (basado en redes convolucionales) para diagnóstico temprano de Alzheimer (AD) a partir de imágenes de resonancia magnética (MRI) cerebral. Enfocado en clasificación binaria/multi-clase (e.g., Normal vs. AD o etapas MCI/AD) usando datasets estándar; logra alta precisión como herramienta auxiliar no invasiva para detección precoz, cuando no hay cura efectiva.
Hurley, M., Sonig, A., Herrington, J., Storch, E. A., Lázaro-Muñoz, G., Blumenthal-Barby, J., & Kostick-Quenet, K. (2024). Ethical considerations for integrating multimodal computer perception and neurotechnology. Frontiers in Human Neuroscience, 18. https://doi.org/10.3389/fnhum.2024.1332451
Resumen: Estudio cualitativo que explora preocupaciones éticas de stakeholders sobre la integración de computer perception (CP: IA para inferir estados emocionales/comportamentales a partir de datos pasivos como wearables, voz, video) con neurotecnologías (EEG, fMRI, DBS). Destaca riesgos de invasividad, privacidad mental, seguridad de datos y conciencia limitada/ansiedad excesiva, proponiendo que la combinación agrava dilemas de neurorights y requiere safeguards éticos.
Ramos, R. (2024). Neurociberética, un nuevo y pertinente enfoque de la neuroética. Gaceta Medica de Mexico, 160(5), 480–485. https://doi.org/10.24875/GMM.M24000947
Resumen: Propone la neurociberética (neurocyberethics) como un enfoque emergente y necesario dentro de la neuroética, para abordar los desafíos éticos derivados de la convergencia entre neurociencia, cibernética, IA y neurotecnologías (e.g., neuroimágenes funcionales, interfaces cerebro-computadora, big data neural). Argumenta que la ética neurocientífica ha evolucionado y requiere atención más específica a riesgos cibernéticos/digitales, como privacidad de datos cerebrales, manipulación cognitiva y gobernanza de tecnologías híbridas humano-máquina.
Lavazza, A., & Giorgi, R. (2023). Philosophical foundation of the right to mental integrity in the age of neurotechnologies. Neuroethics, 16(10). https://doi.org/10.1007/s12152-023-09517-2
Resumen: Propone una fundamentación filosófica para un derecho específico a la integridad mental (mental integrity), que integra privacidad mental y no interferencia en la mente/cerebro. Ante neurotecnologías (EEG, fMRI, BCI como Neuralink) que leen/decodifican/modifican actividad mental, argumenta que estas amenazan rasgos únicos de la mente (intencionalidad, perspectiva de primera persona, autonomía moral, identidad narrativa), justificando un derecho moral (precedente a legal) más allá de la privacidad general.
Berger, S. E., & Rossi, F. (2022). Addressing neuroethics issues in practice: Lessons learnt by tech companies in AI ethics. Neuron, 110(11), 1735–1738. https://doi.org/10.1016/j.neuron.2022.05.006
Resumen: Desde la perspectiva de una gran empresa tech (IBM), se analizan lecciones aprendidas en la implementación práctica de ética en IA para acelerar la traducción de principios neuroéticos a prácticas escalables en neurotecnologías (neurotech) y neurodatos, evitando "ethics washing" y promoviendo gobernanza responsable en un sector dominado por el privado.
Ahluwalia, M. (2021). Legal Governance of Brain Data Derived from Artificial Intelligence. VOICES IN BIOETHICS, 7. https://doi.org/https://doi.org/10.52214/vib.v7i.8403
Resumen: El artículo examina los riesgos éticos y de privacidad del "big brain data" generado por IA y machine learning en neurociencia (e.g., decodificación de patrones cerebrales, pensamientos). Argumenta que los consentimientos actuales son insuficientes y propone gobernanza legal urgente para proteger privacidad, autonomía y prevenir brechas de datos.
Cazzolli, C., Chierici, M., Dallabona, M., Guella, C., & Jurman, G. (2025). Neuropsychological tests and machine learning: identifying predictors of MCI and dementia progression. Aging Clinical and Experimental Research, 37(79). https://doi.org/10.1007/s40520-025-02962-4
Resumen: Estudio observacional que usa machine learning (Random Forest) para identificar las pruebas neuropsicológicas más informativas en la predicción de diagnóstico (MCI vs. demencia) y progresión cognitiva en pacientes mayores. Con 281 pacientes (148 MCI, 133 demencia) y validación externa, destaca pruebas como MMSE, FAB, BSRT, AM y VSF como predictores clave, logrando ~73% accuracy promedio en clasificación diagnóstica. Propone priorizar tests informativos para reducir tiempo de evaluación y sesgos clínicos.
Onciul, R., Tataru, C., Dumitru, A., Crivoi, C., Serban, M., Covache-Busuioc, R., Radoi, M., & Toader, C. (2025). Artificial Intelligence and Neuroscience: Transformative Synergies in Brain Research and Clinical Applications. In Journal of Clinical Medicine (Vol. 14, Issue 2). Multidisciplinary Digital Publishing Institute (MDPI). https://doi.org/10.3390/jcm14020550
Resumen: Revisión narrativa que explora la convergencia bidireccional entre IA y neurociencia: IA acelera análisis de datos neurales (neuroimágenes, señales EEG/fMRI, genómica) para diagnóstico temprano, tratamiento personalizado y BCIs en trastornos como Alzheimer, Parkinson, epilepsia, autismo y parálisis; mientras la neurociencia inspira arquitecturas AI más eficientes (neuromórficas, spiking networks). Enfatiza aplicaciones clínicas transformadoras pero destaca desafíos éticos/técnicos para una integración responsable.
Merlin, M., Siby, M., Abraham, R., Biji, D., Joseph, B., & Jyothi, K. (2024). Ethical Implications of AI in Neuroscience-Discussing the Challenges and Responsibilities of using AI in Brain Disease Research. International Research Journal on Advanced Engineering and Management, 02(12), 3600–3604. https://doi.org/10.47392/IRJAEM.2024.531
Resumen: Discute los avances de la IA en neurociencia para investigación de enfermedades cerebrales (diagnóstico, tratamiento, comprensión de trastornos neurales complejos), pero enfatiza los desafíos éticos asociados: privacidad de datos sensibles, sesgos algorítmicos, responsabilidad por decisiones AI y necesidad de equidad. Aboga por que investigadores, desarrolladores y legisladores prioricen el bienestar, precisión y justicia de los pacientes.

Ligthart, S., Ienca, M., Meynen, G., Molnar-Gabor, F., Andorno, R., Bublitz, C., Catley, P., Claydon, L., Douglas, T., Farahany, N., Fins, J. J., Goering, S., Haselager, P., Jotterand, F., Lavazza, A., McCay, A., Wajnerman Paz, A., Rainey, S., Ryberg, J., & Kellmeyer, P. (2023). Minding Rights: Mapping Ethical and Legal Foundations of ‘Neurorights.’ Cambridge Quarterly of Healthcare Ethics, 32(4), 461–481. https://doi.org/10.1017/S0963180123000245
Resumen: El artículo mapea las bases éticas y legales de los "neurorights" ante avances en neurotecnologías (e.g., lectura/manipulación cerebral). Enfocado en tres conceptos clave: integridad mental, privacidad mental y libertad cognitiva, como extensiones de derechos humanos existentes para proteger dignidad, autonomía y mente contra riesgos emergentes.
Botes, M., Labuschaigne, M., Casteleyn, C., Inkster, B., & Sheppard, M. (2025). Decoding the Brain, Respecting the Person: A Neuroethical Inquiry into Consent and Cognitive Liberty in South Africa. Neuroethics, 18(43). https://doi.org/10.1007/s12152-025-09615-3
Resumen: El paper examina los riesgos éticos y legales de neurotecnologías emergentes en Sudáfrica (clínicas, investigación, consumo) y critica los modelos de consentimiento informado occidentales individualistas por ser insuficientes en contextos culturalmente plurales. Propone un marco de consentimiento relacional basado en filosofía africana (Ubuntu) para proteger privacidad mental, libertad cognitiva y datos neurales, abogando por neurorights sui generis y gobernanza inclusiva/decolonial.
McCulloch, W. S., & Pitts, W. (2022). A human rights-based approach por governing neurotchnologies. In P. Kellmeyer. O. Mueller. W. B. S. Voeneky. (Ed.), The Cambridge Handbook of Responsible Artificial Intelligence (Vol. 5, Issue 4, pp. 412–426). Cambridge University Press. https://doi.org/https://doi.org/10.1017/9781009207898.032
Resumen: El capítulo analiza la protección de la privacidad mental y la integridad mental frente a neurotecnologías basadas en IA (como interfaces cerebro-computadora). Propone un enfoque basado en derechos humanos existentes para gobernar estas tecnologías, enfatizando la necesidad de hacerlos accionables y justiciables.
"""
    }

    ref_seleccion = st.selectbox("Selecciona una referencia", list(referencias.keys()))
    st.write(referencias[ref_seleccion])
