T = int(input(""))
for i in range(T):
    num = [int(x) for x in input().split(" ") ]
    num_jogadores,*num_idades = num
    num_idades.sort()
    print(f'Case {i+1}:',num_idades[(len(num_idades)//2)])



# 2
# 5 19 17 16 14 12
# 5 12 14 16 17 18