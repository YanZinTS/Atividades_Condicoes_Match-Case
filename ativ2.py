cor = str(input('Digite uma cor: '))

match cor:
    case'vermelho':
        print('Cor vermelha encontrada')
    case 'azul':
        print('Cor azul encontrada')
    case 'verde':
        print('Cor verde encontrada')
    case _:
        print('Cor desconhecida')