class DAO_cursos:
    cursos=[]

    def salvarCurso(self,curso):
        DAO_cursos.cursos.append(curso)
    def obterCursoPeloId(self,id):
        for curso in DAO_cursos.cursos:
            if curso.id_curso==id:
                return curso
            return None

    def removerCurso(self,curso):
        DAO_cursos.cursos.remove(curso)        