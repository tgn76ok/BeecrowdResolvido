N = int(input())
lista =  list()

def verificarColuna(matriz):
    Total_num = list()
    coluna_valida =0
    for c in range(0, 9):
        for l in range(0, 9):
            if matriz[l][c] not in Total_num:
                Total_num.append(matriz[l][c])
                
        if len(Total_num)==9:
            coluna_valida += 1
            Total_num.clear() 
            
            
    return True if coluna_valida == 9 else False
            
def verificarLinha(matriz) :
    Total_num = list()
    linha_valida=0
    for l in range(0, 9):
        for c in range(0, 9):
            if matriz[l][c] not in Total_num:
                Total_num.append(matriz[l][c])
                
        if len(Total_num)==9:
            linha_valida += 1
            Total_num.clear() 
    return True if linha_valida == 9 else False

def verficarCelula(matriz=None):
    Total_num = list()
    celula_valida=0
    for cellinha in range(0,9,3):

        
        for celcoluna in range(0,9,3):
            for linha in range(cellinha , cellinha+3):
                
                for coluna in range(celcoluna, celcoluna+3):
                    if matriz[linha][coluna] not in Total_num:
                        Total_num.append(matriz[linha][coluna])
                    
            if len(Total_num)==9:
                celula_valida += 1
                Total_num.clear()  
    
    return True if celula_valida == 9 else False
        


for i in range(N):
    
    for l in range(9):
        e = [int(x) for x in str(input()).split()]
        lista.append(e)

    print('Instancia', i+1)

    if verificarColuna(lista) and verficarCelula(lista) and verificarLinha(lista):

        print("SIM")
    else:

        print("NAO")
    print("")
    lista.clear()


