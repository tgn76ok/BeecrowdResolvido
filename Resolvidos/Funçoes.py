# 6
# 5 3
# 2 30
# 2 100
# 30 20
# 15 5
# 30 2

T = int(input(""))

for i in range(T):
    
    x, y = map(int,input().split(" "))
    
    num_rafael = pow((3*x),2)+ pow(y,2)
    num_beto = (pow(x,2)*2)+pow((5*y),2)
    num_carlos = -100*x+pow(y,3)
    
    if num_beto > num_carlos and num_beto > num_rafael:       print("Beto ganhou")
    elif num_carlos > num_beto and num_carlos > num_rafael:   print("Carlos ganhou")
    elif num_rafael > num_beto and num_rafael > num_carlos:   print("Rafael ganhou")

        