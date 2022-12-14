<div> 
<br>
<i><b>Autor:</b></i> Brayan Stiven Castañeda Cruz
<br>
<i><b>Asignatura:</b></i> Programación Paralela y Distribuida
<br>
<i><b>Fecha: </b>01-11-2022
<br>
<b>Ciencias de la computación e inteligencia artificial</b></i>
<br>
</FONT>
</div>


# __Taller Cython Computacion Paralela__
`En el presente laboratorio se encuentra depositado un ejemplo de programación con el lenguaje de programación Cython`

Para iniciar se considera pertinente hablar sobre el lenguaje de programación Cython. Cython es un lenguaje de programación diseñado para usar la sintaxis de Python y a su vez que pueda implementar métodos y estrategias de programación utilizadas en C y C++, por lo que un código realizado en este lenguaje contaría con beneficios de rendimiento como se observan en C y C++. En otros términos, un programa escrito en este lenguaje contendría la sintaxis de python, solo que, con ciertas correcciones en las declaraciones de variables y funciones, y sería compilado a código de C o C++.

## __Ejemplo de Cython__
A continuación, se encontrarán cinco archivos que conformarán el ejemplo de programación con el lenguaje de programación Cython, que será contrastado contra el rendimiento del lenguaje de programación Python, esto con el fin de comprobar cuantas veces termina siendo más eficiente un programa escrito en Cython contra uno escrito en python. Cabe resaltar que ambos programas darán respuesta al mismo problema, desplazamiento de un cuerpo espacial en una determinada orbita.

Los archivos encontrados dentro del repositorio son los siguientes: 
>### **orbita_py.py**
>En este programa encontrará la solución propuesta dentro del lenguaje de programación python.

>### **orbita_cy.pyx**
>En este programa encontrará la solución propuesta dentro del lenguaje de programación cython. A nivel de comparación podrá observar que será la misma solución escrita en python, pero, así como se nombró al inicio del repositorio, su única diferencia en la sintaxis es que en cython se debe declarar el tipo de variable y marcar el origen de las clases y de las funciones, de este modo Cython entiende el modo de trabajar con determinado valor, variable u función.

>### **setup.py**
>El setup es un programa que permite realizar la compilación del archivo `.pyx` a código C. Se divide el setup del código principal para trabajar bajo las buenas prácticas que se aplican con la compilación por separado.

>### **principal.py**
>Este programa realiza la ejecución de los dos programas que contienen la solución, para esto, este programa escrito en Python implementará ambos programas como bibliotecas y de este modo accede a sus métodos. Posteriormente, toma el tiempo de ejecución para ambos programas por separado, y termina contrastando los rendimientos obtenidos por ambos programas. Por último, imprime el número de veces que el `.pyx` termina siendo más rápido que el `.py`

>### **Makefile**
>Este programa automatiza el proceso de compilación y creación del recurso compartido del archivo `.pyx`

>### **Taller Cython Computacion Paralela - Métricas de Rendimiento (Brayan Stiven Castañeda).ipynb**
>En este Notebook se encontrará un análisis de los resultados obtenidos con la ejecución de los resultados, además se agregan conclusiones obtenidas mediante la elaboración ejecución y análisis del experimiento.

## __Ejecución__
`Por favor tener en cuenta que el método de ejecución descrito a continuación, únicamente aplica para entornos linux`.
1. Inicialmente descargue los cinco archivos y ubíquelos en su carpeta de preferencia. Todos los archivos deben estar en la misma carpeta.
2. Abra una terminal de linux y ubíquese en la carpeta donde se encuentran situados los archivos.
3. Ejecute el siguiente comando: make all, esto con fin de esto para generar e recurso compartido y compilar el archivo `.pyx`.
4. Ejecute el siguiente comando: `python3 principal.py` y los resultados se guardarán en el archivo csv `planeta.csv`.
5. Con el comando `cat planeta.csv` podrá visualizar los resultados obtenidos en las ejecuciones.

> ***NOTA: Tenga en cuenta que, para la ejecución anterior, debe tener instalado el intérprete de python3***
