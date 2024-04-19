from abc import ABC

class Profissional(ABC):
    def __init__(self,nome,cpf,email) -> None:
        self.nome=nome
        self._cpf=cpf
        self._email=email

class Autor(Profissional):
    def __init__(self,nome,cpf,email,curso) -> None:
        super().__init__(nome,cpf,email)
        self.curso=curso
           

class Orientador(Profissional):
    def __init__(self,nome,cpf,email,titulacao) -> None:
        super().__init__(nome,cpf,email)
        self.titulacao=titulacao
    @property
    def titulacao(self):
        return self._titulacao
    
    @titulacao.setter
    def titulacao(self,titulacao):
        if titulacao not in ["pós-graduado","mestre","doutor"]:
            raise ValueError("Titulação inválida")
        else:
            self._titulacao=titulacao