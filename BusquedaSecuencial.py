

def busqueda_secuencial(lista, valor_buscado):
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i
    return -1

entrada = input("Ingrese una lista de números separados por espacios: ")
lista_numeros = list(map(int, entrada.split()))

numero_buscado = int(input("Ingrese el número que desea buscar: "))

resultado = busqueda_secuencial(lista_numeros, numero_buscado)


if resultado != -1:
    print(f"El número {numero_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El número {numero_buscado} no se encuentra en la lista.")