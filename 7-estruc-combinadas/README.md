# Ejercicios clase 7: Estructuras de Datos combinadas

## Ejercicio 1

Le han dado una lista de _k_ listas, cada una de las listas esta ordenada de manera ascendente. Combine las _k_ listas en una sola lista ordenada y retorne dicha lista.

**Input:**

```python
lists = [[1,4,5],[1,3,4],[2,6]]
```

**Output:**

```python
[1,1,2,3,4,4,5,6]
```

## Ejercicio 2

Dada la lista _students_ que es una lista de diccionario, calcule el promedio de notas de los estudiantes y determine cual es el estudiante con mayor nota dentro del grupo.

**Input**:

```python
students = [
  {
    "name": "Jose",
    "grade": 16
  }
  # ...
]
  {
    "name": "Luis",
    "grade": 17
  },
  {
    "name": "Antonio",
    "grade": 14
  },
  {
    "name": "Gabrielle",
    "grade": 12,
  },
  {
    "name": "Alejandro",
    "grade": 11,
  }
]
```

**Output**:

```python
"El promedio de notas es: 14.0ptos"
"El estudiante con mayor nota es Luis con 17ptos"
```

## Ejercicio 3

Dada la lista _orders_, que representa las ordenes que ciertos clientes han hecho en un restaurante. Específicamente, `orders[i] = [customer_name,table_number,food_item]`

Imprima la tabla _display_table_, que es una tabla cuyas filas denotan cuantos items de comida cada mesa ha ordenado, en donde, la primera columna es el número de la mesa y el resto de las columnas corresponden al nombre de los platos ordenados alfabéticamente. La primera fila debe ser el encabezado de la tabla.

**Input:**

```python
orders = [
    ["David", "3", "Ceviche"],
    ["Corina", "10", "Beef Burrito"],
    ["David", "3", "Fried Chicken"],
    ["Carla", "5", "Water"],
    ["Carla", "5", "Ceviche"],
    ["Rous", "3", "Ceviche"]
  ]
```

**Output:**

```python
[
  ["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
  ["3","0","2","1","0"],
  ["5","0","1","0","1"],
  ["10","1","0","0","0"]
]
```

## Ejercicio 4

Suponga una matriz de enteros `m`x`n` que representan las cuentas de un clientes en donde `accounts[i][j]` es la cantidad de dinero del i-ésimo cliente en el j-ésimo banco. Elabore un algoritmo que calcule la riqueza máxima

La riqueza de un cliente es la cantidad de dinero que tenga en todas sus cuentas; y la riqueza máxima es el máximo valor de todas las riquezas posibles dentro de la matriz.

**Input:**

```python
accounts = [
  [1,5],
  [7,3],
  [3,5]
]
```

**Output:**

```python
'La riqueza máxima es 10'
```

**Explicación:**

- La riqueza del 1er client es 6
- La riqueza del 2do client es 10
- La riqueza del 3er client es 8
  El 2do cliente es el más rico con of 10

## Ejercicio 5

Suponga una lista de diccionarios que contienen una longitud y un material. Ahora imagine que los valores de la longitud dibujan lineas verticales de manera que que los dos extremos de la i-ésima línea son (i, 0) y (i, data[i]) (ver figura 1).

![Figura 1](./e5.jpg)

_Figura 1. Diagrama del problema._

Encuentra dos rectas que junto con el eje x formen un recipiente, tal que el recipiente contenga la mayor cantidad de agua.

Debe calcular la máxima cantidad de agua que puede almacenar un recipiente y determinar de que material esta hecho (esto se sabra combinando los dos materiales de las lineas verticales)

Tenga en cuenta que no puede inclinar el contenedor.

**Input:**

```python
data = [
    {height: 1, material: 'concrete'},
    {height: 8, material: 'wood'},
    {height: 6, material: 'steel'},
    {height: 2, material: 'steel'},
    {height: 5, material: 'wood'},
    {height: 4, material: 'wood'},
    {height: 8, material: 'concrete'},
    {height: 3, material: 'concrete'},
    {height: 7, material: 'steel'}
]
```

**Output:**

```python
f'El área máxima es 49 y el material es wood y steel'
```

_Explicación_:

Las líneas verticales de la figura 1 están representadas por una lista `[1,8,6,2,5,4,8,3,7]`. En este caso, el área máxima de agua (sección azul) que puede contener el contenedor es 49. tomando como referencia los valores `(x, y)` (1, 8) y (8, 7) => $\max{(y_2,y_1)} * (x_2 - x_1)$
