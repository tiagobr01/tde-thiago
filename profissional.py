from abc import ABC

class Profissional(ABC):
    def __init__(self,nome,cpf,email) -> None:
        self.nome=nome
        self.cpf=cpf
        self.email=email

class Autor(Profissional):
    def __init__(self,nome,cpf,email,curso) -> None:
        super().__init__(nome,cpf,email)
        self.curso=curso
    def __str__(self) -> str:
        return f"Nome:{self.nome}\n,Cpf:{self.cpf}\n,Email:{self.email}\n,Curso:{self.curso}"       
    def __eq__(self,outro) -> bool:
        if not isinstance(outro,Autor):
            return False
        return self.cpf==outro.cpf
class Orientador(Profissional):
    def __init__(self,nome,cpf,email,titulacao) -> None:
        super().__init__(nome,cpf,email)
        self.titulacao=titulacao
    @property
    def titulacao(self):
        return self.titulacao
    
    @titulacao.setter
    def titulacao(self,titulacao):
        if titulacao not in ["pós-graduado","mestre","doutor"]:
            raise ValueError("Titulação inválida")
        else:
            self.titulacao=titulacao
    def __str__(self) -> str:
        return f"Nome:{self.nome}\n,Cpf:{self.cpf}\n,Email:{self.email}\n,Curso:{self.titulacao}"        
    def __eq__(self,outro) -> bool:
        if not isinstance(outro,Orientador):
            return False
        return self.cpf==outro.cpf