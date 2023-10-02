diaSemana = str(input('Digite um dia da semana: '))

match diaSemana:
    case 'segunda':
        print('Hoje é segunda-feira, dia útil')
    case 'terça':
        print('Hoje é terça-feira, dia útil')
    case 'quarta':
        print('Hoje é quarta-feira, dia útil')
    case 'quinta':
        print('Hoje é quinta-feira, dia útil')
    case 'sexta':
        print('Hoje é sexta-feira, dia útil')
    case 'sábado':
        print('Hoje é sábado, fim de semana')
    case 'domingo':
        print('Hoje é domingo, fim de semana')
    case _:
        print('Digito inválido')