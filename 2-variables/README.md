# Ejercicios Clase 2: Tipos de datos, variables y operadores

## Ejercicio #1

**Nota: Usar archivo e1.py**

Se le ha dado un conjunto de variables para que le realice modificaciones.

1. disminuir la variable de lluvia en un 10% para tener en cuenta el agua de lluvia que circula libremente sobre la superficie de un terreno.

2. Agregue la variable de lluvia a la variable volumen_reservorio.

3. Aumentar volumen_reservorio en un 5% para tener en cuenta las aguas pluviales que fluyen en el embalse en los días posteriores a la tormenta.

4. Disminuir volumen_reservorio en un 2% para tener en cuenta la evaporación.

5. Resta 2.5e5 metros cúbicos de volumen_reservorio para tener en cuenta el agua que se canaliza a regiones áridas.

6. Imprime el nuevo valor de la variable volumen_reservorio.

**Nota:** Aquí usaremos notación científica para definir grandes números.

Output:

```python
 461771000.0
```

---

## Ejercicio #2

**Nota: Usar archivo e2.py**

Se le proporcionarán datos de ejemplo para un usuario:

- La hora de su visita

- El sitio web al que accedió.

Debe usar las variables proporcionadas y las técnicas que ha aprendido para imprimir un mensaje de registro como este (con el nombre de usuario, la URL y la marca de tiempo reemplazados por valores de las variables apropiadas)

**Output:**

```python
'Ana ingreso al sitio https://petshop.com/pets/reptiles/pythons a las 07:00A.M.'
```

---

## Ejercicio #3

**Nota: Usar archivo e3.py**

Escribe un programa en donde pidas por teclado el nombre y el año de nacimiento de la persona y muestre como resultado el siguiente mensaje:

```python
{nombre} debe cumplir o cumplió {edad} años este año
```

---

## Ejercicio 4

Considere un triángulo de lados `a`, `b` y `c`. Utilizando la formula de Herón el área de triangulo viene dada por la siguiente ecuación:

$$
A = \sqrt{s(s-a)(s-b)(s-c)}
$$

Donde el semiperímetro del triángulo es:

$$
s = \frac{a+b+c}{2}
$$

Realice un programa que reciba las distancias de los 3 lados del triángulo y determine su área utilizando la formula de Herón.

## Ejercicio 5

La ley de Coulomb describe matemáticamente la fuerza eléctrica producida entre dos cargas $q_1$ y $q_2$

$$
\vec{F} = k \frac{q_1q_2}{r^2} \widehat{r}
$$

En donde $k$ es la contaste dieléctrica, $q_1$ y $q_2$ es la magnitud de ambas y $r$ es la distancia que hay entre las cargas.

Realice un programa que solicite los valores de $q_1$, $q_2$ y $r$ para calcular la magnitud de la fuerza.

**Nota:** en el vacío la constante $k$ equivale a `8.85e-12`
