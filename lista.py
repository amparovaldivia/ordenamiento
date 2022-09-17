def ordenamiento(lista):

    for numero in range(0, len(lista)):

        for numero2 in range(len(lista)-1-numero):
            if lista[numero2] > lista[numero2+1]:
                temp = lista[numero2]
                lista[numero2] = lista[numero2+1]
                lista[numero2+1] = temp
    return lista


lista = [8, 9, 5, 6, 2, 3, 7, 0, 1, 4]
lista=ordenamiento(lista)
print(lista)
