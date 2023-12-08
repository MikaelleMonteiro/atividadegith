class Bola:
  def __init__(self, cor, medida):
    self.cor = cor # Atributo da Instância
    self.medida = medida # Atributo da Instância

  def comprimentar(self): # Criando o método da classe
      return f"Olá, eu sou uma bola cor de {self.cor} e tenho {self.medida} "

# Criando uma Instância da classe bola
bola1 = Bola("rosa", "20cm!")

# Chamando o método cumprimentar
mensagem = bola1.comprimentar()
print(mensagem)

