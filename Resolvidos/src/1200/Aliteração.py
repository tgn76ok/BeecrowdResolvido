while True:
    try:
        frase = input().lower().split(" ")
        letras = list()
        cont = 0

        for c in range(0,len(frase)-1):
            if frase[c][0:1] == frase[c+1][0:1]:
                cont+=1
            if frase[c][0:1] == frase[c+1][0:1] ==frase[c-1][0:1]:
                cont -=1


        print(cont)

    except EOFError:
        break
