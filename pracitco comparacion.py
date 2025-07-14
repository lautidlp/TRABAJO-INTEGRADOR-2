import random
import time

# Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

# Búsqueda binaria (requiere lista ordenada)
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Tabla Hash
class TablaHash:
    def __init__(self):
        self.tabla = {}

    def insertar(self, clave, valor):
        self.tabla[clave] = valor

    def buscar(self, clave):
        return self.tabla.get(clave, None)

# Crear lista de datos
tamaño_lista = 100000
lista = random.sample(range(1, tamaño_lista * 10), tamaño_lista)
elemento_buscado = random.choice(lista)

# Lista ordenada para la búsqueda binaria
lista_ordenada = sorted(lista)

# Tabla hash con los elementos de la lista
tabla_hash = TablaHash()
for i, valor in enumerate(lista):
    tabla_hash.insertar(valor, i)

# Función para medir tiempos
def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio

# Ejecutar y mostrar resultados
print("🔍 Elemento a buscar:", elemento_buscado)

res_lineal, t_lineal = medir_tiempo(busqueda_lineal, lista, elemento_buscado)
print(f" Búsqueda Lineal: Índice {res_lineal} | Tiempo: {t_lineal:.6f} segundos")

res_binaria, t_binaria = medir_tiempo(busqueda_binaria, lista_ordenada, elemento_buscado)
print(f" Búsqueda Binaria: Índice {res_binaria} | Tiempo: {t_binaria:.6f} segundos")

res_hash, t_hash = medir_tiempo(tabla_hash.buscar, elemento_buscado)
print(f" Búsqueda Hash: Valor {res_hash} | Tiempo: {t_hash:.6f} segundos")
