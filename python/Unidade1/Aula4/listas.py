#instância de variável tipo array (inteiro)
numeros = [10,20,30,17]
print(numeros)
print(numeros[0])   #acesso a um elemento do array - o primeiro elemento tem index 0, e os próximos só somar 1

#instância de variável tipo array (string)
carros = ["gol","variant","k","palio","ecosport"] # ou '', tanto faz para string
print(len(carros))        #len - devolve o número de elementos da lista
print('1->',carros)
carros.append('i30')      #função do array que inclui elemento
print('2->',carros)
carros.remove('gol')      #função do array que remove um elemento do array, indicando o valor que o elemento possui
print('3->',carros)
del carros[3]             #remove elemento do array no indice indicado
print('4->',carros)
carros = sorted(carros)  #retorna o array ordenado
print('5->',carros)

for carro in carros: #percorre a lista no lugar do range e armazena os elementos dela no iterador
    print(carro)