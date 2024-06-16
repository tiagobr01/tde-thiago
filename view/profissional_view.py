class ProfissionalView:
    def __init__(self):
        self.profissionalBC=ProfissionalBC()
    def exibirMenu(self):
        print("1-Para inserir um profissional\n")
        print("2-Para atualizar ou remover um profissional\n")
        print("3-Para remover um profissional")
    def inserirProfissional(self):
        resp=input("Qual tipo de profissional deseja inserir? ").lower()

        if resp=='autor':
            nome=input("Digite o nome:")
            cpf=int(input("Digite o cpf: "))
            email=input("Digite o email: ")
            curso=input("Informe o curso: ")
            if self.ProfissionalBC.inserirProfissional(nome,cpf,email,curso):
                print("Sucesso!")
            else:
                print("Deu não")
        if resp=='orientador':
            nome=input("Digite o nome: ")
            cpf=int(input("Digite o cpf: "))
            email=input("Digite o email: ")
            titulacao=input("Informe o título: ")
            if self.ProfissionalBC.inserirProfissional(nome,cpf,email,titulacao):
                print("Sucesso!")
            else:
                print("Deu não")
    def alterarProfissional(self):
        tipo=input("Digite o tipo de profissional a ser alterado: ")
        id=int(input("Informe o cpf do profissional a ser alterado: "))
        email=input("Informe o novo email:")
        nome=input("Informe o novo nome:")
        if tipo=='orientador':
            titulo=input("Informe o novo titulo:")
            if self.ProfissionalBC.alterarProfissional(nome,id,email,titulo):
                print("Deu bom!")
            else:
                print("Deu ruim")    
        elif tipo=='autor':
            curso=input("Informe o novo curso: ")    
            if self.ProfissionalBC.alterarProfissional(nome,id,email,curso):
               print("Deu bom!")
            else:
                print("Deu ruim")
    def removerProfissional(self):
        id=int(input("Informe o cpf do profissional  que quer remover: "))
        if self.ProfissionalBC.removerProfissional(id):
            print("Sucesso")
        else:
            print("Deu não")      