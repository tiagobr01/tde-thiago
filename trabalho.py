class Trabalho:
    contador=0
    def __init__(self,titulo,descricao,resumo,data_entrega,autores,orientador,palavras) -> None:
        self.titulo=titulo
        self.descricao=descricao
        self.resumo=resumo
        self.data_entrega=data_entrega
        self.autores=autores
        self.orientador=orientador
        self.palavras=palavras
        Trabalho.contador+=1
        self.id=Trabalho.contador
        
    def get_data(self):
        return self.data_entrega
    def __str__(self) -> str:
        return f"Titulo:{self.titulo}\n,Descrição:{self.descricao}\n,Resumo:{self.resumo}\n,Data de entrega:{self.data_entrega}\n,Autores:{self.autores}\n,Orientador:{self.orientador}\n,Palavras-chave:{self.palavras}"
    def __eq__(self,outro) -> bool:
        if not isinstance(outro,Trabalho):
            return False
        return self.id==outro.id
      