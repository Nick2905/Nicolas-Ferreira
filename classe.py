print("Classes e Objetos: Programação Orientada a Objeto")

class Aluno():
    nome = ""
    idade = ""
    nota = 0
    anotacoes = ""
    ativo = True

    def __init__(self, nome, idade, nota, anotacoes, ativo):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.anotacoes = anotacoes
        self.ativo = ativo

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def aprovado(self):
        if self.nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno(
      nome = "Nicolas",
      idade = "14",
      nota = 10,
      anotacoes = "Aluno Ctrlplay",
      ativo = True 
)
print(aluno1)

print("Desativado aluno")
aluno1.desativar()

passou = aluno1.aprovado()
print(f"Situação do aluno: {passou}")
