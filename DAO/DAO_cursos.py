import sqlite3
class DAO_cursos:
    def conectar(self):
        self.conn = sqlite3.connect(".\\database\\portaldb")
        self.cursor = self.conn.cursor()
    
    def desconectar(self):
        self.cursor.close()
        self.conn.close()


    def inserirCurso(self,curso):
        self.conectar()
        parametros = [curso.nome, curso.descricao]
        sql = "insert into cursos (nome,descricao) values (?,?)"
        print(sql)
        print(parametros)
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        print(linhasAfetadas)
        self.conn.commit()
        self.desconectar()
    
    def alterarCurso(self,curso):
        self.conectar()
        parametros = [curso.nome,curso.descricao,curso.id]
        sql = "update cursos set nome = ?, descricao=? where id = ?"
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        self.conn.commit()
        self.desconectar()
        return linhasAfetadas
        
    def obterCursoPeloId(self,id):
        self.conectar()
        parametros = [id]
        sql = "select * from cursos where id = ?"
        self.cursor.execute(sql, (parametros))
        curso = self.cursor.fetchone()
        self.desconectar()
        return curso
    
        

    def removerCurso(self,curso):
        self.conectar()
        parametros = [curso[0]]
        sql = "delete from cursos where id = ?"
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        self.conn.commit()
        self.desconectar()
        return linhasAfetadas
        