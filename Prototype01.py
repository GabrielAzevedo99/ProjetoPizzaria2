# Gabriel Santos Azevedo
#Jeferson Ribeiro da Silva
# 3° DSM

import copy

# Classe Pessoa a ser usada como Prototype
class Cardapio:
  def __init__(self, sabor, preco, nome):
    self.sabor = sabor
    self.preco = preco
    self.nome = nome
    
  def __str__(self):
    return f'Sabor: {self.sabor}, Preco: {self.preco}, Nome: {self.nome}'
  
  def clone(self):
    return copy.copy(self)
    
# Gerenciador de Pessoa:
class CardapioManager:
  def __init__(self):
    self.cardapio = {}
    
  def adicionarCardapio(self, sabor, preco, nome, id):
    cardapio = Cardapio(sabor, preco, nome)
    self.cardapio[id] = cardapio
    
    
  def getCardapio(self, id):
    return self.cardapio[id].clone()
    
    
manager = CardapioManager()

# Adicionar Pessoas:
manager.adicionarCardapio('Parmesão', 45, 'Gabriel', 1)
manager.adicionarCardapio('Mussarela', 35, 'Jef', 2)
manager.adicionarCardapio('Calabresa', 35, 'Alguem1', 3)
manager.adicionarCardapio('Frango com catupiry', 50, 'Alguem2', 4)

# Clone Pessoas
cardapio1 = manager.getCardapio(1)
cardapio2 = manager.getCardapio(2)
cardapio3 = manager.getCardapio(3)
cardapio4 = manager.getCardapio(4)

# Modificando Pessoa:
cardapio1.preco = 18
cardapio2.sabor = "Paulistana"
cardapio3.preco = 20

# Imprime o resultado:
print(manager.getCardapio(1))
print(manager.getCardapio(2))
print(manager.getCardapio(3))
print(manager.getCardapio(4))
print("---------------------------------------")
print(cardapio1)
print(cardapio2)

