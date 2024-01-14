class Pessoa:
    #Atributo de classe
    especie = 'Humana'
    pessoas = []

    #Método construtor
    def __init__(self, nome, idade, rua, cidade):
        self.nome = nome
        self.idade = idade
        self.rua = rua
        self.cidade = cidade
        self.pessoas.append(self)
    
    #Método de instância
    def __str__(self):
        return f'{self.nome} tem {self.idade} anos e mora na {self.rua} em {self.cidade}'