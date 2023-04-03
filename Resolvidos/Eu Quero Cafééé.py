N, L, D = map(int, input().split(' '))

nesecesario = N * D
L = L * 1000
usual = L

cont = 1
if N >= 1:
    while True:
        if nesecesario <= L:
            cont = 1
        elif nesecesario > L:
            print(usual,nesecesario,cont)

            usual += L
            cont += 1
            print(usual,nesecesario,cont)
        if usual >= nesecesario: break

print(cont * (L // 1000))
