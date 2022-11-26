N = int(input())
resul = 0
if 1 < N < 60:
    for i in range(N):
        nome = str(input())
        notas = [float(x) for x in input().split()]
        if len(notas) == 1:
            resul = notas[0] / 2
        elif len(notas) == 2:
            resul = (notas[0] + notas[1]) / 2
        elif len(notas) == 3:
            resul = (notas[0] + notas[1] + notas[2]) / 3
        elif len(notas) == 4:
            if notas[0] > notas[1] and notas[2] > notas[1] and notas[3] > notas[1]:
                notas[1] = notas[-1]
                notas.pop(3)
            elif notas[0] < notas[1] and notas[0] < notas[2] and notas[3] > notas[0]:
                notas[0] = notas[-1]
                notas.pop(3)
            elif notas[2] < notas[1] and notas[2] < notas[0] and notas[3] > notas[2]:
                notas[2] = notas[-1]
                notas.pop(3)
            else:
                resul = (notas[0] + notas[1] + notas[2]) / 3

            resul = (notas[0] + notas[1] + notas[2]) / 3

        print("{}: {:.1f}".format(nome, resul))
