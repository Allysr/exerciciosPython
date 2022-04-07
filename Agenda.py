#  Faça um programa de agenda telefônica, com as classes Agenda e Contato.

class Contato:  
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
 
    # Interações sobre um objeto 'Contato'
    def getNome(self):
        return self.nome
 
    def getTelefone(self):
        return self.telefone
 
    def getEmail(self):
        return self.email
 
    def informacoes(self):
        return f'Nome: {self.nome} - Telefone: {self.telefone}, - Email: {self.email}'
 
 
class Agenda:
    # Uma genda possui uma coleção de Contatos
    arrayContatos = []
 
    # Interacoes sobre um contato
    def addContato(self, nome, telefone, email):
        contato = Contato(nome, telefone, email)
        self.arrayContatos.append(contato)
   # Append acrescenta ao final da lista
    def getTelefone(self, nome):
        for contato in self.arrayContatos:
            if contato.getNome() == nome:
                return contato.getTelefone()
 
    def getEmail(self, nome):
        for contato in self.arrayContatos:
            if contato.getNome() == nome:
                return contato.getEmail()
 
    def printContato(self, nome):
        for contato in self.arrayContatos:
            if contato.getNome() == nome:
                return contato.informacoes()
 
    def printContatos(self):
        listagem = ''
        for contato in self.arrayContatos:
            listagem = listagem + contato.informacoes() + '\n'
        return listagem
 
# Metodo para o código começar por aqui
if __name__ == "__main__":
    agenda = Agenda()
    agenda.addContato('Teste', 333333333, 'teste@teste.com')
    agenda.addContato('SonserinaNao', 7777777, 'SonserinaNao.com')
 
 
    # Buscas
    print(f'Minha Agenda:\n{agenda.printContatos()}')
    #print(f'Telefone: {agenda.get_telefone("Teste")}')
    #print(f'Email: {agenda.get_email("Teste")}')
    #print(f'Contato:\n{agenda.print_contato("Teste")}')
