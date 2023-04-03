N, M = map(float, input().split(" "))

resul = ((1 + N / 100) * (1 + M / 100) - 1) * 100
print("{:.6f}".format(resul))