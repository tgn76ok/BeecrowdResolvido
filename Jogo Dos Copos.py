N = int(input())
letra = input()
lugar = letra
if 1 <= N <= 1000:
    for i in range(N):
        num = int(input())
        if num == 1:
            if lugar == 'A':
                lugar = 'B'
            elif lugar == 'B':
                lugar = 'A'

        if num == 2:
            if lugar == 'C':
                lugar = 'B'
            elif lugar == 'B':
                lugar = 'C'

        if num == 3:
            if lugar == 'A':
                lugar = 'C'
            elif lugar == 'C':
                lugar = 'A'
    print(lugar)
