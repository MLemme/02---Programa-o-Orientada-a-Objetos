#função anônima, lambda function ou função sem nome
numeros = [4, 8 , 9, 3]
'''
resultado = []
for n in numeros 
    resultado.append(n*2)

print(numeros, resultado)

def multiplicar(n1)
    return n1 * 2
'''
#o termo lambda indicará para a IDE que é uma função sem nome
                #entrada  execução
resultado = map(lambda n: n * 3, numeros) #map é uma função que executa algo para algum elemento da lista, sendo função explicita ou anonima
print(numeros, list(resultado))