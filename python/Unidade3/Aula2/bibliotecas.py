import math #matematica
import random #numeros aleatorios
import numpy as np #cria um alias para a biblioteca

nota = 6.855

#arrendodamentos

print(round(nota, 2)) #1 casa

print(math.floor(nota)) #para baixo
print(math.ceil(nota))  #para cima

#números aleatórios
print(round(random.random() * 100))
print(random.randint(1,20))


#no consolte utilizar pip para instalar pacotes de terceiros
#exemplo
#pip install numpy 