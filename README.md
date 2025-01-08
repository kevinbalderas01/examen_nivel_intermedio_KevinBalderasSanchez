# Examen Nivel Intermedio

A continuación se presenta la sollución del examen a nivel intermedio con ejercicios en Python. La estructura del presente directorio es:
* examen.py: Contiene la respuesta a los 8 problemas planteados
* README.md: Contiene la descripción en formato mardown del presente repositorio
* /imgs : Contiene las imagénes de screenshots para probar correcta ejecución de las funciones.

## Estructura:
El archivo examen.py tiene 4 bloques principales, los cuales son:
* Dependencias: Aquí se importan las dependencias necesarias como pandas, faker y sklearn. Me tome la libertad de importar loggins, que es nativo de python y me permite mostrar logs a medida que se ejecuta el script. Es algo que he notado utilizan en producción y me pareció buena idea agregarlo, salvo su mejor opinión.
* Funciones: Son las 8 funciones requeridas completadas, tienen la notación de docstring para mejorar documentación de código.
* Utilidades: Aquí inicializo el logger para mostrar registros, también un dataset de prueba básico para mostrar funcionamiento de las funciones y genero los datos dummy de tipo binario, para el problema de clasificación
* Main: Esta es la ejecución principal del script, y sólo se ejecuta cuando el script se manda a llamar directamente , es decir, cuando no está actuando como modulo. 


## Funciones:
#### Problema 1- Filtrar DataFrame con pandas
La lógica de esta función es que teniendo como argumento un dataframe, una columna y un umbral de valor, regresa otro dataframe, pero transformado y filtrado. Cabe resaltar que tiene manejo de error para en caso de haber ingresado un nombre incorrecto o tipo de valor incorrecto lanzar un logging de error, tal como se muestra en la imagen.
Declaración Función        |  Llamada con manejo de errores
:-------------------------:|:-------------------------:
![Función_1](../imgs/01.png) | ![Función_1](../imgs/02.png)


#### Problema 2- Generar datos para regresión
Para este problem, se utilizó faker para generar datos aleatorios entre 0 y 1.Luego de ahí sólo se manipularon los datos para estar en los formatos adecuados para ser utilizados en el siguiente problema. También en caso de poner un número negativo se tiene que mandar un log de error señalandolo.

Declaración Función        |  Llamada con manejo de errores
:-------------------------:|:-------------------------:
![Función_2](../imgs/03.png) | ![Función_2](../imgs/04.png)

#### Problema 3- Entrenar modelo de regresión múltiple
Aquí, se parte del problema 2, donde se obtuvieron los datos "X" y "y" para aquí entrenar un modelo de regresión lineal. Si bien no venía específicado, me tome la libertad de hacer un split entre train y test para hacer notar el concepto ya que es muy importante a la hora de entrenar modelo, no entrenar sobre todo, sino sobre una parte y así evitar el overfitting. De igual manera, se tiene manejo de errores en caso de pasar a las funciones argumentos no adecuados. Y para finalizar y comprobar el entrenamiento, se utiliza el método predict sobre el conjunto X completo, vemos que nos regresa una respuesta indicando que se entrenó el modelo. Los detalles de si es el mejor modelo se omiten por ahora.


Declaración Función        |  Llamada con manejo de errores
:-------------------------:|:-------------------------:
![Función_3](../imgs/05.png) | ![Función_3](../imgs/06.png)


#### Problema 4- Lista comprehensión anidado
Para este problema sólo se tuvo que desanidar un conjunto de listas dentro de otra lista haciendo uso de list comprehensions. Aquí solo fue necesario el manejo de error en caso de dar como argumento a la función un tipo de dato inadeacuado.

Declaración Función        |  Llamada con manejo de errores
:-------------------------:|:-------------------------:
![Función_4](../imgs/07.png) | ![Función_4](../imgs/08.png)


#### Problema 5- Agrupar y agregar con pandas
Para esta función se tuvo que hacer uso de pandas y la función groupby para agrupar por determinada medida de agregación, en nuestro caso el promedio. Cabe resaltar que antes de hacer el proceso, se selecciona la columna deseada y así evitar que se calcula la agregación para todas las columnas numéricas, que es el comportamiento por defecto de la función de pandas. También tiene manejo de errores con datos de columnas incorrectos

Declaración Función        |  Llamada con manejo de errores
:-------------------------:|:-------------------------:
![Función_5](../imgs/09.png) | ![Función_5](../imgs/10.png)

#### Problema 6- Modelo de clasificación logística
Para el modelo de clasificación logística nos menciona que debemos pasarle como argumento a la función X y Y. Pero como también dicen que con un conjunto de datos de tipo binario. Asi que aprovechando el faker ya importado, se hizo uso de él para generar estos datos dummy. Como es un problema de clasificación, ahora nuestra predicción será un 0 o 1. También tiene manejo de errores. De igual manera, los detalles de cómo hacer el mejor modelo no se tocan aquí, tan sólo me limite a hacer un split entre train y test y así entrenar el modelo de manera adecuada.

Declaración Función        |  Llamada con manejo de errores
:-------------------------:|:-------------------------:
![Función_6](../imgs/11.png) | ![Función_6](../imgs/12.png)


#### Problema 7- Aplicar función a una columna con pandas
Para resolver esta consigna, utilice la función que ya viene por defecto con pandas, ya que se me hizo más lógico hacer uso de ella y así evitar hacer algún tipo de decorador que cumpliera de igual manera. La función toma como entrada la columna, la función que será aplicada y un dataframe. En este caso para probar, utilizamos una lambda para probar. También se manejan los errores al pasar tipos de datos incorrectos.

Declaración Función        |  Llamada con manejo de errores
:-------------------------:|:-------------------------:
![Función_7](../imgs/15.png) | ![Función_7](../imgs/14.png)


#### Problema 8- Comprehensions con condiciones
Para esta tarea solamente se hizo uso de las comprehensiones de listas para elevar los números al cuadrado, que son mayores a 5. También con manejo de error en caso de proporcionar algo que no sea una lista, tal como indica la definición de la función

Declaración Función        |  Llamada con manejo de errores
:-------------------------:|:-------------------------:
![Función_8](../imgs/13.png) | ![Función_8](../imgs/16.png)


#### Ejecución final
Por último, encontramos que al ejecutar el programa .py, tendremos los logs correspondientes que nos permitiran atacar algún caso de error , o en caso contrario, verificar que todas las funciones son correctas, con los argumentos solicitados y resultados esperados.
![Imagen de logs](../imgs/17.png)
