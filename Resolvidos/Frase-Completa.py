Letras = set()
frase = list()
N = int(input())
for i in range(0,N):
    frase.append(input())
    for letras in frase[i]:
        if letras not in ',!?(){}[] ':
            Letras.add(letras)

    if len(Letras) == 26:
        print("frase completa")

    elif 25 >= len(Letras) >= 13:
        print("frase quase completa")

    else:
        print("frase mal elaborada")