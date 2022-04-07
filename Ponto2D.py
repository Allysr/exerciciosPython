# Escreva uma classe Ponto2D que representa um ponto no plano cartesiano. Além dos atributos por você identificados, a classe deve oferecer os seguintes membros:

# a) Construtores sobrecarregados que permitam a inicialização do ponto:
#     i) Por default(sem parâmetros) na origem do espaço 2D;
#     ii) Num local indicado por dois parâmetros do tipo double(indicando o valor de abcissa e ordenada do ponto que está sendo criado);
#     iii) Em um local indicado por outro ponto.

# b) Métodos de acesso(getter/setter) dos atributos do ponto;

# c) Métodos sobrecarregados de movimentação do ponto com os mesmos parâmetros indicados para os construtores;

# d) Método de comparação semântica do ponto(equals);

# e) Método de representação do objeto como String;

# f) Método que permita calcular a distância do ponto que recebe a mensagem, para outro ponto;

# g) Método que permita a criação de um novo ponto no mesmo local do ponto que recebeu a mensagem(clone);

import math


class Ponto2D:
    def __init__(self, ponto_x=0, ponto_y=0):
        self.ponto_x = ponto_x
        self.ponto_y = ponto_y

# Acesso ponto X
    def set_ponto_x(self, ponto_x):
        self.ponto_x = ponto_x

    def set_ponto_x(self, ponto_x):
        self.ponto_x = ponto_x

# Acesso ponto Y
    def get_ponto_y(self):
        return self.ponto_y

    def get_ponto_y(self):
        return self.ponto_y
# Movimentação

    def movimentacao(self, ponto_x=5, ponto_y=6):
        self.ponto_x = ponto_x
        self.ponto_y = ponto_y

# Comparação Semantica
    def semantica(self):
        if (self.ponto_x == self.ponto_y):
            return True
        else:
            return False

# STRING
    def get_string(self):
        return (f'Ponto x: {self.ponto_x} - Ponto y: {self.ponto_y}')


# Distancia

    def distancia(self, ponto_dois):
        x_resultado = ponto_dois.ponto_x - self.ponto_x
        y_resultado = ponto_dois.ponto_y - self.ponto_y
        resultado = math.sqrt(math.pow(x_resultado, 2) +
                              math.pow(y_resultado, 2))
        return resultado

# Comparação
    def clone(self, ponto_dois):
        self.x = ponto_dois.x
        self.y = ponto_dois.y


ponto = Ponto2D(5, 6)
ponto_dois = Ponto2D(1, 1)
print(ponto.distancia(ponto_dois))
