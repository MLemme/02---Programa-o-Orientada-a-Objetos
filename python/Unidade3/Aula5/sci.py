#python e IA e Machine Learn
#pip install scikit-learn

from sklearn.cluster import KMeans
import numpy as np

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

produtos = [
    Produto('P1', 60.50,0.70),
    Produto('P2', 25,0.50),
    Produto('P3', 5.99,0.20),
    Produto('P4', 50,0.78),
    Produto('P5', 15.99,0.30),
    Produto('P6', 8.75,0.15),
]
nc = 4 #numero de clusters ou agrupamentos
precos = [[p.preco, p.peso] for p in produtos]
matriz = np.array(precos)
#cria um cluster agrupando por preço e peso a partir da matriz
kmeans = KMeans(n_init='auto',n_clusters=nc, random_state=0).fit(matriz)
labels = kmeans.labels_

print(labels)
for i in range(nc):
    print(f"Grupo {i+1}:")
    for j in range(len(produtos)):
        if labels[j] == i:
            print(" - ", produtos[j].nome)

