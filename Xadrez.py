L = int(input())
C = int(input())

if (L %2 == 0 and C%2==0) or  (L %2 != 0 and C%2!=0):
    print(1)
else:
    print(0)


#
#c=0
#for linha in range(L):
#    for coluna in range(C):
#        if coluna % 2 ==0:
#            c+=1
#            print(c)
#        else:
#            c-=1
