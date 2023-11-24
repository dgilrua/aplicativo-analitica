<br>

Revisando las variables loan\_grade y loan\_int\_rate en la figura anterior, se encuentra un grado de correlación de 0.93, por lo cual se decide eliminar la variable con menor *Information Value,* correspondiente a loan\_int\_rate como se aprecia en la imagen anterior.

De esta manera, se toman las variables mencionadas a continuación para el entrenamiento del modelo:

> 1. loan\_percent\_income: relación entre el crédito y el salario
> 1. loan\_grade: grado de clasificación del crédito
> 1. person\_income: salario anual de la persona
> 1. income\_group: grupo de clasificación al que pertenece el salario
> 1. person\_home\_ownership: estado de la casa (propia, rentada, hipotecada)
> 1. cb\_person\_default\_on\_file: ha hecho default antes?
> 1. loan\_amnt: monto del crédito-
> 1. loan\_intent: intención del crédito.
> 1. loan\_group: clasificación del monto del crédito
> 1. person\_emp\_length: duración de años laborando

<br>

#### **Scorecard**

<br>

Un puntaje crediticio, en el contexto financiero, es un modelo estadístico utilizado para evaluar la solvencia crediticia de individuos o entidades. Asigna una puntuación numérica para evaluar la probabilidad de que un prestatario reembolse sus deudas a tiempo.

Para esto busca identificar las características más importantes que predicen la solvencia crediticia y crea un modelo que genera un puntaje según su predicción.

Estas características se pueden cuantificar en una variable llamada *Points*, la cual asigna un valor dependiendo de la caracteristica del usuario y como esta relaciona con la variable objetivo. Entre mejor sea esta relacion, mas puntos seran asignados a la caracteristica en cuestion y entre menor sea la relacion, menos puntos habrán. 

<br>

Gracias al scorecard, se pueden identificar cuales variables tienen un mayor peso en el posible riesgo a la hora de realizar un credito. Esto se puede ver en la asignacion de puntos en relacion a cada caracteristica; Si los puntos asignados son negativos esto significa que el riesgo de default es muy elevado.

<br>

#### **Modelo**

<br>

Para el proyecto se decidio usar un  modelo de predicción basado en regresión logística, la cual es una técnica estadística que se utiliza para predecir la probabilidad de que una variable categórica binaria (por ejemplo, sí/no, verdadero/falso, éxito/fracaso) ocurra en función de una o más variables predictoras independientes. Esto debido a que la variable target en este caso (loan_status) tiene valores binarios de True o False, por lo que un metodo simple y optimo para predecir estos valores es el de regresion logistica

<br>

#### **Evaluacion del Modelo**

<br>

Se presenta a continuación la matriz de confusión asociada al modelo y las métricas arrojadas 

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmPxJDj3p'>
  <br>
  <em>Fig 21. Matriz de confusion</em>
</div>

<br>

El modelo presenta un accuracy de 0.847 aproximadamente, lo cual indica que acierta en promedio el 84.7% de las clasificaciones totales.

Además, tiene una precisión aproximada de 0.734, indicando que el porcentaje de acierto de la clase de default es de 73,4%. También tiene un altísimo nivel de recall, indicando que el modelo clasifica correctamente el 95.3% de todos los clientes default.

Finalmente, la métrica del F1-Score es de 0.829 mostrando un rendimiento bastante acertado para predecir clases por parte del modelo.

#### *Curva ROC*

<br>

<div class='img_doc_full'>
  <img src='https://imageshack.com/i/pmpx72jfp'>
  <br>
  <em>Fig 22. Curva ROC</em>
</div>

<br>

El área debajo de la curva ROC representa la probabilidad de que el resultado del modelo para un caso positivo elegido aleatoriamente supere el resultado para un caso negativo elegido aleatoriamente. En nuestro caso podemos ver que esa área es de 0.86 o 86% lo cual es un valor bastante bueno.

Finalmente, se puede determinar en la realización del modelo que hay variables de gran influencia sobre la probabilidad de impago, algunas de ellas son loan_percent_income, loan_grade y person_income. Así, podemos concluir que algunos de los factores diferenciales en la probabilidad de impago son el salario del aspirante, el grado del crédito y la relación entre el monto de la deuda y el salario. 

#### *Referencias*

<br>

1. Gopidurgaprasad. (2022). AMEX : Credit Score Model 💳. Kaggle. https://www.kaggle.com/code/gopidurgaprasad/amex-credit-score-model#Weight-of-Evidence(WOE)

<br>

2. Gonçalves, G. D. S. (2022, 7 enero). Developing scorecards in Python using OptBinning - towards data science. Medium. https://towardsdatascience.com/developing-scorecards-in-python-using-optbinning-ab9a205e1f69

<br>

3. Maklin, C. (2022, 10 mayo). Metrics for evaluating machine learning classification models. Medium. https://towardsdatascience.com/metrics-for-evaluating-machine-learning-classification-models-python-example-59b905e079a5