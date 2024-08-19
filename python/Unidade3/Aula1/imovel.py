#from Unidade3.Aula1e2 import data #importa metodo encapsulado da Aula 2
#import Unidade3.Aula2.data as data
import data
#dumber (double score) methods - métodos especiais do python ou intrísecos ao mesmo
class Categoria:
    def __init__(self, tipo = ''):
        self.tipo = tipo
    
    def taxaAgua(self, consumo):
       print("Data da leitura: ", data.formatarData())
       match self.tipo:
           case 'Clínica': return 1 * consumo
           case 'Restasurante': return 2 * consumo
           case 'Hotel': return 2.5 * consumo

#composição - atributo de uma classe que é do tipo de outra classe

class Imovel:

    imposto = 0.2 #atributo de classe , precisa de um método de classe para ser acessado

    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        self.categoria = Categoria()
    
    #metodos mágicos
    def __add__(self, other): #metodo mágico do Python - automaticamente é chamado quando somado dois objetos
        somaSelf  = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther
    
    def __gt__(self,other): #metodo mágico do Python - automaticamente é chamado quando compara maiorque dois objetos
        somaSelf  = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther
    
    def __lt__(self,other): #metodo mágico do Python - automaticamente é chamado quando compara menorque dois objetos
        somaSelf  = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    
    def __str__(self): #antes de tentar o print natural, ele busca este método
        return str(self.__dict__)
    
    def detalhar(self):
        return self.__dict__
    
    def somarAposentos(self):
        return self.quartos + self.suites
    
    #metodos ESTÁTICO - não precisa instaciar o objeto, porém não aceita self, pois não há um objeto que use
    @staticmethod
    def metodoEstatico():
        print('Chamou o método estático sem criar um objeto')
    
    #metodos de CLASSE
    @classmethod
    def metodoClasse(cls):
        print('Chamoo o método de classe que vê o imposto', cls.imposto)



casarao = Imovel('Casarão', 3, 4)

#print(casarao.__dict__)

mansao = Imovel('Mansão', 4, 5)
#print(mansao.__dict__)

categoria = Categoria('Hotel')
hotel = Imovel('Hostel',0,150)
hotel.categoria = categoria

print(hotel.categoria.taxaAgua(300))

'''
print(casarao + mansao)
print(casarao > mansao)
print(casarao < mansao)
print(casarao)
'''

#print(casarao.somarAposentos())
#print(mansao.somarAposentos())

#Imovel.metodoClasse()
#Imovel.metodoEstatico()