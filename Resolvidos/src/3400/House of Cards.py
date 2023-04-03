
def bhaskara(a,b,c):
  delta = (b**2) - (4*a*c)
  x1 = (((-1)*b) + (delta**0.5))/(2*a)
  x2 = (((-1)*b) - (delta**0.5))/(2*a)
  if delta == 0:
        return x1
  elif delta > 0:
        return x1,x2

T = int(input())

for i in range(T):
    C = int(input())

    la =bhaskara(3,1,-C*2)#deriva da formula que eu cheiqui pela Progressão Aritmética (PA)  3n^2+n-C*2" 
    valor = int(la[0])
    
    print(valor)