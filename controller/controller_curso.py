from curso import Curso
from DAO.DAO_cursos import DAO_cursos
class CursoBC:
    id=0
    def __init__(self):
        self.cursoDAO=DAO_cursos()
    def inserirCurso(self,Curso):
        if self.cursoDAO.obterCursoPeloId(.id)
    def alterarCurso(self,nome,descricao):
        pass
    def removerCurso(self):
        pass    
