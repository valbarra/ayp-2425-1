# Ejercicios clase 5: Ciclos de repetición y list comprehension

**Contenidos:**

- [Ejercicios clase 5: Ciclos de repetición y list comprehension](#ejercicios-clase-5-ciclos-de-repetición-y-list-comprehension)
  - [Ejercicio 1](#ejercicio-1)
  - [Ejercicio 2](#ejercicio-2)
    - [2.1](#21)
    - [2.2](#22)
  - [Ejercicio 3](#ejercicio-3)
  - [Ejercicio 4](#ejercicio-4)
    - [4.1](#41)
    - [4.2](#42)
  - [Ejercicio 5](#ejercicio-5)

---

## Ejercicio 1

**1.1** Use un for loop para tomar la lista que se llama 'oracion' e imprima cada elemento de la lista en su propia línea.

oracion = ["Estoy", "imprimiendo", "una", "lista", "linea", "por", "linea"]

**Output:**

```python
Estoy
```

```python
imprimiendo
```

```python
una
```

```python
lista
```

```python
linea
```

```python
por
```

```python
linea
```

**1.2** Escribe un for loop que imprima números enteros multiples de 5 menores e iguales a 30.

**Output:**

```
5
```

```
10
```

```
15
```

```
20
```

```
25
```

```
30
```

---

## Ejercicio 2

### 2.1

Escribe un For Loop que itere sobre la lista 'students' y crea una lista 'usernames' para cada nombre. Para crear un username debes:

- Colocar todo el nombre en minúscula.
- Remplaza los espacios con guion bajo " \_ ".

**Input:**

```python
students = ["Elijah Evans", "Charissa Mueller", "Kirby Park",
     "Jescie Hill",
     "Leroy Herring",
     "Francis Castaneda",
     "Bree Gregory",
     "Kermit Stevens",
     "Jordan Terry",
     "Paul Trujillo",
     "Linda Beck",
     "Dara Mckinney",
     "Idola Pearson",
     "Phelan Vazquez",
     "Cleo Dyer",
     "Kameko Mccall",
     "Kitra Tillman",
     "Oren Miles",
     "Martin Kerr",
     "Orlando Noble",
     "Ferdinand Carr",
     "Scott Norman",
     "Autumn Winters",
     "Phillip Heath",
     "Ryder Mueller",
     "Armand Lucas",
     "Naida Hart",
     "Deborah Spencer",
     "Blythe Kidd",
     "Colleen Keller"]
```

**Pista:** Puedes remplazar los espacios con el método .replace(), para saber como funciona chequea esta documentación:

`https://www.w3schools.com/python/ref_string_replace.asp`

### 2.2

Ahora en vez de crear una nueva lista, queremos actualizar la lista existente llamada estudiantes.

---

## Ejercicio 3

Debes escribir un While Loop que tome los números en una lista dada llamada: `num_list`

```python
num_list = [422, 136, 524, 84, 96, 719, 85, 92, 10, 17, 312, 542,
            86, 24, 86, 190, 116, 36, 174, 46, 150, 58, 84, 60, 114, 167]
```

Su código debe **sumar** los números impares en la lista, pero solo hasta los primeros 5 números impares.

- Sumar los primeros 5 números impares en la lista.
- Si hay mas de 5 números impares, detenerse de sumar en el 5to número y mostrar mensaje con la cantidad de números impares y la suma total.

**Output:**

```python
"La cantidad de números impares es: {contador_impares}"
"La suma total de los números impares es: {suma_impares}"
```

---

## Ejercicio 4

### 4.1

Use una comprensión de la lista para crear una nueva lista primeros_nombres que contenga solo los primeros nombres en minúsculas.

**Input**:

```python
names = ["Elijah Evans", "Charissa Mueller", "Kirby Park",
               "Jescie Hill",
               "Leroy Herring",
               "Francis Castaneda",
               "Bree Gregory",
               "Kermit Stevens",
               "Jordan Terry",
               "Paul Trujillo",
               "Linda Beck",
               "Dara Mckinney",
               "Idola Pearson",
               "Phelan Vazquez",
               "Cleo Dyer",
               "Kameko Mccall",
               "Kitra Tillman",
               "Oren Miles",
               "Martin Kerr",
               "Orlando Noble",
               "Ferdinand Carr",
               "Scott Norman",
               "Autumn Winters",
               "Phillip Heath",
               "Ryder Mueller",
               "Armand Lucas",
               "Naida Hart",
               "Deborah Spencer",
               "Blythe Kidd",
               "Colleen Keller"]
```

**Output**:

```python
['elijah', 'charissa', 'kirby', 'jescie', 'leroy', 'francis', 'bree', 'kermit', 'jordan', 'paul', 'linda', 'dara', 'idola', 'phelan', 'cleo', 'kameko', 'kitra', 'oren', 'martin', 'orlando', 'ferdinand', 'scott', 'autumn', 'phillip', 'ryder', 'armand', 'naida', 'deborah', 'blythe', 'colleen']
```

### 4.2

Use una comprensión de lista para crear una lista `multiplos_3` que contenga los primeros 20 múltiplos de 3.

**Output**:

```python
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
```

## Ejercicio 5

Desarrolla un programa que permita calcular el cuadrado mas cercano a un numero,ejemplo: el cuadrado mas cercano de **40** es 36 (ya que 6\*6)
