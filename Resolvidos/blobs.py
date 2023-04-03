N = int(input(''))
cont = 0 
if 1<= N<= 1000:
    for c in range(N):
        C= float(input())
        while True:
            C/=2
            cont+=1
            if C<=1:
                print(f"{cont} dias")
                cont=0
                break
                
else: exit()
    
    #https://github.com/potigol/beecrowd
