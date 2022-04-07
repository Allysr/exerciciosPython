# Identifique as classes e implemente um programa para a seguinte especificação:
#  “O supermercado vende diferentes tipos de produtos. Cada produto tem um preço e uma
#   quantidade em estoque. Um pedido de um cliente é composto de itens, onde cada item
#   especifica o produto que o cliente deseja e a respectiva quantidade. Esse pedido pode
#   ser pago em dinheiro, cheque ou cartão.”

class Produto:
    def __init__(self, cod_prod, nome, preco_unitario, qtd_estoque):
        self.cod_prod = cod_prod
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.qtd_estoque = qtd_estoque

    # Get pegar o nome

    def get_cod_prod(self):
        return self.cod_prod

    def get_nome(self):
        return self.nome

    def get_preco_unitario(self):
        return self.preco_unitario

    def get_qtd_estoque(self):
        return self.qtd_estoque

    # Para alterar o valor
    def set_preco_unitario(self, preco_unitario):
        self.preco_unitario = preco_unitario

    def baixa_qtd_estoque(self, qtd):
        # Utilização da forma resumida
        # self.qtd_estoque = self.qtd_estoque - qtd
        self.qtd_estoque -= qtd

    def add_qtd_estoque(self, qtd):
        self.qtd_estoque += qtd


class Item:
    def __init__(self, cod_prod, preco_unitario, qtd_comprada):
        self.cod_prod = cod_prod
        self.preco_unitario = preco_unitario
        self.qtd_comprada = qtd_comprada

    def get_preco_unitario(self):
        return self.preco_unitario

    def get_qtd_comprada(self):
        return self.qtd_comprada

    def get_cod_prod(self):
        return self.cod_prod


class Pedido:
    lista_compras = []

    def add_item(self, cod_prod, preco_unitario, qtd_comprada):
        self.lista_compras.append(Item(cod_prod, preco_unitario, qtd_comprada))

    def print_lista_compras(self):
        for compra in self.lista_compras:
            print(
                f"COD: {compra.get_cod_prod()} - PREÇO: {compra.get_preco_unitario()} - QTD:{compra.get_qtd_comprada()} ")
        print(
            f"TOTAL: {self.get_total_pedidos()} - FORMA DE PAGAMENTO: {self.get_forma_pgto()} ")

    def set_forma_pgto(self, forma):
        self.forma = forma

    def get_forma_pgto(self):
        return self.forma

    def get_total_pedidos(self):
        total = 0
        for item in self.lista_compras:
            var = item.get_preco_unitario() * item.get_qtd_comprada()
            total += var
        return total

    def get_lista_itens(self):
        return self.lista_compras

def menu():
    print("""
              - MERCADO -
              1. Logista
              2. Cliente
              3. Sair
                  """)
    escolha = int(input("Digite sua Escolha:"))
    if escolha == 1:
        print("""
              - ÁREA DO LOGISTA-
              1. Ver Estoque
              2. Adicionar Produtos
              3. Voltar
              4. Sair
               """)
        escolha = int(input("Digite sua Escolha:"))
        if escolha == 1:
            print("RELATÓRIO DE ESTOQUE")
            for prod in estoque:
                print(f"\t -{prod.get_nome()} - QTD: {prod.get_qtd_estoque()}")
            menu()

        elif escolha == 2:
            print("ADICIONAR PRODUTOS")
            #Quando for booleano colocar is na frente
            codigo_utilizado = False
            while codigo_utilizado == False:
                new_cod_prod = int(input("Digite o código do produto:"))
                for prod in estoque:
                    # print(type(prod.get_cod_prod()), '--' , type(new_cod_prod))
                    if prod.get_cod_prod() == new_cod_prod:
                        codigo_utilizado = True
                        print(
                            f"Atenção, codigo {new_cod_prod} já cadastrado, adicione um novo código")
            # print("passou")

            nome = input("Digite o nome do produto: ")
            preco_unitario = input("Digite o preço do produto: ")
            qtd_estoque = input("Digite a quantidade de estoque: ")
            estoque.append(Produto(new_cod_prod, nome,
                           preco_unitario, qtd_estoque))
            print("PRODUTO ADICIONADO COM SUCESSO!")
            menu()

        elif escolha == 3:
            print("Voltar")
            menu()
        elif escolha == 4:
            print("Sair")

        else:
            print("Opção Inválida")
    elif escolha == 2:
        print("""
              - ÁREA DO CLIENTE -
              1. Ver Produtos Disponiveis
              2. Comprar Produtos
              3. Voltar
              4. Sair
               """)
        escolha = int(input("Digite sua Escolha:"))
        if escolha == 1:
            print("PRODUTOS")
            for prod in estoque:
                if prod.get_qtd_estoque() > 0:
                    print(
                        f"\tCod:{prod.get_cod_prod()} - {prod.get_nome()} - R${prod.get_preco_unitario()}")

         elif escolha == 2:
            print("COMPRAR PRODUTOS")
            for prod in estoque:
                if prod.get_qtd_estoque() > 0:
                    print(
                        f"\tCod:{prod.get_cod_prod()} - {prod.get_nome()} - R${prod.get_preco_unitario()}")
            pedido = Pedido()
            is_compra_finalizada = False
            while is_compra_finalizada == False:
                cod_item = int(input("Digite o código do produto desejado:"))
                qtd_item = int(input("Digite a quantidade desejada:"))
                preco_item = 0
                for prod in estoque:
                    if prod.get_cod_prod() == cod_item:
                        preco_item = prod.get_preco_unitario()
                pedido.add_item(cod_item, preco_item, qtd_item)
                finalizar = str(input("Deseja encerrar a compra (y/n): "))
                if finalizar.lower() == "y":
                    is_compra_finalizada = True
            print(""" 
              - FORMA DE PAGAMENTO -
              1. Cartão de Credito
              2. Cheque
              3. Dinheiro
              4. Sair
               """)
            escolha = int(input("Digite sua Escolha:"))
            if escolha == 1:
                pedido.set_forma_pgto("Cartão de Credito")
            elif escolha == 2:
                pedido.set_forma_pgto("Cheque")
            elif escolha == 3:
                pedido.set_forma_pgto("Dinheiro")

            #  Baixa no Estoque
            for item in pedido.get_lista_itens():
                for prod in estoque:
                    if prod.get_cod_prod() == item.get_cod_prod():
                        prod.baixa_qtd_estoque(item.get_qtd_comprada())
            pedido.print_lista_compras()
            menu()

         elif escolha == 3:
            print("Voltar")
         elif escolha == 4:
            print("Sair")
         else:
            print("Opção Inválida")
    elif escolha == 3:
        print("Saindo...")
    else:
        print("Opção Inválida")


if __name__ == "__main__":
    estoque = []
    estoque.append(Produto(111, "Carne Vegana", 20, 10))
    estoque.append(Produto(222, "Suco Vegano", 5, 10))
    estoque.append(Produto(333, "Pão Vegano", 10, 20))
    estoque.append(Produto(444, "Almondega Vegano", 10, 0))

    # for prod in estoque:
    #     print(prod.get_nome())
    menu()

# Adicionar uma função para cada tipo de menu, pois ele volta para o menu inicial
