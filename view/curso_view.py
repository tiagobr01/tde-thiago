class CursoView:
    def __init__(self) :
        self.cursoBC=CursoBC()
    def exibirMenu(self):
        print("1-Para inserir um curso\n")
        print("2-Para atualizar um curso\n")
        print("3-Para remover um cursos")
    def inserirCurso(self):
        nome=input("Nome do curso: ")
        descricao=input("Descrição do curso: ")
        if self.CursoBC.salvarCurso(nome,descricao):
            print("Sucesso")
        else:
            print("Deu não")
    def alterarCurso(self):
        id=int(input("Informe o id do curso a ser alterado: "))
        nome=input("Informe o novo nome do curso: ")
        desc=input("Descreva o curso: ")
        if self.CursoBC.alterarCurso(id,nome,desc):
            print("Sucesso")
        else:
            print("Deu não")  
    def removerCurso(self):
        id=int(input("Informe o id do curso que quer remover: "))
        if self.CursoBC.removerCurso(id):
            print("Sucesso")
        else:
            print("Deu não")            