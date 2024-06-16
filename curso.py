class Curso:
    contador=0
    def __init__(self,nome_curso,descricao_curso) -> None:
        self.nome_curso=nome_curso
        self.descricao_curso=descricao_curso
        Curso.contador+=1
        self.id_curso=Curso.contador

    def get_id(self):
        return self.id_curso
    def __str__(self) -> str:
        return f"Nome:{self.nome_curso}\n,Id:{self.id_curso}\n  Descrição:{self.descricao_curso}"
    def __eq__(self,outro) -> bool:
        if not isinstance(outro,Curso):
            return False
        return self.id_curso==outro.id_curso