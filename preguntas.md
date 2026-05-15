

# 🔹 ¿Qué es un Condicional?

Un **condicional** es una estructura que permite que el programa tome decisiones dependiendo de si una condición es verdadera o falsa.

## 📌 ¿Para qué sirve?

Los condicionales sirven para:

- Ejecutar diferentes acciones según una condición.
- Validar datos.
- Controlar el flujo del programa.
- Crear lógica dentro de una aplicación.

---

# 🧠 Sintaxis de un Condicional

```python
if condicion:
    # código a ejecutar
```

---

# 🔹 Ejemplo Básico

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

## ✅ Explicación

- `if` significa "si".
- `edad >= 18` es la condición.
- Si la condición es verdadera, se ejecuta el bloque de código.

---

# 🔹 Condicional con else

```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## ✅ Explicación

- `else` significa "si no".
- Se ejecuta cuando la condición del `if` es falsa.

---

# 🔹 Condicional con elif

```python
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

## ✅ Explicación

- `elif` significa "si no, pero si..."
- Permite evaluar múltiples condiciones.

---

# 📌 Operadores de Comparación

| Operador | Significado |
|---|---|
| `==` | Igual que |
| `!=` | Diferente |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |

---

# 🔹 ¿Qué son los Bucles en Python?

Los **bucles** permiten repetir un bloque de código varias veces sin necesidad de escribirlo repetidamente.

## 📌 ¿Por qué son útiles?

Porque ayudan a:

- Automatizar tareas repetitivas.
- Recorrer listas o datos.
- Ahorrar tiempo y código.
- Crear programas más eficientes.

---

# 🔄 Tipos de Bucles en Python

Python tiene principalmente dos tipos de bucles:

1. `for`
2. `while`

---

# 🔹 Bucle FOR

El bucle `for` se utiliza para recorrer elementos de una secuencia.

## 📌 Sintaxis

```python
for variable in secuencia:
    # código
```

---

# 🔹 Ejemplo de FOR

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

---

# 🔹 FOR con range()

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

## 📌 Explicación

`range(5)` genera números del 0 al 4.

---

# 🔹 Bucle WHILE

El bucle `while` ejecuta código mientras una condición sea verdadera.

## 📌 Sintaxis

```python
while condicion:
    # código
```

---

# 🔹 Ejemplo de WHILE

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

# ⚠️ Importante

Si la condición nunca cambia, el bucle puede volverse infinito.

❌ Ejemplo incorrecto:

```python
while True:
    print("Hola")
```

---

# 🔹 ¿Qué es una Lista por Comprensión?

Las **listas por comprensión** permiten crear listas de forma rápida y elegante en una sola línea.

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

# ✅ Ventajas

- Código más corto.
- Más legible.
- Más rápido en muchos casos.

---

# 🔹 Lista por Comprensión con Condición

```python
pares = [n for n in range(10) if n % 2 == 0]

print(pares)
```

## ✅ Resultado

```python
[0, 2, 4, 6, 8]
```

---

# 🔹 ¿Qué es un Argumento en Python?

Un **argumento** es un valor que se envía a una función cuando se llama.

---

# 📌 Ejemplo Básico

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Carlos")
```

## ✅ Explicación

- `nombre` es un parámetro.
- `"Carlos"` es el argumento enviado.

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

# 🔹 ¿Qué es una Función Lambda?

Una función **lambda** es una función pequeña y anónima creada en una sola línea.

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

# 📌 ¿Para qué sirven las Lambdas?

Se usan principalmente para:

- Funciones cortas.
- Operaciones rápidas.
- Trabajar con `map()`, `filter()` y `sorted()`.

---

# 🔹 Ejemplo con sorted()

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

# 🔹 ¿Qué es un paquete pip?

`pip` es el administrador de paquetes oficial de Python.

Permite instalar librerías externas creadas por otros desarrolladores.

---

# 📌 ¿Para qué sirve?

Con `pip` puedes:

- Instalar librerías.
- Actualizar paquetes.
- Eliminar paquetes.
- Gestionar dependencias.

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
