#Exercício 1 - Aula 05
#Lê 3 valores, encontra o maior, menor e a média deles

valor1 = int(input('informe um valor:'))
valor2 = int(input('informe outro valor:'))
valor3 = int(input('informe o terceiro valor:'))

#Encontrar o maior valor
if valor1 >= valor2 and  valor1 >= valor3:
  maior = valor1
elif valor2 >= valor1 and valor2 >= valor3:
  maior = valor2
else:
  maior = valor3
print('maior valor:', maior)

#Encontrar o menor valor
if valor1 <= valor2 and  valor1 <= valor3:
  maior = valor1
elif valor2 >= valor1 and valor2 >= valor3:
  maior = valor2
else:
  maior = valor3
print('maior valor:', maior)


#Encontrar a média
media = (valor1 + valor2 + valor3) / 3
print('valor médio', media) 
