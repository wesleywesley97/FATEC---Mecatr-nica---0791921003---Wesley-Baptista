#Pede ao usuário digitar uma senha e a valida com a senha secreta
#Cria uma variável para guardar a senha
senha_secreta = '123456'

#Pede ao usuário para digitar sua senha
senha = input('Informe a senha:')

#Verifica se a senha do usuário está correta
if senha == senha_secreta:
  print('Bem-vindo, Hackerman!')
else: 
  print('Acesso negado')
