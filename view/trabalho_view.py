class TrabalhoView:
    def __init__(self):
        self.trabalhoBC=TrabalhoBC()
    def exibirMenu(self):
        print("1-Para inserir um trabalho\n")
        print("2-Para atualizar um trabalho\n")
        print("3-Para remover um trabalho")
    def inserirTrabalho(self):
        titulo=input("Título do trabalho: ")
        descricao=input("Descrição do trabalho: ")
        resumo=input("Resumo do trabalho: ")
        entrega=input("Data de entrega: ")
        autores=input("Autores do trabalho: ")
        orientador=input("Orientador: ")
        palavras=input("Palavras-chave: ")
        if self.TrabalhoBC.inserirTrabalho(titulo,descricao,resumo,entrega,autores,orientador,palavras):
            print("Sucesso!")
        else:
            print("Deu não")                
    def alterarTrabalho(self):
        id=int(input("Informe o id do trabalho a ser alterado: "))
        titulo=input("Informe o título do trabalho: ")
        descricao=input("Informe a descrição do trabalho: ")
        resumo=input("Informe o resumo do trabalho: ")
        data=input("Informe a data de entrega do trabalho: ")
        autores=input("Informe os autores do trabalho: ")
        orientador=input("Informe o orientador do trabalho: ")
        palavras=input("Informe as palavras-chave do trabalho: ")
        if self.TrabalhoBC.alterarTrabalho(id,titulo,descricao,resumo,data,autores,orientador,palavras):
            print("Sucesso")
        else:
            print("Vai dar não")    
    def removerTrabalho(self):
        id=int(input("Informe o id do Trabalho que quer remover: "))
        if self.TrabalhoBC.removerTrabalho(id):
            print("Sucesso")
        else:
            print("Deu não")