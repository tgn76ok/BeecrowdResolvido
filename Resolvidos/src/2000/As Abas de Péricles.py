N, M = map(int, input().split(" "))

for i in range(M):
    acao=input()
    if "fechou" == acao:
        N +=1
    elif "clicou" == acao:
        N-=1
print(N)