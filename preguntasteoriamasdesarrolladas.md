# 🔹 ¿Qué es un Condicional en Python?

Un **condicional** es una estructura de control que permite que un programa tome decisiones dependiendo de si una condición se cumple o no.

Gracias a los condicionales, los programas pueden comportarse de manera diferente según los datos recibidos o las acciones del usuario.

---

# 📌 ¿Para qué sirven los condicionales?

Los condicionales son fundamentales en programación porque permiten:

- Ejecutar acciones diferentes según una situación.
- Validar información ingresada por el usuario.
- Controlar el flujo de ejecución del programa.
- Crear lógica y automatización.
- Evitar errores comprobando condiciones antes de ejecutar código.

---

# 🧠 Sintaxis Básica de un Condicional

```python
if condicion:
    # código a ejecutar
```

## ✅ Explicación

- `if` significa **"si"**.
- `condicion` es una expresión que puede ser:
  - Verdadera (`True`)
  - Falsa (`False`)
- Los dos puntos `:` indican el inicio del bloque de código.
- La indentación es obligatoria en Python.

---

# 🔹 Ejemplo Básico

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

## ✅ ¿Qué ocurre aquí?

1. La variable `edad` almacena el valor `18`.
2. Python evalúa la condición:

```python
edad >= 18
```

3. Como la condición es verdadera, se ejecuta:

```python
print("Eres mayor de edad")
```

---

# 🔹 Uso de else

La palabra `else` permite ejecutar código cuando la condición del `if` es falsa.

---

# 📌 Sintaxis

```python
if condicion:
    # código si es verdadero
else:
    # código si es falso
```

---

# 🔹 Ejemplo con else

```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## ✅ Explicación

- Si la edad es mayor o igual a 18:
  - Se muestra `"Eres mayor de edad"`
- En caso contrario:
  - Se ejecuta `else`

---

# 🔹 Uso de elif

`elif` significa:

> “si no, pero si…”

Permite evaluar múltiples condiciones en orden.

---

# 📌 Sintaxis

```python
if condicion1:
    # código
elif condicion2:
    # código
else:
    # código final
```

---

# 🔹 Ejemplo con elif

```python
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

## ✅ Explicación Paso a Paso

- Python revisa si `nota >= 90`
  - Es falso.
- Luego revisa `nota >= 70`
  - Es verdadero.
- Entonces imprime:

```python
Aprobado
```

---

# 📌 Operadores de Comparación

Los operadores de comparación permiten comparar valores.

| Operador | Significado | Ejemplo |
|---|---|---|
| `==` | Igual que | `a == b` |
| `!=` | Diferente | `a != b` |
| `>` | Mayor que | `a > b` |
| `<` | Menor que | `a < b` |
| `>=` | Mayor o igual | `a >= b` |
| `<=` | Menor o igual | `a <= b` |

---

# 🔹 Operadores Lógicos

También existen operadores lógicos para combinar condiciones.

| Operador | Significado |
|---|---|
| `and` | Ambas condiciones deben cumplirse |
| `or` | Al menos una debe cumplirse |
| `not` | Niega la condición |

---

# 🔹 Ejemplo con Operadores Lógicos

```python
edad = 20
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puedes entrar")
```

---

# 🔹 Condicionales Anidados

Un condicional puede estar dentro de otro.

```python
edad = 25

if edad >= 18:
    print("Eres adulto")

    if edad >= 60:
        print("Además eres adulto mayor")
```

---

# ⚠️ Errores Comunes

## ❌ Olvidar la indentación

```python
if True:
print("Hola")
```

✅ Correcto:

```python
if True:
    print("Hola")
```

---

## ❌ Usar `=` en lugar de `==`

```python
if edad = 18:
```

✅ Correcto:

```python
if edad == 18:
```

---

# 🧠 Resumen

Los condicionales permiten que un programa:

- Tome decisiones.
- Ejecute diferentes acciones.
- Evalúe situaciones.
- Controle el comportamiento del código.

Son una de las bases más importantes de la programación.

---

# 🔹 ¿Qué son los Bucles en Python?

Los **bucles** o **loops** permiten repetir un bloque de código varias veces automáticamente.

Sin los bucles, tendríamos que escribir el mismo código muchas veces.

---

# 📌 ¿Para qué sirven los bucles?

Los bucles son útiles para:

- Automatizar tareas repetitivas.
- Recorrer listas y colecciones.
- Procesar datos.
- Repetir acciones hasta cumplir una condición.
- Crear algoritmos más eficientes.

---

# 🔄 Tipos de Bucles en Python

Python tiene dos tipos principales de bucles:

1. `for`
2. `while`

---

# 🔹 Bucle FOR

El bucle `for` se utiliza para recorrer elementos de una secuencia.

Puede recorrer:

- Listas
- Tuplas
- Strings
- Diccionarios
- Rangos numéricos

---

# 📌 Sintaxis

```python
for variable in secuencia:
    # código
```

---

# 🔹 Ejemplo Básico

```python
frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)
```

## ✅ Resultado

```python
manzana
pera
uva
```

## ✅ Explicación

- `fruta` toma el valor de cada elemento.
- El ciclo se repite automáticamente.

---

# 🔹 FOR con range()

La función `range()` genera secuencias numéricas.

---

# 📌 Ejemplo

```python
for numero in range(5):
    print(numero)
```

## ✅ Resultado

```python
0
1
2
3
4
```

## ✅ Explicación

```python
range(5)
```

Genera números desde `0` hasta `4`.

---

# 🔹 range(inicio, fin, salto)

```python
for numero in range(1, 10, 2):
    print(numero)
```

## ✅ Resultado

```python
1
3
5
7
9
```

---

# 🔹 Recorrer Strings

```python
for letra in "Python":
    print(letra)
```

---

# 🔹 Bucle WHILE

El bucle `while` repite código mientras una condición sea verdadera.

---

# 📌 Sintaxis

```python
while condicion:
    # código
```

---

# 🔹 Ejemplo Básico

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

## ✅ Resultado

```python
1
2
3
4
5
```

---

# 🔹 ¿Qué significa `contador += 1`?

Es una forma abreviada de escribir:

```python
contador = contador + 1
```

Sirve para incrementar el valor.

---

# ⚠️ Bucles Infinitos

Si la condición nunca cambia, el bucle jamás terminará.

---

# ❌ Ejemplo Incorrecto

```python
while True:
    print("Hola")
```

Este código se ejecutará infinitamente.

---

# 🔹 Uso de break

`break` permite salir inmediatamente de un bucle.

```python
while True:
    texto = input("Escribe salir: ")

    if texto == "salir":
        break
```

---

# 🔹 Uso de continue

`continue` salta la iteración actual.

```python
for numero in range(5):

    if numero == 2:
        continue

    print(numero)
```

## ✅ Resultado

```python
0
1
3
4
```

---

# 🧠 Resumen de Bucles

| Bucle | Uso Principal |
|---|---|
| `for` | Recorrer elementos |
| `while` | Repetir mientras se cumpla una condición |

---

# 🔹 ¿Qué es una Lista por Comprensión?

Las listas por comprensión son una forma compacta y elegante de crear listas en Python.

Permiten escribir menos código y hacerlo más legible.

---

# 📌 Sintaxis

```python
[expresion for elemento in iterable]
```

---

# 🔹 Ejemplo Básico

```python
numeros = [1, 2, 3, 4, 5]

cuadrados = [n ** 2 for n in numeros]

print(cuadrados)
```

## ✅ Resultado

```python
[1, 4, 9, 16, 25]
```

---

# 🔹 ¿Qué ocurre aquí?

- `n` toma cada valor de `numeros`.
- `n ** 2` calcula el cuadrado.
- Se crea una nueva lista automáticamente.

---

# 🔹 Lista Tradicional vs Comprensión

## ❌ Forma tradicional

```python
cuadrados = []

for n in numeros:
    cuadrados.append(n ** 2)
```

---

## ✅ Con comprensión

```python
cuadrados = [n ** 2 for n in numeros]
```

Mucho más corto y limpio.

---

# 🔹 Comprensión con Condición

```python
pares = [n for n in range(10) if n % 2 == 0]

print(pares)
```

## ✅ Resultado

```python
[0, 2, 4, 6, 8]
```

---

# 🔹 Explicación

La condición:

```python
if n % 2 == 0
```

permite agregar solamente números pares.

---

# 🔹 Comprensión con Strings

```python
palabras = ["python", "java", "c"]

mayusculas = [p.upper() for p in palabras]

print(mayusculas)
```

---

# 🧠 Ventajas

- Código más corto.
- Mejor legibilidad.
- Mayor eficiencia.
- Fácil de escribir.

---

# 🔹 ¿Qué es un Argumento en Python?

Un argumento es un valor enviado a una función cuando se ejecuta.

Las funciones pueden recibir datos para trabajar con ellos.

---

# 📌 Ejemplo Básico

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Carlos")
```

---

# ✅ Explicación

- `nombre` es un parámetro.
- `"Carlos"` es el argumento.

---

# 🔹 Parámetro vs Argumento

| Concepto | Descripción |
|---|---|
| Parámetro | Variable definida en la función |
| Argumento | Valor enviado a la función |

---

# 🔹 Tipos de Argumentos

## 1️⃣ Argumentos Posicionales

```python
def suma(a, b):
    print(a + b)

suma(5, 3)
```

---

## 2️⃣ Argumentos por Nombre

```python
def persona(nombre, edad):
    print(nombre, edad)

persona(edad=20, nombre="Ana")
```

---

## 3️⃣ Argumentos por Defecto

```python
def saludar(nombre="Invitado"):
    print("Hola", nombre)

saludar()
```

---

# 🔹 Argumentos Variables

## 📌 *args

```python
def suma(*numeros):
    print(sum(numeros))

suma(1, 2, 3, 4)
```

---

## 📌 **kwargs

```python
def mostrar(**datos):
    print(datos)

mostrar(nombre="Ana", edad=20)
```

---

# 🔹 ¿Qué es una Función Lambda?

Las funciones lambda son funciones pequeñas y anónimas definidas en una sola línea.

---

# 📌 Sintaxis

```python
lambda argumentos: expresion
```

---

# 🔹 Ejemplo Básico

```python
suma = lambda a, b: a + b

print(suma(5, 3))
```

## ✅ Resultado

```python
8
```

---

# 🔹 Equivalente con Función Normal

```python
def suma(a, b):
    return a + b
```

---

# 🔹 ¿Cuándo usar Lambda?

Son útiles cuando:

- La función es muy corta.
- Se usa temporalmente.
- Se necesita una función rápida.

---

# 🔹 Lambda con map()

```python
numeros = [1, 2, 3]

dobles = list(map(lambda n: n * 2, numeros))

print(dobles)
```

---

# 🔹 Lambda con filter()

```python
numeros = [1, 2, 3, 4, 5]

pares = list(filter(lambda n: n % 2 == 0, numeros))

print(pares)
```

---

# 🔹 Lambda con sorted()

```python
personas = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 18},
    {"nombre": "Carlos", "edad": 25}
]

ordenadas = sorted(personas, key=lambda p: p["edad"])

print(ordenadas)
```

---

# 🧠 Ventajas de Lambda

- Código compacto.
- Ideal para funciones pequeñas.
- Muy útil con funciones integradas.

---

# 🔹 ¿Qué es pip en Python?

`pip` es el gestor oficial de paquetes de Python.

Permite instalar librerías desarrolladas por otros programadores.

---

# 📌 ¿Qué es una librería?

Una librería es un conjunto de herramientas y funciones ya creadas que podemos reutilizar.

---

# 🔹 ¿Para qué sirve pip?

Con `pip` puedes:

- Instalar paquetes.
- Actualizar librerías.
- Eliminar paquetes.
- Administrar dependencias.

---

# 🔹 Instalar un Paquete

```bash
pip install requests
```

---

# 🔹 Ejemplo Real

```python
import requests

respuesta = requests.get("https://api.github.com")

print(respuesta.status_code)
```

---

# 🔹 Ver Paquetes Instalados

```bash
pip list
```

---

# 🔹 Actualizar un Paquete

```bash
pip install --upgrade requests
```

---

# 🔹 Desinstalar un Paquete

```bash
pip uninstall requests
```

---

# 🔹 Instalar una Versión Específica

```bash
pip install requests==2.31.0
```

---

# 🔹 Archivo requirements.txt

Se utiliza para guardar dependencias de un proyecto.

## 📌 Crear archivo

```bash
pip freeze > requirements.txt
```

## 📌 Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 🧠 Buenas Prácticas con pip

- Usar entornos virtuales (`venv`)
- Mantener librerías actualizadas
- Instalar solo lo necesario
- Usar `requirements.txt`

---

# 🎯 Conclusión General

Todos estos conceptos forman parte de las bases fundamentales de Python:

- Los **condicionales** permiten tomar decisiones.
- Los **bucles** automatizan tareas repetitivas.
- Las **listas por comprensión** simplifican la creación de listas.
- Los **argumentos** permiten enviar información a funciones.
- Las **funciones lambda** ayudan a escribir funciones rápidas.
- `pip` permite ampliar las capacidades de Python instalando librerías externas.

Dominar estos temas es esencial para avanzar hacia proyectos más complejos y convertirte en un desarrollador Python más sólido.