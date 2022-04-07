#  Escreva uma classe Contador, que encapsule um valor usado para contagem de itens ou eventos. A classe deve oferecer métodos que devem:
# a) Zerar;
# b) Incrementar;
# c) Retornar o valor do contador.

class Contador:
    def __init__(self, _valor=0):
        self._valor = _valor

    def set_zerar(self):
        self._valor = 0

    def set_incrementar(self):
        self._valor = self._valor + 1

    def set_decrementar(self):
        self._valor = self._valor - 1

    def get_numero(self):
        print(f" --> O número está em {self._valor} <--")


if __name__ == "__main__":
    contador = Contador()


def menu():
    is_final_contagem = False
    while is_final_contagem == False:
        print("""ESCOLHA UMA OPÇÃO:
                1.Zerar
                2.Incrementar
                3.Decrementar
                4.Retornar valor do contador
                5.Sair""")
        escolha = int(input("Digite a sua escolha: "))
        if escolha == 1:
            contador.set_zerar()
        elif escolha == 2:
            contador.set_incrementar()
            contador.get_numero()
        elif escolha == 3:
            contador.set_decrementar()
            contador.get_numero()
        elif escolha == 4:
            contador.get_numero()
        elif escolha == 5:
            is_final_contagem = True
        else:
            print("""- ERRO! -
                  Opção Inválida""")


menu()

# COLOCAR UM SUB MENU PARA "DESEJA CONTINUAR"
