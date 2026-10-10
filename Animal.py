print("Aula Abstração Polimorfismo")

class Animal:

    def nome(self):
        print("Animal")

    def oquecome(self):
        print("Comida")

    def habitate(self):
        print("Planeta Terra")

class Cachorro(Animal):
    def nome(self):
        print("Cachorro")

    def oquecome(self):
        print("Ração")

    def habitate(self):
        print("Em Casa")

    def latir(self):
        print("Auau")


class Gato(Animal): 

    def nome(self):
        print("Gato")

    def miar(self):
        print("Miau")

animal = Animal()

animal.nome()
animal.oquecome()
animal.habitate()

print("Dados do cachorro")

cachorro = Cachorro()
cachorro.nome()
cachorro.oquecome()
cachorro.habitate()
cachorro.latir()

print("Dados do gato:")

gato = Gato()
gato.nome()
gato.oquecome()
gato.habitate()
gato.miar()