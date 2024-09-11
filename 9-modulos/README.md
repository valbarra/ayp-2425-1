# Ejercicios clase 10: Try Except, Funciones Lambda, módulos

## Ejercicio 1

Realice una función _lambda_ que reciba dos pares ordenado `(x,y)` y determine la distancia entre los puntos. La distancia entre dos puntos se calcula utilizando la ecuación:

![distancia](https://latex.codecogs.com/png.latex?%5Cdpi%7B120%7D%20%5Chuge%20d%20%3D%20%5Csqrt%7B%28x_2-x_1%29%5E2%20+%20%28y_2%20-%20y_1%29%5E2%7D)

## Ejercicio 2

Desarrolle una función que pueda castear un string a un número flotante, considerando que el separador por defecto es `.` puede puede ser `,`.

**Input:**

```python
num = parse_float('1,9') # 1.9
num = parse_float('2.3') # 2.3
num = parse_float('Error') # Exception
```

## Ejercicio 3

Desarrolle un archivo _utils_ en donde se encuentren las funciones: `get_costumer_information`, `add_to_basket`, `calculate_subtotal` y `calculate_tax`, estas funciones servirán de apoyo al código principal para desarrollar un programa que le permita al usuario ingresar su información de facturación, escoger productos de un menú y luego informarle el total sobre su compra.

## Ejercicio 4

### Ejercicio 4.1

map(<funcion, List[]>) es una función de Python que toma como parámetros una función y una lista, este retorna una lista con el que se le aplico la función pasada como parámetro a cada elemento de lista.

Usa map() para encontrar la media de cada elemento en la lista 'números' y crear una nueva lista llamada promedios.

Puedes leer más sobre map() [aquí](https://www.w3schools.com/python/ref_func_map.asp)

**Nota:** Para este ejercicio es obligatorio aplicar el uso de lambda expressions en Python.

**Output esperado:**

```python
[57.0, 58.2, 50.6, 27.2]
```

### Ejercicio 4.2

filter(<funcion, list[]>) es una función de Python que toma como parámetros una función y una lista, este retorna una lista con el que se le aplico la función pasada como parámetro a cada elemento de lista y solo se insertan aquellos elementos que cumplen con la condición.

Usa filter() para obtener los nombres en ciudades que tienen menos de 8 caracteres y crea una nueva lista llamada ciudades_pequenas[]

Puedes leer más sobre filter() [aquí](https://www.w3schools.com/python/ref_func_filter.asp)

**Nota:** Para este ejercicio es obligatorio aplicar el uso de lambda expressions en Python.

**Output esperado:**

```python
['Caracas', 'Barinas']
```

## Ejercicio 5

Escriba una función llamada generar_contrasena que seleccione tres palabras aleatorias de la lista lista_palabras[] y las concatene en un solo String. Su función no debe aceptar ningún argumento y debe hacer referencia a la variable global lista_palabras para crear la contraseña.

Puedes usar una función de la librería random llamada choice para encontrar un elemento aleatorio de una secuencia no vacía. Más información en el link debajo:

[https://docs.python.org/3.7/library/random.html?highlight=choice](https://docs.python.org/3.7/library/random.html?highlight=choice)
