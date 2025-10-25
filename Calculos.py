import MonthUpdadte as MU



def somaMes():
    with open("Gastos.txt", "r") as file:
        gastos = list(file)
    
    total = 0
    #Vai ler a lista de traz pra frente ate encontrar
    #a primeira linha que indica o mes
    primeiraLinha = 0
    for line in range(len(gastos)-1, -1, -1):
        if gastos[line][0] in "-":
            primeiraLinha = int(line)
            break
    
    #Agora vai começar a ler a partir da linha encontrada no loop anterior

    for line in gastos[primeiraLinha+1:]:
        #verifica se a linha mostra um gasto ou um investimento
        if "R" in line[0]:
            #Nas linhas de gasto, a divisao entre o preço e a descrição é -
            #Entao aqui pega a linha inteira ate -
            gasto = line[3: line.index("-")if "-" in line else -1].strip()
            #Vai verificar se o valor foi extraido corretamente
            if gasto.replace(".", "").isnumeric():
                total = total + (float(gasto.replace(".", ""))/100)
    
   

    return(total)



def somaMesEspec(mes):
    with open("Gastos.txt", "r") as file:
        gastos = list(file)
    meses = MU.MesesDoAno

    #checa se o mes é valido
    #primeiro checa se o input é por nome ou por numero do mes
    if mes.isnumeric():
        #procura o mes por numero
        if int(mes) not in meses:
            return "Mes invalido"
        else:
            mes = meses[int(mes)]
    else:
        #procura o meus por nome
        mesCheck = False
        mes = mes.capitalize()
        for i in meses:
            #procurar assim torna valido caso o input seja Janeiro ao inves de Jan
            if meses[i] in mes:
                mesCheck = True
                break
        if not mesCheck:
            return "Mes invalido"
    
    #total de gastos somado         
    total = 0
    print(mes)
    for line in range(len(gastos)):
        #chegou no mes atual
        if gastos[line][0] in "-" and mes in gastos[line]:
            #Nas linhas de gasto, a divisao entre o preço e a descrição é -
            #Entao aqui pega a linha inteira ate -
            l = line+1
            gasto = gastos[l]
            gasto = gasto[3: gasto.index("-")if "-" in gastos[l] else -1].strip()
            
            #Vai verificar se o valor foi extraido corretamente
            #se o valor nao for valido, significa que chegou no proximo mes
            while(gasto.replace(".", "").isnumeric()):
                total += (float(gasto.replace(".", ""))/100)
                #proxima linha
                l += 1
                if l >= len(gastos): break
                gasto = gastos[l]
                gasto = gasto[3: gasto.index("-")if "-" in gastos[l] else -1].strip()
                
                
            break

    return(total)


def printaMeses(preco):
    meses = MU.MesesDoAno
    with open("Gastos.txt", "r") as file:
        gastos = list(file)

    #print {mes}
    if len(preco) > 5:

        if preco[6:].isnumeric():
            preco = preco.replace(preco[6:], meses[int(preco[6:])])

        #se o print for de um mes especifico
        for i in range(len(gastos)):
            if gastos[i][0] == "-" and preco[6:9].capitalize() in gastos[i]:
                print(gastos[i][:-1]) 
                for x in gastos[i+1:]:
                    if x[0] != "R":
                        break
                    print(x[:-1])
                break
    
    else:
        #se o print for desse mes
        for i in range(1, len(gastos) + 1):
            #Le o arquivo de tras pra frente até encontrar o começo do ultimo mes
            if gastos[-i][0] in "-":
                #Começa outro loop que vai dessa linha até o fim
                for x in gastos[-i+1:]:
                        #a ultima caractere é \n ent o :-1 é pra n dar mais espaço doq precisa
                        print(x[:-1])
                break
    return(1)
    




