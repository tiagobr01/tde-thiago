class Trabalho:
    def __init__(self,titulo,descricao,resumo,data_entrega,autores,orientador,palavras) -> None:
        self.titulo=titulo
        self.descricao=descricao
        self.resumo=resumo
        self.__data_entrega=data_entrega
        self.autores=autores
        self.orientador=orientador
        self.palavras=palavras
        
    def get_data(self):
        return self.__data_entrega
    
      