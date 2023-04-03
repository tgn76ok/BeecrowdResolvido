lista = list()
lista2 = list()
while True:
    lista.clear()
    lista2.clear()
    N = int(input())
    if N ==0:break
    for i in range(1, N + 1):
        lista.append(i)
    while len(lista)!=1:


        if len(lista)>1:
            valor_na_segunda_casa = lista[1]
            lista.pop(1)
            lista.append(valor_na_segunda_casa)
            lista2.append(lista[0])
            lista.pop(0)

    print(f"Discarded cards:",end=" ")
    for i in range(len(lista2)-1):
        print(lista2[i],end=", ")
    print(f"{lista2[-1]}")
    print(f"Remaining card: {lista[0]}")




