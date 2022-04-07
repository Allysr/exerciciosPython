#     Escreva uma classe que represente um país. Um país é representado através dos atributos: código ISO 3166-1 (ex.: BRA), nome(ex.: Brasil), população(ex.: 193.946.886) e a sua dimensão em Km2(ex.: 8.515.767, 049). Além disso, cada país mantém uma lista de outros países com os quais ele faz fronteira. Escreva a classe e forneça os seus membros a seguir:
#     a) Construtor que inicialize o código ISO, o nome e a dimensão do país;

#     b) Métodos de acesso(getter/setter) para as propriedades código ISSO, nome, população e dimensão do país;

#     c) Um método que permita verificar se dois objetos representam o mesmo país(igualdade semântica). Dois países são iguais se tiverem o mesmo código ISO;

#     d) Um método que informe se outro país é limítrofe do país que recebeu a mensagem;

#     e) Um método que retorne a densidade populacional do país;

#     f) Um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países. Considere que um país tem no máximo 40 outros países com os quais ele faz fronteira.

class Pais:
    def __init__(self,codigo_Iso, nome, dimensao):
        self.codigo_Iso = codigo_Iso
        self.nome = nome
        self.dimensao = dimensao
 
 
#SETTER
    def set_codigo_Iso(self, codigo_Iso):
        self.codigo_Iso = codigo_Iso
   
    def set_nome(self,nome):
        self.nome = nome
       
    def set_populacao (self, populacao):
        self.populacao = populacao
   
    def set_dimensao(self, dimensao):
        self.dimensao = dimensao
 
    def set_fronteiras(self, fronteiras = {}):
        self.fronteiras = fronteiras
   
    def set_limitrofe(self,limitrofe = []):
        self.limitrofe = limitrofe
 
#GETTER
    def get_codigo_Iso(self):
        return self.codigo_Iso
   
    def get_nome(self):
        return self.nome
 
    def get_populacao (self):
        return self.populacao
   
    def get_dimensao(self):
        return self.dimensao
   
 
   
# VERIFICAR SE SÃO IGUAIS
    def mesmo_pais (self,pais, pais_dois):
        if (pais.codigo_Iso == pais_dois.codigo_Iso):
            print("São Iguais")
        else:
            print("Paises diferentes")
 
 
    def limitrofes (self,pais,pais_dois):
        if pais.nome in pais_dois.limitrofe:
            return "É limitrofe"
        else:
            return "Não é limitrofe"
 
    def paises_comuns(self,pais,pais_dois):
      return (pais.fronteiras.intersection(pais_dois.fronteiras))
 
 
   
if __name__ == "__main__":
    # PRIMEIRO PAIS INFOS:
    pais = Pais("BRA", "Brasil", "8.516.000 km²")
    pais.set_fronteiras({"Argentina", "Uruguai", "Bolívia", "Colômbia", "Guiana", "Paraguai", "Peru", "Suriname", "Venezuela", "Guiana Francesa"})
    pais.set_limitrofe(["Uruguai", "Argentina", "Paraguai", "Bolívia", "Peru", "Colômbia", "Venezuela", "Guiana Francesa", "Suriname"])
    pais.set_populacao("212 milhões")
   
    # PAIS DOIS INFOS:
    pais_dois = Pais("ARG", "Argentina",  "2.780.000 km²")
    pais_dois.set_fronteiras({"Chile", "Brasil", "Bolívia", "Paraguai", "Uruguai"})
    pais_dois.set_limitrofe(["Chile", "Brasil", "Bolívia", "Paraguai", "Uruguai"])
    pais_dois.set_populacao( "42 milhões")
 
    #TESTES
    pais.mesmo_pais(pais, pais_dois)
    print(pais.get_populacao())
    print(pais.limitrofes(pais,pais_dois))
    print(pais.paises_comuns(pais,pais_dois))