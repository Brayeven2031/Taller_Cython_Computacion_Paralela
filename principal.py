"""
- Fecha: 1 nov 2022
- Autor: Brayan Stiven Castañeda
- Tema: Cython
- Tópico: Planetas - orbita gravitacional
- Principal: Llama a ambos programas (Cy/Py)
    * La idea principal es crear un csv con la toma de tiempos *
"""

import orbita_cy
import orbita_py
import time

# Se inicializa el planeta para Python
# Datos de WikiPedia
tierra_py = orbita_py.Planet()
tierra_py.x = 100*10**3
tierra_py.y = 300*10**3
tierra_py.z = 700*10**3
tierra_py.vx = 2.00*10**3
tierra_py.vy = 29.87*10**3
tierra_py.vz = 0.034*10**3
tierra_py.m = 5.9742*10**24

# Se inicializa el planeta para Cython
# Datos de WikiPedia
tierra_cy = orbita_cy.Planet()
tierra_cy.x = 100*10**3
tierra_cy.y = 300*10**3
tierra_cy.z = 700*10**3
tierra_cy.vx = 2.00*10**3
tierra_cy.vy = 29.87*10**3
tierra_cy.vz = 0.034*10**3
tierra_cy.m = 5.9742*10**24

# Se consideran las otras variables
time_span = 400
n_steps = 2000000

# Se crea un formato para la impreión sobre el fichero
formato_datos = "{:.5f}, {:.5f}\n"

# Definición de experimentos
# Reducción ruido Gaussiano 
for i in range(2):
    
    # Toma de tiempos para Python
    ini_time = time.time()
    orbita_py.step_time(tierra_py, time_span, n_steps)
    fin_time = time.time()

    time_python = fin_time-ini_time

    # Toma de tiempos para Cython
    ini_time = time.time()
    orbita_cy.step_time(tierra_cy, time_span, n_steps)
    fin_time = time.time()

    time_cython = fin_time-ini_time

    with open("planeta.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))

    print("Cython Time: ",time_cython)
    print("Python Time: ",time_python)

    print("Cython es: ",time_python/time_cython," mas rapido")
    print()
    