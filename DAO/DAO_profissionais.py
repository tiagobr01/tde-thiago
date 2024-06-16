class DAO_profissionais:
    profissionais=[]

    def salvarProfissional(self,profissional):
        DAO_profissionais.profissionais.append(profissional)
    
    def obterProfissionalPeloCpf(self,cpf):
        for profissional in DAO_profissionais.profissionais:
            if profissional.cpf==cpf:
                return profissional
            return None
    def removerProfissional(self,profissional):
        DAO_profissionais.profissionais.remove(profissional)        