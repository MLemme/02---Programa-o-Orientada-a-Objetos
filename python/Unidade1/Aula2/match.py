#dia = 4
dia = int(input("Digite o número do dia da semana: "))
#a entrada via teclado é default string o int converte para número
#Estrutura encadeada simples
'''
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
else:
    print("Esse não existe")
''' #comentário de bloco

#Estrutura match ou case
match dia:
    case 1:
       print("Domingo") 
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case other:
        print("Esse não existe")