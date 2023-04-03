numeros = list()
l=0
for i in range(0, 20):
    numeros.append(int(input()))

for c in range(len(numeros)-1, -1, -1):
    print(f"N[{l}] = {numeros[c]}")
    l += 1