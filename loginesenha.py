print('Exercícios com If\n')

print('Por favor, informe seu login e senha:\n')

login = "carol.spessoto"
senha = 123456
login_digitado = input('Digite seu login: ')
senha_digitada = int(input('Digite sua senha: '))

if login == login_digitado and senha == senha_digitada:
    print('Login efetuado com sucesso\n')
else:
    print('Login ou senha incorretos! Tente novamente')
