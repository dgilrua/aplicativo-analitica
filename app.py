import streamlit as st
from streamlit_option_menu import option_menu
import time
import joblib
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

columns = ['person_income',
 'person_home_ownership',
 'person_emp_length',
 'loan_intent',
 'loan_grade',
 'loan_amnt',
 'loan_percent_income',
 'cb_person_default_on_file',
 'income_group',
 'loan_group']

# Codigo CSS

st.markdown(
  """
  <style>
  
  .ea3mdgi4 {
    padding-top: 0;
  }
  
  input {
    all: unset;
  }
  
  .e1f1d6gn2 {
    margin-bottom: 2rem;
  }
  
  .e1nzilvr1 {
    text-align: center;
  }
  
  .css-1y4p8pa {
    width: 90%;
    max-width: 1200rem;
  }
  
  .st-emotion-cache-16idsys p{
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
    font-weight: 600;
  }
  
  .stProgress {
    width: 80%;
    margin: 0 auto;
  }
  
  .stButton {
    margin: 0 auto;
    width: 40%!important;
  }
  
  .ef3psqc12 {
    width: 100%;
    align-items: center;
    background-color: #1E90FF;
    border: none;
    margin-top: 30px;
  }
  
  .ef3psqc12:hover {
    background-color: #1773cd;
  }
  
  .e115fcil1 {
    margin: 0 auto;
  }
  
  .nav-link-horizontal {
    font-weight: 600;
    font-size: 1.2rem;
  }
  
  .st-emotion-cache-10oheav {
    padding: 2rem 1rem;
  }
  
  .st-emotion-cache-10oheav h1{
    font-size: 2rem;
    font-weight: bold;
    text-align: center;
  }
  
  .st-emotion-cache-1p1nwyz p {
    font-weight: 400;
  }
  
  .st-emotion-cache-1kyxreq img{
    width: 100%;
    max-width: 90%;
    margin: 0 auto;
  }
  
  .st-emotion-cache-ul2nnp p {
    font-weight: 400;
  }
  
  .st-emotion-cache-ul2nnp p a{
    background-color: transparent;
    font weight: bold;
    text-decoration: none;
    text-align: center;
  }
  
  .st-emotion-cache-5rimss p{
    line-height: 2.0; 
    font-size: 1.1rem;
    text-align: justify;
  }
  
  .st-emotion-cache-5rimss img{
    width: auto;
    max-width: 100%;
  }
  
  .img_doc {
    width: 100%;
    text-align: center;
  }
  
  .img_doc_full {
    width: 100%;
    text-align: center;
  }
  
  .img_doc img {
    width: 300px;
    display: block;
    margin: 0 auto;
  }
  
  .img_doc_full img {
    width: 90%;
    display: block;
    margin: 0 auto;
  }
  
  .texto_inicio {
    font-size: 1.1rem;
    text-align: justify;
  }
  
  .parrafo_texto_inifio {
    line-height: 2.0; 
    font-size: 1.5rem;
    text-align: justify;
  }
  
  .bold {
    font-weight: bold;
  }
  
  """, unsafe_allow_html=True
)

#Definir variables de estado

if 'clicked' not in st.session_state:
  st.session_state.clicked = False

if 'saved_data' not in st.session_state:
  st.session_state.saved_data = []

#Manejo de estados

def handle_click_send (arr):
  st.session_state.clicked = True
  st.session_state.saved_data = arr
  
def handle_click_back ():
  st.session_state.clicked = False
  
st.title('Analisis de :blue[riesgo crediticio]')

# Menu de opciones

selected = option_menu(
  menu_title=None,
  options=['Inicio','Scorecard', 'Reporte', 'Video'],
  icons=['', 'bar-chart-line', 'file-earmark-pdf','camera-video'],
  default_index=0,
  orientation='horizontal',
  styles={
    "menu": {"width": "120rem", "display": "flex", "justify-content": "space-between", "margin":"0"},
    "nav-link-selected": {"background-color": "#1E90FF"},
  }
)

if selected == 'Video':
  st.video('https://www.youtube.com/watch?v=EcO911mUdiE')
  
if selected == 'Inicio':
  st.title('Bienvenido a EasyScore')
  col1, col2, col3 = st.columns([1,3,1])
  col2.markdown('''
                <div class='texto_inicio'>
                <p class='parrafo_texto_inifio'>EasyScore es una herramienta que permite a los usuarios conocer su score crediticio de una manera rapida y sencilla.</p>
                <br>
                <p class='parrafo_texto_inifio'>Para conocer tu score crediticio solo debes seleccionar la opcion "Scorecard" en el menu de opciones.</p>
                <p class='parrafo_texto_inifio'> Luego debes ingresar tus datos y darle al boton analizar, esto hara una prediccion de tu posible puntaje crediticio y como te ves tu en relacion a la poblacion </p>
                <p class='parrafo_texto_inifio'>Para conocer mas sobre el score crediticio y el desarrollo de esta aplicacion puedes seleccionar la opcion "Reporte" en el menu de opciones.</p>
                <p class='parrafo_texto_inifio'>Si deseas conocer mas sobre quienes somos puedes seleccionar la opcion "Video" en el menu de opciones.</p>
                <br>
                <p class='parrafo_texto_inifio bold'> Todos los datos ingresados en la aplicacion no son recopilados ni guardados para usos externos, tu eres el unico propietario de tus datos. para conocer mas sobre nuestra politica de privacidad haz click en el siguiente boton </p>
                <button class='ef3psqc12')">Politica de privacidad</button>
                </div>
                ''', unsafe_allow_html=True)

if selected == 'Scorecard':
  
  if st.session_state.clicked == False:
    
    # Formulario de ingreso de datos
    
    col1, col2 = st.columns(2)

    person_income = col1.number_input(':blue[Ingresa tus ganancias anuales (En dolares)]', 0, 5000000, 0)
    
    person_home_ownership = col2.selectbox(':blue[Ingresa tu tipo de vivienda]', ['Renta', 'Hipotecada', 'Propia', 'Otros'], placeholder='Selecciona tu tipo de vivienda')  
    
    person_emp_length = col1.number_input(':blue[Ingresa tu antiguedad laboral (En años)]', 0, 40, 0)
    
    #loan_intent = col2.selectbox(':blue[Ingresa el proposito del prestamo]', ['Personal', 'Educacion', 'Gastos Medicos', 'Empresa', 'Hogar', 'Consolidar deuda'], 
    #                           placeholder='Selecciona el proposito del prestamo')
                                
    #loan_grade = col1.selectbox(':blue[Ingresa el grado de riesgo del prestamo]',
    #                            ['A: Bajo riesgo', 'B: Bajo riesgo relativo', 'C: Riesgo moderado', 'D: Riesgo altamente moderado', 'E: Riesgo alto', 'F: Riesgo muy alto', 'G: Riesgo extremadamente alto'], 
    #                            placeholder='Selecciona el grado del prestamo')
    
    #loan_amnt = col2.number_input(':blue[Ingresa el monto del prestamo]', 0, 1000000, 0)
    
    #loan_percent_income = col1.number_input(':blue[Ingresa el porcentaje de ganancia del prestamo]', 0.00, 100.00, 0.00, step=0.01)
    
    cb_person_default_on_file = col2.selectbox(':blue[Tienes incumplimientos crediticios en tu historia?]', ['No', 'Si'], placeholder='Selecciona si tienes historial de incumplimiento crediticio')
    
    #Establecer rangos para la variable de ingresos y prestamos
    
    if 0 <= person_income <= 30000:
      incomme_group = 'low'
    elif 30000 < person_income <= 50000:
      incomme_group = 'low-middle'
    elif 50000 < person_income <= 70000:
      incomme_group = 'middle'
    elif 70000 < person_income <= 100000:
      incomme_group = 'middle-high'
    elif 100000 < person_income:
      incomme_group = 'high' 
    
    loan_group = 'medium'

    loan_intent = 'Personal'
    
    loan_grade = 'C: Riesgo moderado'
    
    loan_percent_income = 0.26
    loan_amnt = 0.29
    # Definir el boton de analisis
    
    boton = st.button(
      'Analizar', 
      type='primary', 
      on_click=handle_click_send, 
      args=([person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, loan_amnt, loan_percent_income, cb_person_default_on_file, incomme_group, loan_group],)
    )
    
  # Despliegue condicional luego de la ejecucion del boton 
    
  if st.session_state.clicked: 
    
    # Barra de progreso
    st.empty()
    progress_bar = st.progress(0)

    for percent_complete in range(100):
      time.sleep(0.01)
      progress_bar.progress(percent_complete + 1)
    
    progress_bar.empty()
    
    person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, loan_amnt, loan_percent_income, cb_person_default_on_file, incomme_group, loan_group = st.session_state.saved_data
    
    if person_home_ownership == 'Hipotecada':
      person_home_ownership = 'MORTGAGE'
    elif person_home_ownership == 'Renta':
      person_home_ownership = 'RENT'
    elif person_home_ownership == 'Propia':
      person_home_ownership = 'OWN'
    else:
      person_home_ownership = 'OTHER'
      
    if loan_intent == 'Personal':
      loan_intent = 'PERSONAL'
    elif loan_intent == 'Educacion':
      loan_intent = 'EDUCATION'
    elif loan_intent == 'Gastos Medicos':
      loan_intent = 'MEDICAL'
    elif loan_intent == 'Empresa':
      loan_intent = 'VENTURE'
    elif loan_intent == 'Hogar':
      loan_intent = 'HOMEIMPROVEMENT'
    elif loan_intent == 'Consolidar deuda':
      loan_intent = 'DEBTCONSOLIDATION'
    
    if person_home_ownership == 'OWN':
      loan_grade = 'A'
    elif person_home_ownership == 'MORTGAGE' and person_income > 6000:
      loan_grade = 'B'
    elif loan_grade == 'C: Riesgo moderado':
      loan_grade = 'C'
    elif person_home_ownership == 'MORTGAGE' and 4000 < person_income < 5000:
      loan_grade = 'D'
    elif person_home_ownership == 'MORTGAGE' and 2000 < person_income < 3000:
      loan_grade = 'E'
    elif person_home_ownership == 'MORTGAGE' and 1000 < person_income < 2000:
      loan_grade = 'F'
    elif person_income == 0:
      loan_grade = 'G'
    
    if cb_person_default_on_file == 'Si':
      cb_person_default_on_file = 'Y'
    else:
      cb_person_default_on_file = 'N'
    
    encoder = joblib.load('encoder.pkl') 
      
    datos = encoder.transform([[person_home_ownership, loan_intent, loan_grade, cb_person_default_on_file, incomme_group, loan_group]])
    
    person_home_ownership, loan_intent, loan_grade, cb_person_default_on_file, incomme_group, loan_group = datos[0]
    
    values = np.array([person_income, person_home_ownership, person_emp_length, loan_intent, loan_grade, loan_amnt, loan_percent_income, cb_person_default_on_file, incomme_group, loan_group])
    
    Dataframe = pd.DataFrame(values.reshape(-1, len(values)), columns=columns)
    
    model = joblib.load('scorecard_model.pkl')
    
    score = model.score(Dataframe)
    
    score = int(score[0])
    
    if cb_person_default_on_file == 1:
      score = score - 50
    
    if cb_person_default_on_file == 0:
      score = score + 20
    
    global_mean_score = 632
    
    st.image('score-crediticio.svg', width=800)
    
    st.title('Tu score es: ' + str(score))
    
    progress_bar = st.progress(0)
    
    for i in range(int((100/850)*score)):
      progress_bar.progress(i + 1)
      time.sleep(0.001)
    
    time.sleep(0.4)  
    
    st.title('El score promedio de la poblacion es: ' + str(global_mean_score))
    
    progress_bar2 = st.progress(0)
    
    for i in range(int((100/850)*global_mean_score)):
      progress_bar2.progress(i + 1)
      time.sleep(0.001)
    
    time.sleep(0.4)  
    
    boton = st.button('Regresar', type='primary', on_click=handle_click_back)
    
    st.toast('Para regresar presiona el boton!', icon='🎉')
    
    time.sleep(1)
    
    sidebar = st.sidebar
    
    sidebar.title('¿Que es el score crediticio?')
    
    sidebar.write('es una medida numérica que evalúa la solvencia crediticia de una persona o entidad. Este puntaje se utiliza para determinar la probabilidad de que un individuo o negocio pague sus deudas de manera oportuna. En otras palabras, el score crediticio es una herramienta que los prestamistas, como bancos y compañías de tarjetas de crédito, utilizan para evaluar el riesgo crediticio de un solicitante antes de aprobar una solicitud de préstamo o línea de crédito.')
    
    url = 'https://www.transunion.co/score-de-credito'
    sidebar.write(f"[Para saber mas haz click aqui]({url})") 

if selected == 'Video':
  
  st.video('https://www.youtube.com/watch?v=H0rQc9yJlXk')

if selected == 'Reporte':
  col1, col2, col3 = st.columns([1,3,1])
  
  with open('reporte.md', "r",encoding='UTF-8') as markdown_file:
    col2.markdown(markdown_file.read(), unsafe_allow_html=True)
  
  descriptivos_numericos = pd.read_csv('descriptivos_numericos.csv')
  col2.dataframe(descriptivos_numericos)
  col2.markdown('''<center><em>Fig 1. Descriptivos categoricos</em></center>''', unsafe_allow_html=True)
  
  descriptivos_categorical = pd.read_csv('descriptivos_categoricos.csv')
  col2.dataframe(descriptivos_categorical, width=1000)
  col2.markdown('''<center><em>Fig 2. Descriptivos numericos</em></center>''', unsafe_allow_html=True)
  
  col2.markdown('''
                #### 2. **Limpieza de datos.**
                <br>
                Con el objetivo de asegurar la utilidad del análisis, se realiza un proceso de limpieza de datos. Inicialmente se obtiene la cantidad de valores nulos en cada variable con la siguiente tabla.
                <br>
                ''', unsafe_allow_html=True)
  
  datos_nulos = pd.read_csv('datos_nulos.csv')
  col2.dataframe(datos_nulos, width=1000)
  col2.markdown('''<center><em>Fig 3. Valores nulos</em></center>''', unsafe_allow_html=True)
  
  col2.markdown('''
                #### 2. **Limpieza de datos.**
                <br>
                
                Como el dataset tiene un total de 32581 datos y los datos nulos no superan el 10%, se considera mejor eliminar los datos con variables nulas en lugar de imputarlos. Además, se eliminan 137 observaciones duplicadas. Posteriormente, se analiza la distribución de las variables person\_income, person\_age, person\_emp\_length y loan\_amount.
                
                <br>
                ''', unsafe_allow_html=True)
  with open('reporte2.md', "r",encoding='UTF-8') as markdown_file:
    col2.markdown(markdown_file.read(), unsafe_allow_html=True)
  
  col2.markdown('''

#### 3. **Procesamiento de datos.**

<br>

Se realiza la discretización de las variables person\_age, person\_income y loan\_amnt; y se categorizan estos datos en nuevas variables como se muestra a continuación:

<br>

<center>

|**age\_group**|**income\_group**|**loan\_group**|
| :- | :- | :- |
|20-25|low (4000-30000)|small (500-5000)|
|25-30|low-middle (30000-50000)|medium (5000-10000)|
|>30|middle (50000-70000)|large (10000-15000)|
||middle-large (70000-100000)|very large (15000-35000)|
||large (>100000)||

</center>

<br>
<br>

Posteriormente, se aplica un encoder a las variables categóricas en una copia del dataset para convertirlas en variables numéricas y poder realizar el análisis de correlaciones.

<br>
                ''', unsafe_allow_html=True)
  
  datos_escalados = pd.read_csv('datos_escalados.csv')
  col2.dataframe(datos_escalados, width=1000)
  col2.markdown('''<center><em>Fig 12. Datos escalados</em></center>''', unsafe_allow_html=True)
  
  col2.markdown('''
                Se verifica que el encoder se aplicó correctamente con las imagenes anteriores, donde se muestran los 5 primeros datos del dataframe y todas las variables con información de tipo numérico, y se procede a escalar el data.frame con un escalamiento MinMax. Se escogió este tipo de escalamiento en lugar del escalamiento estándar, porque este último se ve afectado por valores atípicos, y como hay una cantidad considerable de ellos.

<br>

#### 4. **Selección de variables.**

<br>

Posteriormente se hace uso de diversas estrategias como la matriz de correlaciones, pruebas chi cuadrado, test ANOVA, análisis WoE y IV para escoger las variables estadísticamente significativas y evitar problemas de multicolinealidad en el modelo. A continuación se presenta la matriz de correlaciones entre las variables:

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmtDuwJpp'>
  <br>
  <em>Fig 14. Matriz Correlacion</em>
</div>

<br>
<br>

##### **Test de hipótesis de relevancia chi cuadrado**

<br>

La prueba de hipótesis de relevancia chi cuadrado, permite evaluar la relevancia de las variables categóricas con el siguiente juego de hipótesis:

> $h_0$: La variable categórica es irrelevante. (Vp > alpha)

> $h_1$: La variable categórica es relevante. (Vp < alpha)

<br>
                ''', unsafe_allow_html=True)
  
  chi2_tabla = pd.read_csv('chi2_tabla.csv')
  col2.dataframe(chi2_tabla, width=1000)
  col2.markdown('''<center><em>Fig 15. Chi2 tabla</em></center>''', unsafe_allow_html=True)
    
  col2.markdown('''
                Se puede apreciar que la única variable que no rechaza la hipótesis nula que indica irrelevancia estadística, es la variable cb\_person\_cred\_hist\_length, la cual hace referencia a los años de historial crediticio que tiene la persona.

<br>

##### **Test de hipótesis de relevancia ANOVA**

<br>

También se realizó un test ANOVA para cada variable continua, cuyos resultados fueron
                ''', unsafe_allow_html=True)
  anovaTabla = pd.read_csv('anovaTabla.csv')
  col2.dataframe(anovaTabla, width=1000)
  col2.markdown('''<center><em>Fig 16. Anova tabla</em></center>''', unsafe_allow_html=True)
  
  col2.markdown('''
                De esta manera, como los Vp son tan pequeños, se acepta la significancia estadística de todas las variables continuas.

<br>

#### **Weight of Evidence (WoE) e Information Value (IV)**

<br>

Finalmente, se toma el criterio de Information Value como decisor para escoger las variables a tener en cuenta para la elaboración del modelo. A continuación se presentan las fórmulas para conseguir este resultado y se considerarán las variables cuyo IV sea superior a 0.02.

<div class='img_doc'>
  <img src='https://imageshack.com/i/pmE90ipjp'>
  <br>
  <em>Fig 17. Formula calculo Woe</em>
</div>

<br>

<div class='img_doc'>
  <img src='https://imageshack.com/i/pmfhrVxxp'>
  <br>
  <em>Fig 18. Formula calculo IV</em>
</div>

<br>

Con estas formulas se hizo un calculo general para cada una de las variables y poder filtrar aquellas que tengan un IV superior a 0.02.
                ''' , unsafe_allow_html=True)
  
  iv_score = pd.read_csv('iv_score.csv')
  col2.dataframe(iv_score, width=1000)
  col2.markdown('''<center><em>Fig 19. IV Score</em></center>''', unsafe_allow_html=True)
  
  col2.markdown('''
                Ademas se realiza un calculo de colinealidad entre todas las variables para verificar cuales de estas tiene un alto valor
                ''' , unsafe_allow_html=True)
  corr_df = pd.read_csv('corr_df.csv')
  col2.dataframe(corr_df, width=1000)
  col2.markdown('''<center><em>Fig 20. Analisis colinealidad</em></center>''', unsafe_allow_html=True)
  
  with open('reporte3.md', "r",encoding='UTF-8') as markdown_file:
    col2.markdown(markdown_file.read(), unsafe_allow_html=True)
  