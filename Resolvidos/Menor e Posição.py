N = int(input())
menor = 0
pos= 0

if 1<N<1000:
    e = [int(x) for x in str(input()).split()]

    for i in range(len(e)-1):
        if i == 0:
            menor = e[i]
        if menor > e[i]:
            menor = e[i]
            pos = i

print(f'''Menor valor: {menor}
Posicao: {pos}''')