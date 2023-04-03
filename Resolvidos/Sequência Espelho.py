C=int(input())
for i in range(0,C):
    ini,fim = map(int, input().split(" "))
    if 1<=ini<=fim<=12221:
        for i in range(ini,fim+1):
            print(f"{i}",end="")
        for c in range(fim,ini-1,-1):
            print(f"{c}",end="")
