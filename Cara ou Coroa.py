while True:
    cont1 = cont0 = 0

    N = int(input())
    if N == 0:break
    for i in range(0,N):
        pass
    e = [int(x) for x in str(input()).split()]
    for j in e:
        if j == 0:     cont0 += 1
        elif j == 1:   cont1 +=1

    print(f"Mary won {cont0} times and John won {cont1} times")
