num = int(input('Digite um número de 1 a 3: '))
if num == 1 or num == 2 or num == 3:
    print(f'O número digitado foi {num}')
else:
    print(f'Digite um número entre 1 e 3')

#---------------------------OPA-----------------------------#

num1 = int(input('Digite um número de 1 a 3: '))
match num1:
    case 1:
        print(f'Digitou {num1}')
    case 2:
        print(f'Digitou {num1}')
    case 3:
        print(f'Digitou {num1}')
    case _:
        print('Digitou errado')

#---------------------------OPA-----------------------------#

login = str(input('Digite seu login: '))
senha = str(input('Digite sua senha: '))

match (login, senha):
    case('Yan', '123'):
        print('Logado com sucesso')
    case _:
        print('Login ou senha incorreta')

#---------------------------OPA-----------------------------#

