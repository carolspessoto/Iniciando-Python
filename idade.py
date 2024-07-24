print('Exercícios com If\n')

print('Qual é sua idade?:\n')

#def inserir_numero():
idade_inserida = int(input('Insira sua idade: '))

if idade_inserida <= 12:
        print('Você está na Categoria: Criança')
elif idade_inserida >= 13 and idade_inserida <= 18:
        print('Você está na Categoria: Adolescente')
#elif idade_inserida >= 19:
        #print('Categoria: Adulto')        
else:
        print('Você está na Categoria: Adulto')
