while True:
    cont1 = cont0 = 0

    N = int(input())
    if N <= 0 or N>10:break

    for i in range(0,N):
        A,B =  map(int, input().split(' '))
        if A>B:
            cont0 += 1
        elif B>A:
            cont1 += 1

    print(f"{cont0} {cont1}")