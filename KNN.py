import matplotlib.pyplot as plt
from random import uniform
import pandas as pd
from math import sqrt
import math
p = math.pi

# Funcion que genera 2 numero aleatorios en decimal.
def aleatorios():
    # Generamos 2 numeroa decimales aleatorios
    x = uniform(0, 20)
    y = uniform(0, 20)
    return(x, y)

# Creamos una tabla para nuestros Datos.
data_frame = pd.DataFrame(columns=['Clase', 'x', 'y'])

# Funcion que llena una Tabla.
def generar_clases(clase, tamaño):
    # Llenamos la tabla con con x, y y su Clase. 
    for i in range(tamaño):
        x, y = aleatorios()
        data_frame.loc[len(data_frame)] = [clase, x , y]

# Funcion que saca la distancia de 2 puntos.
def distancia(data_frame):
    new = (9, 7.5)
    distancia = sqrt(((new[0]-data_frame['x'])**2) + ((new[1]-data_frame['y'])**2))
    return distancia

# Generamos los datos con nuestras 2 Clase y mostramos la Tabla.
generar_clases(1, 30)
generar_clases(2, 30)
print(data_frame)
print("\n")

# Creamos una copia de la tabla anterior para agregar sus distancias y ponemos la Distancia.
data_frame_distancia = data_frame
data_frame_distancia['Distancia'] = data_frame_distancia.apply(distancia, axis = 1)

# Mostramos la tabla con sus Distancias.
print(data_frame_distancia)
print("\n")

# Acomodamos la tabla de menor a mayor, dependiendo de las Distancias.
data_frame_distancia = data_frame_distancia.sort_values('Distancia')

# Mostramos la tabla con sus Distancias de menor a mayor.
print(data_frame_distancia)
print("\n")

k = int(input("Ingresa k: "))
k_copia = k
contador_clase1 = 0
contador_clase2 = 0

# Ciclo que cuenta los elementos de las Clases en un K = n.
for columna, fila in data_frame_distancia.iterrows():
    k -= 1
    if(fila['Clase'] == 1):
        contador_clase1 += 1
    else:
        contador_clase2 += 1
    if k == 0:
        distancia_circulo = fila['Distancia']
        break

# Resultado de los elementos que se encuentran en la Clase.
print("\n")
print(f"Para k = {k_copia} se tiene que:")
print(f"La Clase 1 tiene: {contador_clase1}")
print(f"La Clase 2 tiene: {contador_clase2}")

# Saber de que Clase es el nuevo patron.
if contador_clase1 > contador_clase2:
    print("La nueva nuestra pertenece a la Clase 1.")
else:
    print("La nueva nuestra pertenece a la Clase 2.")

# Realizar la Circunferencia que encierra las muestras.
circle2 = plt.Circle((9, 7.5), distancia_circulo, color='black', fill=False)
ax = plt.gca()
ax.add_patch(circle2)

# Generamos nuestra Grafica (Los puntos de la Clase 1 y 2), y al punto nuevo.
plt.scatter(x = data_frame[data_frame['Clase'] == 1]['x'], y = data_frame[data_frame['Clase'] == 1]['y'],
c = 'red', alpha = 1, label='Clase 1')
plt.scatter(x = data_frame[data_frame['Clase'] == 2]['x'], y = data_frame[data_frame['Clase'] == 2]['y'],
c = 'blue', alpha = 1, label='Clase 2')
new = (9, 7.5)
plt.scatter(new[0], new[1], c = 'green', label = 'nueva muestra')

# Asignamos nombre a los ejes y mostramos la Grafica.
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Algoritmo KNN")
plt.legend()
plt.show()