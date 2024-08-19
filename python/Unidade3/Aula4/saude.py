#exemplos
#Saude
import numpy as np
import pandas as pd

class Pacientes:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

pacientes = {
    "Paciente 1": Pacientes('Maria', 25, 'F', 60, 1.70),
    "Paciente 2": Pacientes('João', 30, 'M', 80, 1.80),
    "Paciente 3": Pacientes('José', 45, 'M', 70, 1.85),
    "Paciente 4": Pacientes('Ana', 35, 'F', 90, 1.65),
}
#constroi uma lista
l_pacientes = [p.__dict__ for p in pacientes.values()]
#cria um data frame com pandas
df_pacientes = pd.DataFrame.from_records(l_pacientes, index=pacientes.keys())
#inclui um indice através de uma função no data frame
df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis=1)

print(df_pacientes)

media = np.mean(df_pacientes['IMC'])

sobrepeso = df_pacientes[df_pacientes['IMC'] > 25]

percentual = len(sobrepeso) / len(df_pacientes) * 100

print(sobrepeso, " percentual: ", percentual)