import sqlite3

class DAO_trabalho:
    def conectar(self):
        self.conn = sqlite3.connect(".\\database\\portaldb")
        self.cursor = self.conn.cursor()
    
    def desconectar(self):
        self.cursor.close()
        self.conn.close()

    def inserirTrabalho(self,trabalho):
        self.conectar()
        parametros = [trabalho.titulo,trabalho.descricao,trabalho.resumo,trabalho.data_entrega,trabalho.autores,trabalho.orientador,trabalho.palavras,trabalho.id]
        sql = "insert into trabalhos (titulo,descricao,resumo,data_entrega,autores,orientador,palavras,id) values (?, ?, ?,?,?,?,?,?)"
        print(sql)
        print(parametros)
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        print(linhasAfetadas)
        self.conn.commit()
        self.desconectar()
    def obterTrabalhoPeloId(self,id):
        self.conectar()
        parametros = [id]
        sql = "select * from trabalhos where email = ?"
        self.cursor.execute(sql, (parametros))
        contato = self.cursor.fetchone()
        self.desconectar()
        return contato
    
    def alterarTrabalho(self,trabalho):
        self.conectar()
        parametros = [trabalho.titulo,trabalho.descricao,trabalho.resumo,trabalho.data_entrega,trabalho.autores,trabalho.orientador,trabalho.palavras,trabalho.id]
        sql = "update trabalhos set nome = ?, descricao=?,resumo=?,data_entrega=?,autores=?,orientador=?,palavras=? where id = ?"
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        self.conn.commit()
        self.desconectar()
        return linhasAfetadas
    
    def removerTrabalho(self,trabalho):
        self.conectar()
        parametros = [trabalho[0]]
        sql = "delete from trabalhos where id = ?"
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        self.conn.commit()
        self.desconectar()
        return linhasAfetadas