import json

pessoas = [
    {'nome': 'Mauricio','telefone': '64 555 1234', 'endereco': 'Limoeiros'},
    {'nome': 'Milton','telefone': '64 555 3412', 'endereco': 'Laranjal'},
    {'nome': 'Myrna','telefone': '64 555 4321', 'endereco': 'Bananal'},
]

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4) 