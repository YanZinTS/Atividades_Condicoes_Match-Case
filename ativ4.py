animal = str(input('Digite o nome de um animal: '))

match animal:
    case 'vaca':
        print('Você digitou o animal vaca')
    case 'galinha':
        print('Você digitou o animal galinha')
    case 'ovelha':
        print('Você digitou o animal ovelha')
    case _:
        print('Animal desconhecido')
