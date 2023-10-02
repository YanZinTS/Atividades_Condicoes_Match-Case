login = str(input('Digite seu login: '))
senha = str(input('Digite sua senha: '))

match (login, senha):
    case("admin", "admin_pass"):
        print('Logado com sucesso usuário 1')
    case("user", "user_pass"):
        print('Logado com sucesso usuário 2')
    case("guest", _):
        print('Logado com sucesso usuário 3')
    case _:
        print('Login ou senha incorreta')