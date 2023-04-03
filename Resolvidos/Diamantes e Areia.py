conta = 0

N = int(input())
for i in range(N):

    resum = str(input()).replace('.','')

    while '<>' in resum:
        resum = resum.replace('<>', '', 1)
        conta += 1

    print(conta)



