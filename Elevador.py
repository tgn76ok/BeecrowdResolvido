import math
L,C,R1,R2,RaioM=1,1,1,1,0
while(True):

    L,C,R1,R2 = [int(x) for x in input().split()]
    if ((L == 0) and (C == 0) and (R1 == 0) and (R2 == 0)):break
    Diame= (R1*2)+(R2*2)
    areaC1= 3.14 * pow(R1,2)
    areaC2= 3.14 * pow(R2,2)
    AreaDosCilisdros = areaC2+areaC1
    areaQuadrado = L*C
    if R1>R2:
        RaioM =R1
    else:
        RaioM =R2


    if((RaioM*2)<=L and (RaioM*2<=C)):
        if L >= Diame or C >= Diame:
            if areaQuadrado > AreaDosCilisdros:
                print("S")
            else:
                print("N")
        else:
            x1,y1 = R1,R1
            x2,y2 = (L-R2),(C-R2)

            resul = math.sqrt((pow(x2-x1,2))+(pow(y2-y1,2)))
            if resul >= R1+R2:
                print("S")
            else:
                print("N")

    else:
        print("N")




#19 10 5 5
#10 19 5 5
#n

#8 9 3 2
#s
#56 70 13 24
#s