

tabla_hash = {}

def calcular_hash(numero):
    return hash(numero)

def agregar_elemento(tabla, clave):
    tabla[calcular_hash(clave)] = clave

def buscar_elemento(tabla, clave):
    hash_clave = calcular_hash(clave)
    return tabla.get(hash_clave, None)

numeros = [23, 42, 56, 78, 99, 12, 45]

for numero in numeros:
    agregar_elemento(tabla_hash, numero)

print(buscar_elemento(tabla_hash, 42))
print(buscar_elemento(tabla_hash, 100))
