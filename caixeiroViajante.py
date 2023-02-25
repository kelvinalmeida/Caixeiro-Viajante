matriz = [[0, 30, 84, 56, -1, -1, -1, 75, -1, 80],
[30, 0, 65, -1, -1, -1, 70, -1, -1, 40],
[84, 65, 0, 74, 52, 55, -1, 60, 143, 48],
[56, -1, 74, 0, 135, -1, -1, 20, -1, -1],
[-1, -1, 52, 135, 0, 70, -1, 122, 98, 80],
[70, -1, 55, -1, 70, 0, 63, -1, 82, 35],
[-1, 70, -1, -1, -1, 63, 0, -1, 120, 57],
[75, -1, 135, 20, 122, -1, -1, 0, -1, -1],
[-1, -1, 143, -1, 98, 82, 120, -1, 0, -1],
[80, 40, 48, -1, 80, 35, 57, -1, -1, 0]]

estadoInicial = 'c1'
borda = []
visitados = []

def getPosicao(el):
    return int(el[1]) - 1

# print(add(1))

# print(getPosicao(estadoInicial))

def sucessores(el):
    sucesso = []
    numLinha = getPosicao(el)
    linha = matriz[numLinha]

    for i in range(10):
        if(linha[i] != -1 and linha[i] != 0):
            numEl = i + 1
            sucesso.append('c{}'.format(numEl))

    return sucesso

# print(sucessores(estadoInicial))

def busca():

    borda.append(estadoInicial)

    # while 1 != 0:
    for i in range(10):
        # soc = sucessores(borda[len(borda) - 1])
        numEl = i + 1
        soc = sucessores('c{}'.format(numEl))
        print(soc)

busca()