#tratamento de erros
'''
try:
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))

    resultado = n1/n2

    print(f"O resultado da divisão é {resultado}")

except Exception as erro: #para tratamentos genéricos
    print(f"Ocorreu um erro: {erro}")
'''
try:
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))

    resultado = n1/n2

    print(f"O resultado da divisão é {resultado}")
#para tratamentos específicos
except ValueError: 
    print("Favor digitar somente números")
except ZeroDivisionError:
    print("Não é possível dividir o número por 0")
#para tratamentos genéricos
except Exception as erro: #para tratamentos genéricos
    print(f"Ocorreu um erro: {erro}")
#executa caso de sucesso, sem ocorrência de erros
else:
    print("O programa foi executado corretamente")
#executa indepente de ocorrência ou não do erro
finally:
    print("FIM")