import datetime, os
import Calculos
import MonthUpdadte as MU

#V4
payballs = {
    "██████╗  █████╗ ██╗   ██╗██████╗  █████╗ ██╗     ██╗     ███████╗███╗   ███╗ █████╗ ███╗   ██╗\n"    
    "██╔══██╗██╔══██╗ ██╗ ██╔╝██╔══██╗██╔══██╗██║     ██║     ██╔════╝████╗ ████║██╔══██╗████╗  ██║\n"        
    "██████╔╝███████║  ████╔╝ ██████╔╝███████║██║     ██║     ███████╗██╔████╔██║███████║██╔██╗ ██║\n"
    "██╔═══╝ ██╔══██║   ██╔╝  ██╔══██╗██╔══██║██║     ██║     ╚════██║██║╚██╔╝██║██╔══██║██║╚██╗██║\n"
    "██║     ██║  ██║   ██║   ██████╔╝██║  ██║███████╗███████╗███████║██║ ╚═╝ ██║██║  ██║██║ ╚████║\n"
    "╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝"
}

try:
    for p in payballs:
        print(p)
    
    
    conti = 0
    
    #verifica se o arquivo com os gastos está presente
    if not os.path.isfile("Gastos.txt"):
        print("\nArquivo não encontrado - criando nova lista\n")
        #cria um novo arquivo
        MU.StartNewFile()
            
        
        
    while conti == 0:
        print("Digite \"help\" para ver os comandos")
        preco = input("Qualquer quantia de dinheiro -- adiciona os gastos à lista\n")
        
        #enquanto for escolhido qualquer opção que nao seja registrar uma nova compra
        while preco.replace(".", "").isnumeric() == False:
            preco = preco.upper().strip()
            #Mostrar soma de gastos do mes atual
            if "SOMA" in preco:
                print(Calculos.somaMes())
            
            #Mostrar soma de gastos de um mes especifico
            elif "ESPEC" in preco:
                #Caso o usuario cometa o erro de digitar
                #espec {1} ao ives de espec 1
                if "{" in preco[6:]:
                    print("Tente de novo, mas sem \"{}\"")
                #Caso o usuario nao especifique o mes
                elif len(preco.strip()) == 5:
                    print(Calculos.somaMesEspec(input("Qual mês? ")))
                #padrao espec {mes}
                else:
                    print(Calculos.somaMesEspec(preco[6:]))
                
            #Printa uma lista dos gastos do ultimo mes
            elif "PRINT" in preco:
                Calculos.printaMeses(preco)

            #Comando pra printar os comandos
            elif "HELP" in preco:
                print(print("Print -- Mostra os gastos desse mês\nSoma -- Soma os gastos deste mês\nEspec {mes especifico} -- Soma os gastos de um mes especifico"))


            #Comando invalido 
            else:
                print("Comando Invalido")

            #proximo comando
            preco = input()
                
        
    
            
        #A partir daqui é pra registrar uma nova compra
        #descrição doq comprou
        desc = input("Agora o que comprou: ")
        
        #se os centavos nao forem especificados, aqui vai adicionar .00
        if "." not in preco:
            preco = preco + ".00"
        
        #se apenas a casa decimal do centavo for especificado
        #verificando se há 2 caracteres após o "."
        #exemplo: 13.1 --> 13.10
        while len(preco[preco.index("."):]) < 3:
            preco = preco + "0"
        
        #so pra ficar bonito
        complete = "R$ " + str(preco) + " "

        #vai garantir que a descrição sempre vai começar na caractere numero 12
        #falha se gastar 1 milhao ou mais kkkk
        #ele vai digitar "-" 7 vezes, vai digitar um "-" a menos para cada casa decima no preco (contando centavos e o .)
        for i in range(7 - len(preco)):
            complete = complete + "-"
        complete = complete + "- "
        
        complete = complete + desc
        MU.CheckForUpdate()
        with open("Gastos.txt", "a") as file:
            file.write(complete + "\n")

finally:
    print("Finalizou")