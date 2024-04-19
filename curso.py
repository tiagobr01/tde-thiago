class Curso:
    def __init__(self,descricao_curso,nome_curso,id_curso) -> None:
        self.descricao_curso=descricao_curso
        self.nome_curso=nome_curso
        self.__id_curso=id_curso

    def get_id(self):
        return self.__id_curso