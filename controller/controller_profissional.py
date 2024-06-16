from profissional import Profissional,Autor,Orientador
from DAO.DAO_profissionais import DAO_profissionais

class ProfissionalBC:
    def __init__(self):
        self.profissionalDAO=DAO_profissionais()
    def inserirProfissional(self,nome,cpf,email,diferenca):
        pass
    def alterarProfissional(self,nome,cpf,email,diferenca):
        pass
    def removerProfissional(self,cpf):
        pass    
    