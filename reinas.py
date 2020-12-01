key = 0
actividad=[]
matriz =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

posiciones = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def entrada(reinas, matriz, key,posiciones):
    print("Reinas => "+str(reinas))

    cnt = 0
    play = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if reinas == 1:
        return res(matriz)
    else: 
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                #print(r)
                if cnt == 0:
                    if posiciones[i][j] != 3:
                        if(matriz[i][j] == 0):
                            if reinas == 4:
                                posiciones[i][j] = 3
                            matriz[i][j] = 1
                            cnt = cnt + 1
                            actividad.append([i,j])
        #print(actividad)
        matriz = iterar(matriz,actividad)

        actividad.pop(0)
        for i in matriz:
            if 0 in i:
                key = 0
            else:
                key = 1
        if key == 1:
            print(key)
            for i in play:
                print(i)
            reinas = 4
            key=0
            return entrada(reinas,play,key,posiciones)
        if key == 0:
            print(key)
            reinas=reinas-1
            return entrada(reinas,matriz,key,posiciones)

def iterar(matriz,actividad):
    print("H => V")
    act = actividad[0][0]
    b = actividad[0][1]
    r = range(len(matriz))
    mov = b
    movim = act
    print(actividad)

    for i in range(len(matriz)):
        for r in range(len(matriz[i])):
            matriz[act][r] = 2
            matriz[i][b] = 2
    imprimir(matriz)
    for i in range(len(matriz)):
        mov = mov-1
        movim = movim -1
        if (mov >= 0)and(movim >=0):
            print("- -")
            matriz[movim][mov] = 2
    mov = b
    movim = act
    imprimir(matriz)
    for i in range(len(matriz)):
        movim = movim +1
        mov = mov +1
        if (movim <= r)and(mov <= r):
            print("+ +")
            matriz[movim][mov] = 2

    mov = b
    movim = act
    imprimir(matriz)
    for i in range(len(matriz)):
        mov = mov+1
        movim = movim -1
        if (mov < r)and(movim >=0):
            print("+ -")
            matriz[movim][mov] = 2
    mov = b
    movim = act
    imprimir(matriz)
    for i in range(len(matriz)):
        mov = mov-1
        movim = movim + 1
        if (mov >= 0)and(movim <r):
            print("- +")
            matriz[movim][mov] = 2
    matriz[act][b]=1
    imprimir(matriz)
    print()
    return matriz
def imprimir(matriz):
    for i in matriz:
        print(i)
def res(matriz):
    for i in range(len(matriz)):
        for r in range(len(matriz[i])):
            if (matriz[i][r]) == 0:
                 matriz[i][r] = 1
    for i in matriz:
        print(i)
entrada(4,matriz,0,posiciones)