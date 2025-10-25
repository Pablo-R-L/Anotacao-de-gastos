import datetime


MesesDoAno = {
    1 : "Jan",
    2 : "Feb",
    3 : "Mar",
    4 : "Abr",
    5 : "Mai",
    6 : "Jun",
    7 : "Jul",
    8 : "Ago",
    9 : "Sep",
    10 : "Out",
    11 : "Nov",
    12 : "Dez"
}


def CheckForUpdate():
    with open("Gastos.txt", "r") as file:
        gastos = list(file)
   
   #pega o numero do mes atual
    mesAtual = MesesDoAno[int(datetime.datetime.now().month)]
    

    #procura no arquivo de tras pra frente
    #pra pegar o ultimo mes registrado no arquivo
    for i in range(len(gastos)-1, -1, -1):
        #se a linha começa com "-" quer dizer que a linha que informa o mes
        if gastos[i][0] == "-":
            #se o ultimo mes registrado for o mes atual, ok, se não, atualiza
            if mesAtual in gastos[i][4:7]:
                return(0)
            else: 
                with open("Gastos.txt", "a") as file:
                    file.write("\n\n----" + mesAtual + "----\n")
                return(1)


def StartNewFile():
    #pega o numero do mes atual
    mesAtual = MesesDoAno[int(datetime.datetime.now().month)]

    with open("Gastos.txt", "w") as file:
        file.write("----" + mesAtual + "----\n")