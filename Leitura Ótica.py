N = int(input())
for f in range(0,N):
    if N ==0: break
    A, B, C, D, E = map(int, input().split(' '))
    if 0<= A <= B<=C <=D <= E<= 255:
        cont = 0
        if A <= 127:    cont += 1
        if B <= 127:    cont += 1
        if C <= 127:    cont += 1
        if D <= 127:    cont += 1
        if E <= 127:    cont += 1
        if cont == 1:
            if A <= 127:        print("A")
            elif B <= 127:      print("B")
            elif C <= 127:      print("C")
            elif D <= 127:      print("D")
            elif E <= 127:      print("E")
        else:     print('*')