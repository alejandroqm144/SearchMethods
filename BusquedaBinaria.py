

def busqueda_binaria(lista, valor_buscado):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor_buscado:
            return medio
        elif lista[medio] < valor_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

entrada = input("Ingrese una lista ordenada de números separados por espacios: ")
lista_numeros = list(map(int, entrada.split()))

numero_buscado = int(input("Ingrese el número que desea buscar: "))

resultado = busqueda_binaria(lista_numeros, numero_buscado)

if resultado != -1:
    print(f"El número {numero_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El número {numero_buscado} no se encuentra en la lista.")
