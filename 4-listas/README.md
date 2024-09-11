# Ejercicios Clase 4: Listas

## Ejercicio 1

Escriba un programa para agregar el elemento 7000 después de 6000 en la siguiente lista de Python

**Input**:

```python
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
```

**Output**:

```python
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
```

## Ejercicio 2

Dados dos vectores $\vec{u}$ y $\vec{v}$ en el espacio vectorial $\reals^3$ se define a la operaciones entre vectores como:

- suma ($\vec{u} + \vec{v}$)
- producto punto ($\vec{u} \cdot \vec{v}$)
- producto cruz ($\vec{u} \times \vec{v}$)

Realice un programa que considere a dos listas de tres posiciones como los vectores $\vec{u}$ y $\vec{v}$ y ejecute las tres operaciones entre estos vectores:

**Nota**: Asi se definen las operaciones:

$$
\vec{u} + \vec{v} = \begin{bmatrix}
u_1+v_1\\
u_2+v_2\\
u_3+v_3
\end{bmatrix}
$$

$$\vec{u} \cdot \vec{v} =  u_1v_1 + u_2v_2 + u_3v_3$$

$$
\vec{u} \times \vec{v} = \begin{bmatrix}
u_2v_3 - u_3v_2\\
u_3v_1 - u_1v_3\\
u_1v_2 - u_2v_1
\end{bmatrix}
$$

## Ejercicio 3

Considere la siguiente lista:

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

Responda las siguientes preguntas, utilizando unicamente slices en python

1. Agregue las letras `ñ`, `ch` y `ll` al alfabeto
2. Imprima las primeras cinco letras del abecedario
3. Imprima las últimas cinco letras del abecedario
4. Imprima el alfabeto si se eliminarán las letras que están en posiciones impares
5. Imprima el reverso del alfabeto

## Ejercicios 4 (Extra)

Escribe un _for loop_ que itere sobre la lista 'estudiantes' y crea una lista 'usernames' para cada nombre. Para crear un username debes:

- Colocar todo el nombre en minúscula.
- Remplaza los espacios con guion bajo `_`

**Pista**: Puedes remplazar los espacios con el método .replace(), para saber como funciona chequea esta documentación:

[https://www.w3schools.com/python/ref_string_replace.asp](https://www.w3schools.com/python/ref_string_replace.asp)
