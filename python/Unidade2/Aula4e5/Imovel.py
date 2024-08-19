from abc import ABC, abstractmethod #importa Abstract Base Class

class Imovel(ABC): # se torna uma classe abstrata podendo se utilizar de métodos abstratos além dos concretos
    def __init__(self,nome, uf, valor, endereco = '', area = ''):
        #atributos
        self._nome = nome #convenção python _ protegido (pode usar na classe filha) __ privado (pertence apenas a classe pai)
        self._uf = uf
        self._valor = valor
        self._endereco = endereco
        self._area = area
    #métodos
    #encapsulamento: atributos passaram a serem privados e apenas acessados por métodos
    #métodos de acesso a atributos
    @property           #annotation
    def nome(self):     #método get
        return self._nome
    @nome.setter        #método set
    def nome(self, nome):
        self._nome = nome

    @property           
    def uf(self):     #método get
        return self._uf
    @uf.setter        #método set
    def uf(self, uf):
        self._uf = uf

    @property           
    def valor(self):     #método get
        return self._valor
    @valor.setter        #método set
    def valor(self, valor):
        self._valor = valor

    @property           
    def endereco(self):     #método get
        return self._endereco
    @endereco.setter        #método set
    def endereco(self, endereco):
        self._endereco = endereco

    @property           
    def area(self):     #método get
        return self._area
    @area.setter        #método set
    def area(self, area):
        self._area = area

    '''
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
        '''
    #métodos gerais
    def detalhar(self): #método concreto
        #...
        print(self.__dict__)

    def calcularImposto(self):
        return self._valor * (2/100)
    
    @abstractmethod                 #obriga a todas outras classes que herdam tem de possuir este método dentro delas
    def AluguelSugerido(self):
        ...


#herança
class ImovelResidencial(Imovel): #não precisa do extend, a indicação já gera a herança
    def __init__(self,nome, uf, valor, endereco = '', area = ''): #se um init ou um método é reescrito igual ao pai o do filho substituir
        #atributos
        super().__init__(nome, uf, valor, endereco = '', area = '') #com o super, apesar de reescrito repõe no método os parâmetros do da classe pai
        #atributos novos da classe filha
        self._quartos = ''
        self._banheiros = ''
    
    @property           
    def quartos(self):     #método get
        return self._quartos
    @quartos.setter        #método set
    def quartos(self, quartos):
        self._quartos = quartos

    @property           
    def banheiros(self):     #método get
        return self._banheiros
    @banheiros.setter        #método set
    def banheiros(self, banheiros):
        self._banheiros = banheiros

    def AluguelSugerido(self):
        return self._valor * 0.01
    
class ImovelComercial(Imovel):
    def AluguelSugerido(self):
        return self._valor * 0.020
    
    def calcularImposto(self): #polimorfismo - substituindo ou sobrescrevendo o método do pai
        match self._uf:
            case 'RJ': taxa = 3
            case 'SP': taxa = 4
            case 'DF': taxa = 5
            case other: taxa = 6
        return self._valor * (taxa/100)

class ImovelRural():
    def __init__(self, hectares = '', curral = '', produtiva = True):
        self._hectares = hectares
        self._curral = curral
        self._produtiva = produtiva

    @property           
    def hectares(self):     #método get
        return self._hectares
    @hectares.setter        #método set
    def hectares(self, hectares):
        self._hectares = hectares

    @property           
    def curral(self):     #método get
        return self._curral
    @curral.setter        #método set
    def curral(self, curral):
        self._curral = curral

    @property           
    def produtiva(self):     #método get
        return self._produtiva
    @produtiva.setter        #método set
    def produtiva(self, produtiva):
        self._produtiva = produtiva

    def mesPlantacao(self, mes):
        match int(mes):
            case 1: print('Milho')
            case 2: print('Feijão')
            case 3: print('Soja')
            case other: print('Algodão')

#herança multipla
class Fazenda(Imovel,ImovelRural): # a ordem interfere, na questão de metodos iguais, sendo que o primeiro substitui o segundo
    def AluguelSugerido(self):
        return self.valor * 0.015


#classe abstrata não pode ser instanciada, por isto esta só serve para modelo para classes filhas, só serve de herança
    

casa = ImovelResidencial('Bandeira 51', 'RJ', 250000)
#casa.setNome('Casa Bonita')
#print(casa.getNome())
#casa.nome = 'Casa muito bonita'
#print(casa.nome)
#casa.detalhar()
#print(casa.AluguelSugerido())

print(casa.calcularImposto())

clinica = ImovelComercial('São Luiz', 'SP', 300000)
clinica2 = ImovelComercial('São Luiz', 'RJ', 300000)
#clinica.detalhar()

print(clinica.calcularImposto())
print(clinica2.calcularImposto())

'''
fazenda = Fazenda('São Luiz', 'RJ', 300000)
fazenda.detalhar()
'''

'''
#instância da classe
imovel = Imovel('Apartamento A', 'RJ', 500000)

imovel.endereco = 'Rua dos Limoeiros, 55, 201'
imovel.area = 100

imovel.detalhar()
'''