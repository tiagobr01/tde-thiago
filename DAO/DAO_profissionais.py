import sqlite3
class DAO_profissionais:
    def conectar(self):
        self.conn = sqlite3.connect(".\\database\\portaldb")
        self.cursor = self.conn.cursor()
    
    def desconectar(self):
        self.cursor.close()
        self.conn.close()

    

    def inserirProfissional(self,profissional):
        self.conectar()
        parametros = [profissional.nome, profissional.email, profissional.]
        sql = "insert into contatos (nome, email, telefone) values (?, ?, ?)"
        print(sql)
        print(parametros)
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        print(linhasAfetadas)
        self.conn.commit()
        self.desconectar()
    def obterProfissionalPeloCpf(self,cpf):
        self.conectar()
        parametros = [cpf]
        sql = "select * from trabalhos where cpf = ?"
        self.cursor.execute(sql, (parametros))
        contato = self.cursor.fetchone()
        self.desconectar()
        return contato

    def alterarProfissional(self,profissional):
        self.conectar()
        parametros = [profissional.nome,profissional.cpf,profissional.email]
        sql = "update profissionais set nome = ?, email=?, where cpf = ?"
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        self.conn.commit()
        self.desconectar()
        return linhasAfetadas
        
    def removerProfissional(self,profissional):
        self.conectar()
        parametros = [profissional[0]]
        sql = "delete from profissionais where cpf = ?"
        self.cursor.execute(sql, (parametros))
        linhasAfetadas = self.cursor.rowcount
        self.conn.commit()
        self.desconectar()
        return linhasAfetadas