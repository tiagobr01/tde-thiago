view=UserView()

escolha='-1'

while escolha !=5:
    escolha=input("Escolha uma opção: ")

    match escolha:
        case '1':
            view.inserirUsuario()
        case '2':
            view.removerUsuario()
        case '3':
            view.alterarUsuario()
        case'5':
            print("Fim do programa")