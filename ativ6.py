palavra1 = str(input('Digite alguma palavra: '))
palavra2 = str(input('Digite alguma palavra: '))

match (palavra1, palavra2):
    case ('Hello', 'World'):
        print('Amabs são iguais')
    case ('Hello', _):
        print('Não são iguais')
    case (_, 'World'):
        print('Essa condição não é favorável')