# Faça um programa para controle de empréstimo de livros, com as classes Empréstimo, Livro e Pessoa.
class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def informacoes(self):
        print(f'Nome: {self.nome} - Telefone: {self.telefone}')


class Livros:
    def __init__(self, titulo):
        self.titulo = titulo

    def informacoes(self):
        print(f'Titulo: {self.titulo}')


class Emprestimo:
    def __init__(self, nome, telefone, titulo, data, entrega):
        self.nome = pessoa
        self.telefone = pessoa
        self.titulo = livro
        self.data = data
        self.entrega = entrega

    def informacoes(self):
        print(f'Nome: {self.nome.nome} - Telefone: {self.telefone.telefone} - Titulo: {self.titulo.titulo} - Data: {self.data} - Entrega: {self.entrega}')


pessoa = Pessoa("Alicia", 999999999)
livro = Livros("João das Neves")
emprestimo = Emprestimo(pessoa, pessoa, livro, 11.07, 12.08)
emprestimo.informacoes()
