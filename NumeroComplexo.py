#    Escreva uma classe NumeroComplexo, que representa um número complexo. A classe deve fornecer as seguintes operações:
#     a) Construtor com valores das partes inteira e fracionária;
#     b) Métodos getter/setter para os atributos da parte inteira e parte imaginária;
#     c) Método somar, que recebe outro número complexo e o adiciona ao número complexo que recebeu a mensagem. (a+bi)+(c+di)=(a+c)+(b+d)i;
#     d) Método subtrair, que recebe outro número complexo e o subtrai do número complexo que recebeu a mensagem. (a+bi)−(c+di)=(a−c)+(b−d)i;
#     e) Método multiplicar, que recebe outro número complexo e o multiplica ao complexo que recebeu a mensagem: (a+bi) * (c+di)=(ac−bd)+(ad+bc)i;
#     f) Método dividir, que recebe outro número complexo e o divide ao complexo que recebeu a mensagem: (a+bi) / (c+di)=(ac+bd)/(c2 + d2) + (bc-ad)/(c2 + d2)i;
#     g) Um método de comparação semântica dos números complexos;
#     h) Um método que gere e retorne a representação string do número complexo;
#     i) Um método que retorne o módulo do número complexo.

import math


class NumerosComplexos:
    def __init__(self, inte, ima):
        self.inte = inte
        self.ima = ima

# SET
    def set_inteiro(self):
        self.inte = self.inte

    def set_imaginario(self):
        self.ima = self.ima

# GET
    def get_inteiro(self):
        return self.inte

    def get_imaginario(self):
        return self.ima

# SOMAR
    def somar(self, numero_dois):
        soma = (numeros.inte + numeros.ima) + \
            (numero_dois.inte + numero_dois.ima)
        return soma

# SUBTRAIR
    def subtrair(self, numero_dois):
        subtrai = (numeros.inte + numeros.ima) - \
            (numero_dois.inte + numero_dois.ima)
        return subtrai

# MULTIPLICAR
    def multiplicar(self, numero_dois):
        multiplicar = (numeros.inte + numeros.ima) * \
            (numero_dois.inte + numero_dois.ima)
        return multiplicar

# DIVIDIR
    def dividir(self, numero_dois):
        dividir = (numeros.inte + numeros.ima) / \
            (numero_dois.inte + numero_dois.ima)
        return dividir

    def semantica(self):
        if (self.inte == self.ima):
            return True
        else:
            return False

    def get_string(self):
        return (f'Numero inteiro: {self.inte} - Numero imaginário: {self.frac}')

    def modulo(self):
        return math.sqrt(self.inte*self.inte + self.ima*self.ima)


numeros = NumerosComplexos(2, 7j)
numero_dois = NumerosComplexos(3, 3j)
