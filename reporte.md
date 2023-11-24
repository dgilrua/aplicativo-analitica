### **Definición del problema.**
<br>

El crédito es una herramienta indispensable en el sistema económico mundial, este instrumento financiero estimula la circulación de los recursos que permiten realizar inversiones en búsqueda del aumento de la competitividad empresarial y la mejora del bienestar social. Sin embargo, las entidades crediticias se encuentran con un negocio asimétrico, en el cual si se dan préstamos de manera irracional y desproporcionada, se perderá mucho más dinero del que se pudo haber ganado, muestra de ello es la crisis financiera del 2008, cimentada en los créditos otorgados a personas con pobre historial crediticio en el sector inmobiliario, afectando no solo a entidades financieras sino también a la economía global.

<br>

De esta manera, para las entidades crediticias es de notable interés tener la capacidad de saber si una persona cumplirá o no con sus obligaciones crediticias antes de realizar el desembolso del dinero. Por tal motivo, recolectan datos del aspirante como el ingreso anual, el número de propiedades, la cantidad de dinero prestada, la finalidad del préstamo, el historial crediticio, entre otras para determinar qué tan probable es que la persona no pague, a lo cual se le da el nombre de PD (Probabilidad de Default) y clasificarlo entre las categorías de pago o no pago. Todo esto con el entrenamiento de modelos soportados por campos como la estadística y la analítica de datos.

<br>

### **Metodología.**


<br>

Para el desarrollo de un modelo que permita afrontar la problemática anteriormente mencionada, se presentan los siguientes pasos.

<br>

> 1. Exploración de datos.
> 1. Limpieza de datos.
> 1. Procesamiento de datos.
> 1. Selección de variables.
> 1. Entrenamiento del modelo.

<br>

## **Desarrollo**

<br>

#### 1. **Exploración de los Datos.**

<br>

En primer lugar se carga la base de datos con nombre *credit\_risk\_dataset.csv,* analizando aspectos básicos como el número de observaciones, la cantidad de variables, las variables con datos *null* y el tipo de dato en el cual se almacena la información. También se determina la variable loan\_status como target.

Variable loan\_status: 

> 0 &nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;No Pago, Incumplimiento de las obligaciones.

> 1 &nbsp;&nbsp;&nbsp;→&nbsp;&nbsp;&nbsp;Pago, Cumplimiento de las obligaciones.

Agregado a esto, se plantean hipótesis del comportamiento de la variable target (loan\_status) frente a cambios en las demás variables:

<br>

<center>

|**income\_group**|**loan\_group**|
| :- | :- |
|loan_percent_income|Aumenta|
|person_income|Disminuye|
|income_group|Disminuye|
|loan_amnt|Aumenta|
|person_emp_length|Disminuye|

</center>

<br>
<br>

Por otra parte, el dataset tiene un total de 32581 observaciones y 12 variables, de las cuales 8 son numéricas y 4 categóricas. Posteriormente, se realiza el análisis de estadísticos descriptivos para variables numéricas y categóricas, en busca de valores atípicos y una idea inicial de la distribución de los datos.