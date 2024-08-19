n1 = 10
n2 = 4
n3 = 6
n4 = 2

soma = n1 + n2 + n3 + n4
media = soma / 4

#Seleção simples - estrutura de SE ou IF 
if media >= 7: 
    print("Aprovado") #depois dos pontos se há um TAB o coder entende que é faz parte do bloco
    print("Esse print está dentro do IF")

print("Esse print não está dentro do IF")

#Seleção composta
print("A média é: ", media)
if media >= 7: 
    print("Aprovado") 
else: #estrutura SENÂO
    print("Reprovado")


#Seleção encadeada
print("A média é: ", media)
if media >= 7: 
    print("Aprovado") 
elif media < 5: #estrutura SENÃO SE
    print("Reprovado") 
else:
    print("Recuperação")