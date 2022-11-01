O = input().upper()
soma= cont = num = 0

for l in range(12):
    for c in range(12):
        num = float(input())
        if l < c and l+c >= 12:
            soma+=num
            cont +=1

if O == 'S': print(f'{soma:.1f}')
else: print(f'{(soma / cont):.1f}')