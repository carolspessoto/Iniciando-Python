print('Exercícios com If\n')

print('Por favor, informe as coordenadas:\n')

coordenadaX = '-2'
coordenadaY = '8'

coordenadaX_inserida = int(input('Insira a coordenadaX: '))
coordenadaY_inserida = int(input('Insira a coordenadaY: '))

if coordenadaX_inserida > 0 and coordenadaY_inserida > 0:
        print('Primeiro quadrante')
elif coordenadaX_inserida < 0 and coordenadaY_inserida > 0:
        print('Segundo quadrante')
elif coordenadaX_inserida < 0 and coordenadaY_inserida < 0:
        print('Terceiro quadrante')  
elif coordenadaX_inserida > 0 and coordenadaY_inserida < 0:
        print('Quarto quadrante')         
else:
        print('O ponto está localizado no eixo ou origem')