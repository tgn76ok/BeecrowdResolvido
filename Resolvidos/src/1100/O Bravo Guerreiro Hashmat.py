

while True:
    try:
        num_aliado, num_inimigo  = input("").split(" ")
        num_aliado= int(num_aliado);num_inimigo= int(num_inimigo)
        resul = num_inimigo-num_aliado if num_aliado<= num_inimigo else num_aliado-num_inimigo
        print(resul)
    except EOFError :
        break
    