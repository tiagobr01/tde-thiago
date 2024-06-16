class DAO_trabalho:
    trabalhos=[]

    def salvarTrabalho(self,trabalho):
        DAO_trabalho.trabalhos.append(trabalho)
    def obterTrabalhoPeloId(self,id):
        for trabalho in DAO_trabalho.trabalhos:
            if trabalho.id==id:
                return trabalho
            return None
    def removerTrabalho(self,trabalho):
        DAO_trabalho.trabalhos.remove(trabalho)        