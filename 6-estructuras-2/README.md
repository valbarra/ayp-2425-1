# Ejercicios clase 6: Set, tuplas y diccionarios

- [Ejercicios clase 6: Set, tuplas y diccionarios](#ejercicios-clase-6-set-tuplas-y-diccionarios)
  - [Ejercicio 0](#ejercicio-0)
  - [Ejercicio 1](#ejercicio-1)
    - [1.1](#11)
    - [1.2](#12)
  - [Ejercicio 2](#ejercicio-2)
    - [2.1](#21)
    - [2.2](#22)
  - [Ejercicio 3](#ejercicio-3)
  - [Ejercicio 4](#ejercicio-4)
  - [Ejercicio 5](#ejercicio-5)

## Ejercicio 0

Realice un programa capaz de determinar si un número es abundante.

En teoría de números, un **número abundante** o número excesivo es un número para el cual la suma de sus divisores propios es mayor que el propio número. El entero 12 es el primer número abundante. Sus divisores propios son 1, 2, 3, 4 y 6 para un total de 16.

## Ejercicio 1

### 1.1

Usa zip para escribir un bucle **for** que cree una lista que especifique el label y las coordenadas de cada punto. Cada elemento debe formatearse como:

**Output:**

```python
f'{label}: {x}, {y}, {z}'
```

**Por ejemplo:**

```python
'F: 23, 677, 4'
```

### 1.2

Usa enumerate para modificar la lista de casting para que cada elemento contenga el nombre seguido de la altura correspondiente del personaje.

Por ejemplo, el primer elemento del elenco debería cambiar de "Barney Stinson" a "Barney Stinson 72".

---

## Ejercicio 2

### 2.1

Utilizando _sets_, determine cuales son los elementos iguales entre dos listas.

**nota**: Puede ayudarse utilizando teoría de conjuntos.

### 2.2

Realice un programa que le pida al usuario una palabra y determine cual vocales contiene dicha palabra.

Output:

```python
f'La palabra {output} tiene a las vocales {vowels}'
```

---

## Ejercicio 3

Cuente la cantidad de frutas en su cesta. Para hacer esto, tiene el diccionario y la lista de frutas. Use el diccionario y la lista para contar el número total de frutas y los otros artículos que no son frutas en su cesta.

**Output:**

```python
f'Hay {qty_fruits} frutas en la cesta. y {qty_no_fruits} objetos que no son frutas.'
```

---

## Ejercicio 4

Podemos crear un diccionario, contador, que realiza un seguimiento del recuento total de cada palabra en la lista quote.

**Output:**

```python
`{'Tienes': 1, 'que': 1, 'bailar': 1, 'como': 4, 'si': 4, 'no': 2, 'hubiera': 2, 'nadie': 2, 'mirando': 1, 'Ama': 1, 'nunca': 1, 'te': 1, 'lastimaran': 1, 'Canta': 1, 'escuchando': 1,'Y': 1, 'vive': 1, 'fuera': 1, 'el': 1, 'cielo': 1, 'en': 1,'la': 1, 'tierra.': 1}`
```

---

## Ejercicio 5

Determine si la representación binaria de dos números son anagramas

_Un anagrama es un procedimiento que consiste en crear una palabra a partir de la reordenación de las letras de otra palabra._

**Ejemplo:**

```python
a = 8 # 1000
b = 4 # 0100
c = 5 # 0110
d = 4 # 0100
```

**Output:**

```shell
Los números {a} y {b} son un anagrama
```

**Pista**: Utilice la función _[bin](https://www.programiz.com/python-programming/methods/built-in/bin)_
