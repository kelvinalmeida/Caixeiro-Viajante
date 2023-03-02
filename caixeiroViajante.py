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

estadoInicial = 'c8'
borda = []
visitados = []
caminhosIniciais = []
caminhosIniciaisNivel2 = []
caminhosIniciaisNivel3 = []
caminho = []

def getPosicao(el):
    elModificado = el[1:]

    return int(elModificado) - 1

# print(add(1))

# print(getPosicao(estadoInicial))

def estaEmVisitados(el):
    # print('&&',visitados)
    # print('&&&&&',el)
    for i in visitados: 
        # print('&&&&&',i)
        if(i == el):
            return True
    else:
        return False

def sucessores(el):
    sucesso = []
    numLinha = getPosicao(el)
    linha = matriz[numLinha]

    for i in range(10):
        if((linha[i] != -1 and linha[i] != 0) and (not estaEmVisitados('c{}'.format(i + 1)))):
            numEl = i + 1
            # print('*', numEl)
            sucesso.append('c{}'.format(numEl))

    if(len(sucesso) != 0):
        return sucesso
    else:
        return -1


def ordenarMelhoresCaminhosInciais(arrSuc, caminhoInicArray,linhaDeverificação):

    for i in range(len(arrSuc)):
        melhor = melhorSuc(arrSuc, linhaDeverificação)

        caminhoInicArray.append(melhor)
        arrSuc.remove(melhor)



def melhorSuc(borda, melhorAnteior):
    indexLinha = getPosicao(melhorAnteior)
    linhaMatriz = matriz[indexLinha]
    melhor = 999
    index = -1

    for j in borda:
        elJ = getPosicao(j)
        if(linhaMatriz[elJ] < melhor):
            melhor = linhaMatriz[elJ]
            index = elJ
    
    return 'c{}'.format(index + 1)


def encontrouCaminho():
    linha = getPosicao(caminho[9])
    linhaMatriz = matriz[linha]

    estInicial = getPosicao(estadoInicial)

    if(linhaMatriz[estInicial] != -1 and linhaMatriz[estInicial] != 0):
        return True
    else:
        return False


def busca():

    borda.append(estadoInicial)
    caminho.append(estadoInicial)
    visitados.append(estadoInicial)
    arrSoc = []
    melhorDosSuce = estadoInicial
    ordenarMelhoresCaminhosInciais(sucessores(estadoInicial),caminhosIniciais, estadoInicial)
    ordenarMelhoresCaminhosInciais(sucessores(caminhosIniciais[0]),caminhosIniciaisNivel2, caminhosIniciais[0])
    ordenarMelhoresCaminhosInciais(sucessores(caminhosIniciaisNivel2[0]), caminhosIniciaisNivel3, caminhosIniciaisNivel2[0])
    segundoMelhor = caminhosIniciais[0]
    terceiroMelhor = caminhosIniciaisNivel3[0]
    nivelDeVarredura = 0

    print()
    print('Estado Inicial:', estadoInicial)
    print('Caminho partindo do estado inicial, passando por todas as cidades até chegar no estado inicial novamente, sem repetir nenhuma cidade:')

    for i in range(120):

        arrSoc = sucessores(borda[len(borda) - 1])

        if(arrSoc != -1):
            
            borda.clear()
            
            # Colocar os suc na borda
            for elSuc in arrSoc:
                borda.append(elSuc)

            melhorDosSuce = melhorSuc(borda, melhorDosSuce)
            
            caminho.append(melhorDosSuce)
            visitados.append(melhorDosSuce)
            borda.clear()
            borda.append(melhorDosSuce)

        elif(nivelDeVarredura == 1):

            if(len(caminho) == 10 and  encontrouCaminho()):
                caminho.append(estadoInicial)
                print(caminho)
                break
            if(len(caminhosIniciaisNivel2) == 0):
                nivelDeVarredura = 2

            borda.clear()
            caminho.clear()
            visitados.clear()

            borda.append(estadoInicial)
            caminho.append(estadoInicial)
            caminho.append(segundoMelhor)
            visitados.append(estadoInicial)
            visitados.append(segundoMelhor)

            if(len(caminhosIniciaisNivel2) != 0):
                borda.append(caminhosIniciaisNivel2[0])
                caminho.append(caminhosIniciaisNivel2[0])
                visitados.append(caminhosIniciaisNivel2[0])
                melhorDosSuce = caminhosIniciaisNivel2[0]

                del caminhosIniciaisNivel2[0]


        elif(nivelDeVarredura == 2):

            if(len(caminho) == 10 and  encontrouCaminho()):
                caminho.append(estadoInicial)
                print(caminho)
                break
            if(len(caminhosIniciaisNivel3) == 0):
                nivelDeVarredura = 3

            borda.clear()
            caminho.clear()
            visitados.clear()

            caminho.append(estadoInicial)
            caminho.append(terceiroMelhor)
            visitados.append(estadoInicial)
            visitados.append(terceiroMelhor)

            if(len(caminhosIniciaisNivel3) != 0):
                borda.append(caminhosIniciaisNivel3[0])
                caminho.append(caminhosIniciaisNivel3[0])
                visitados.append(caminhosIniciaisNivel3[0])
                melhorDosSuce = caminhosIniciaisNivel3[0]

                del caminhosIniciaisNivel3[0]

        else:

            if(len(caminho) == 10 and  encontrouCaminho()):
                caminho.append(estadoInicial)
                print(caminho)
                break
            if(len(caminhosIniciais) == 0):
                nivelDeVarredura = 1

            borda.clear()
            caminho.clear()
            visitados.clear()

            borda.append(estadoInicial)
            caminho.append(estadoInicial)
            visitados.append(estadoInicial)

            if(len(caminhosIniciais) != 0):

                borda.append(caminhosIniciais[0])
                caminho.append(caminhosIniciais[0])
                visitados.append(caminhosIniciais[0])
                melhorDosSuce = caminhosIniciais[0]

                del caminhosIniciais[0]
                

busca()
print()
