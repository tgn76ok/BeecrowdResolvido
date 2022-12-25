N = int(input())
for i in range(N):

    minuto,tempo=  map(str, input().split(' '))
    minuto= int(minuto)
    if tempo[0] == '1':
        if minuto <= 45:
            print(minuto)
        else:
            extra = minuto-45
            print(f"45+{extra}")
    if tempo[0] == '2':
        minuto
        if minuto <= 45:
            print(minuto+45)
        else:
            extra = minuto-45
            print(f"90+{extra}")