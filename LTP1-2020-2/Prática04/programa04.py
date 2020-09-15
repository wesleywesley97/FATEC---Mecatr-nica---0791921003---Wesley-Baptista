# #Operadores de divisão (/) e resto %
# divisão = 15 / 2
# resto = 15 % 2

# print('Divisão', divisão)
# print('Resto', resto)

#Ler um número para ver se é ímpar
número = int(input('informe um número:'))
#Calcula o resto da divisão do número por 2
resto = número % 2
#Olha para o valor do resto
if resto == 0:
 print(número,'é par!')
else:
 print(numero,'é ímpar!')
