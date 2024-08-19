
n3 = 7 #variavel fora da função, escopo global

def soma(n1,n2):
    print('Função soma n1:', n1) #variavel existente apenas no escopo da função
    print('Função soma n2:', n2)
    print('Função soma n3:', n3) #acessou aqui mas pertence ao escopo global
    resultado = n1 + n2
    #print(f"O resultado da divisão é {resultado}")
    #print(f'{n1} / {n2} = {resultado}')
    return resultado

soma(5,8)