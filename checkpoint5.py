# 1
# Un bucle for que imprime los números del 0 al 4
for i in range(5):
    print(f"Estamos en la iteración: {i}")

# 2
def suma(a, b, c):
    return a + b + c

# Ejemplo de uso:
resultado_funcion = suma(10, 20, 30)
print(f"Resultado de la función suma: {resultado_funcion}")

# 3
suma_lambda = lambda a, b, c: a + b + c

# Ejemplo de uso:
resultado_lambda = suma_lambda(10, 20, 30)
print(f"Resultado de la lambda: {resultado_lambda}")

# 4
nombre = 'Enrique'
# Definimos la colección (en este caso una lista)
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

# Verificamos si 'Enrique' está en la lista
if nombre in lista_nombre:
    print(f"Éxito: {nombre} se encuentra en la lista.")
else:
    print(f"Aviso: {nombre} no coincide con ningún valor de la lista.")