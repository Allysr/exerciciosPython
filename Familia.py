# Faça um programa para representar a árvore genealógica de uma família. Para tal, crie uma classe Pessoa que permita indicar, além de nome e idade, o pai e a mãe. Tenha em mente que pai e mãe também são do tipo Pessoa.

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_idade(self, idade):
        self.idade = idade

    def get_idade(self):
        return self.idade

    # PAI
    def set_pai(self, pai):
        self.pai = pai

    def get_nome_pai(self):
        return self.pai.get_nome()

    # MAE
    def get_nome_mae(self):
        return self.mae.get_nome()

    def set_mae(self, mae):
        self.mae = mae

    # AVÓ

    def get_nome_avo(self):
        return self.avo.get_nome()

    def set_avo(self, avo):
        self.avo = avo

    # AVÓ PATERNA
    def get_nome_avo_paterna(self):
        return self.avo_paterna.get_nome()

    def set_avo_paterna(self, avo_paterna):
        self.avo_paterna = avo_paterna

    #PRINT GERAL

    def info(self):
        return (self.nome, self.idade, self.pai.get_nome(), self.mae.get_nome(), self.get_nome_avo(), self.get_nome_avo_paterna())


def menu():
    opcao = 0
    while opcao != 2:
        print("""  Arvoré Genealógica
                    1. Criar Árvore
                    2. Sair
                    """)
        escolha = int(input("Digite sua escolha: "))
        if escolha == 1:
            # Pessoa
            nome = input("Digite o seu nome: ")
            pessoa = Pessoa(nome)
            idade = int(input("Digite a sua idade: "))
            pessoa.set_idade(idade)
            # Pai
            nome_pai = input("Digite o nome do seu pai: ")
            pessoa_pai = Pessoa(nome_pai)
            pessoa.set_pai(pessoa_pai)
            # Mae
            nome_mae = input("Digite o nome do sua mãe: ")
            pessoa_mae = Pessoa(nome_mae)
            pessoa.set_mae(pessoa_mae)

            # Avó Materna
            nome_avo = input("Digite o nome do sua Avó Materna: ")
            pessoa_avo = Pessoa(nome_avo)
            pessoa.set_avo(pessoa_avo)

            # Avó Paterna
            nome_avo_paterna = input("Digite o nome do sua Avó Paterna: ")
            pessoa_avo_paterna = Pessoa(nome_avo_paterna)
            pessoa.set_avo_paterna(pessoa_avo_paterna)

            print(f"""Nome: {pessoa.get_nome()} - Idade: {pessoa.get_idade()} - Mae: {pessoa.get_nome_mae()}
            - Pai {pessoa.get_nome_pai()} - Avó Materna: {pessoa.get_nome_avo()} - Avó Paterna: {pessoa.get_nome_avo_paterna()}""")
            menu()
        elif escolha == 2:
            opcao = 2
        else:
            print("Opção invalida")


menu()
