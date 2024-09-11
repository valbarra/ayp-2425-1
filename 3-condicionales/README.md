# Ejercicios Clase 3: Expresiones lógicas, condicionales, funciones built-in de Python

## Ejercicio 1

Realizar un programa donde se reciba un número flotante por teclado e imprima un mensaje diciendo si el número es par o impar y evaluar si es positivo/negativo.

**Output:**

```python
'El número: **X** es par/impar y positivo/negativo'
```

Donde **X** es el número ingresado por teclado.

---

## Ejercicio 2

Una famosa cadena de cines en Venezuela te contrató para hacerles un programa de descuento en las entradas basado en la edad del cliente, para ello tendrás que recibir por teclado la edad y nombre del cliente y verificar los siguientes casos:

- Si su edad es menor o igual a 4 años el precio de su entrada es gratis.
- Si su edad es menor o igual a 18 años el precio de su entrada es de $1.50
- Si su edad es mayor o igual a los 60 años su entrada tendrá un valor de $1
- La entrada para un adulto promedio es de $2.00

Deberás imprimir un mensaje dependiendo de la edad del cliente para saber el precio de su entrada.

**Output:**

```python
'El cliente: {nombre} tiene: {edad} años y su entrada de cine cuesta: ${precio_entrada}'
```

---

## Ejercicio 3

Te contrataron para realizar un programa donde calcule el premio de un juego.

Los premios son basados en puntos:

**Puntos** **Premio**

- 1-50 No hay premio
- 51-150 Bronze
- 151-180 Plata
- 181-200 Oro

Todos los límites inferior y superior aquí son inclusivos, y los puntos solo pueden tomar valores enteros positivos hasta 200.

En su declaración **if**, asigne la variable de resultado a un String que contenga el mensaje apropiado según el valor de los puntos.

Si ganaron un premio, el mensaje debería decir:

**Output:**

```python
 "Felicitaciones, Ganaste la medalla de {nombre del premio} por haber tenido {puntos} pts!"
```

Si no hay premio, el mensaje debe decir:

**Output:**

```python
 "No hay premios para {puntos} pts"
```

---

## Ejercicio 4

Llamamos raíces de una ecuación de segundo grado con una variables a los dos valores: $x_1$ y $x_2$, si existen, para los que la igualdad de la siguiente ecuación es cierta

$$
x_{1,2} = \frac{- b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Elabore un programa que dado los valores $a$, $b$ y $c$ produzca como resultado los valores para $x_1$ y $x_2$ si existen

---

## Ejercicio 5

Desarrolla en Python el juego de _Piedra, Papel y Tijeras_ en donde pedirás por teclado la opción del jugador 1, luego la opción del jugador 2, y posteriormente dará el resultado diciendo quien gano.
