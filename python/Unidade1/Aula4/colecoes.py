#coleções próprias do phyton - possuem funções próprias acessadas por .
#conjuntos - são imutaveis não podem ter valores alterados diferentes dos arrays
conjunto = set([4,7,2,3,0,8])
print("Conjunto: ",conjunto)
#tuplas - também imutavel, podem ser resultados de arquivos e bancos
tupla = (4,7,2,3,0,8)
print("Tupla: ", tupla)
#dicionários - criam lista com uma estrutura indexada, permitindo dados definidos em uma lista com atributos
#ex.:
pessoa = {'nome': 'Mauricio','telefone': '64 555 1234', 'endereco': 'Limoeiros'}
print(pessoa['nome'])

pessoas = [
    {'nome': 'Mauricio','telefone': '64 555 1234', 'endereco': 'Limoeiros'},
    {'nome': 'Milton','telefone': '64 555 3412', 'endereco': 'Laranjal'},
    {'nome': 'Myrna','telefone': '64 555 4321', 'endereco': 'Bananal'},
]

print(pessoas[0]['nome'])