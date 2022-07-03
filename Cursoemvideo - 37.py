'''

!!! OUTROS EXERCÍCIOS !!!

'''
----------------------------------------

#22 - crie um programa que leia o nome completo de uma pessoa e mostre
#1 o nome com todas as letras maiusculas
#2 o nome com todas minusculas
#3 quantas letras ao todo(sem considerar espaços)
#4 quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo de uma pessoa:'))
nome = nome.upper()
print(" ")
----------------------------------------

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
#print('A soma entre',n1,'e',n2,'vale',s)
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))
----------------------------------------

n = input('digite algo')
print('numerico',n.isnumeric())
print('Alfa numerico',n.isalnum())
print('Letra',n.isalpha())
print('Maiusculo',n.isupper())
print('decimal',n.isdecimal())
----------------------------------------

n1 = int(input('Digite em que ano nós estamos,no formato aaaa'))
n2 = int(input('Digite o ano do seu nascimento,no formato aaaa'))
s = n1 - n2
print('Fazendo a subtração das datas digitadas:{0}-{1}, você tem {2}anos.'.format(n1, n2, s)
----------------------------------------

n1 = int(input('Digite um número'))
print(n1-1,n1,n1+1)

n2 = int(input('Digite um número: '))
print('O dobro do número é: ',n2*2)
print('O triplo do número é: ',n2*3)
print('A raiz quadrada do número é: ',n2**(1/2))

aluno = str(input('Digite o nome do Aluno: '))
nota1 = float(input('Digite a primeira nota do aluno'))
nota2 = float(input('Digite a segunda nota do aluno'))
media = (nota1 + nota2)/2
print('O aluno,',aluno,' tem as notas:',nota1,'e',nota2,'e a sua média é:',media,)


'''               
                  ### MUNDO 1 - TRATANDO DADOS E FAZENDO CONTAS ###

'''              

#5 - NÚMERO ANTECESSOR,ELE E SUCESSOR - ***(3 FORMAS DE FAZER)***
n = int(input('Digite um número'))
print(n-1,n,n+1)

ou

n = int(input('Digite um número'))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))

ou

n = int(input('Digite um número'))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
------------------------------

#6 - NÚMERO DOBRO TRIPLO E RAIZ QUADRADA
n2 = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n,d))
print('O triplo de {} vale {}. \nA Raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
-------------------------------

#7 - NOTAS ALUNO E MÉDIA - MÉDIA ARITMÉTRICA
aluno = str(input('Digite o nome do Aluno: '))
nota1 = float(input('Digite a primeira nota do aluno'))
nota2 = float(input('Digite a segunda nota do aluno'))
media = (nota1 + nota2)/2
print('O aluno,',aluno,' tem as notas:',nota1,'e',nota2,'e a sua média é:',media,)

ou

print('A media entre {} e {} é igual a {}'.format(n1, n2, media))
--------------------------------

#8 - CONVERSÃO 3 METROS - CONVERSOR DE MEDIDAS
medida = float(input('Uma distância em metros:'))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))
---------------------------------

#9 - TABUADA
n = int(input('Digite um número para mostrar a tabuada dele'))

print('Valor de',n,'x 0=',n*0)
print('Valor de',n,'x 1=',n*1)
print('Valor de',n,'x 2=',n*2)
print('Valor de',n,'x 3=',n*3)
print('Valor de',n,'x 4=',n*4)
print('Valor de',n,'x 5=',n*5)
print('Valor de',n,'x 6=',n*6)
print('Valor de',n,'x 7=',n*7)
print('Valor de',n,'x 8=',n*8)
print('Valor de',n,'x 9=',n*9)
print('Valor de',n,'x 10=',n*10)

ou

n = int(input('Digite um número para ver sua tabuada'))
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
---------------------------------

#10 - CAMBIO REIAS DOLLAR CONVERSOR DE MOEDAS
nome = str(input('Qual é o nome do comprador?'))
dinheiroreal = float(input('Quantos reais tem disponível para o cambio?'))
print('Após o cambio o',nome,'terá US',dinheiroreal*3.27)

ou

real = float(input('Quanto dinheiro você tem na carteira?'))
dolar = real / 3.27
print('Com R${:2f} você pode comprar US${:2f}',format(real, dolar))
---------------------------------

#11 - PINTURA
larparede = float(input('Qual é a largura da parede:'))
altparede = float(input('Qual é a altura da parede:'))
area = larparede*altparede
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(larparede, altparede, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta,'.format(tinta))
---------------------------------

#12 - VALOR PRODUTO CALCULANDO DESCONTO
preco = float(input('Qual é o valor do produto? R$:'))
novopreco = preco - (preco * 5 / 100)
print('O produto que custava {}, na promoção com desconto de 5% vai custar R${}'.format(preco, novopreco))
---------------------------------

#13 - SALÁRIO FUNCIONÁRIO AUMENTO DE 15%
salario = float(input('Digite o salário do funcionário'))
salarionovo = salario + (salario * 15 /100)
print('A salário inicial do funcionário era R$: {0}, com o aumento de 15%,\n passou a ser R$:{1}'.format(salario, salarionovo))
----------------------------------

#14 - CONVERSOR DE TEMPERATURA °C PARA °F
c = float(input('Informe a temperatura em °C'))
f = ((9 * c) / 5 ) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
-----------------------------------

#15 - ALUGUEL DE CARRO
dias = int(input('Quantos dias alugados?'))
rodado = int(input('Quantos Km rodados?'))
gastos = (dias * 60) + (rodado * 0.15)
print('O custo total de gastos é de R$:{}'.format(gastos))
-----------------------------------

                ### MUNDO 1 - USANDO MÓDULOS DO PYTHON ###

#16 - PROGRAMA QUE LEIA UM NÚMERO REAL, PELO TECLADO E MOSTRE NA TELA A PORÇÃO INTEIRA EX.: 6.127 = 6
n = float(input('Digite um número real'))
print('O número real é: {} e a sua porção inteira é: {} '.format(n, math.trunc(n)))

ou

from math import trunc
n = float(input('Digite um número real'))
print('O número real é: {} e a sua porção inteira é: {} '.format(n, trunc(n)))

ou

n = float(input('Digite um número:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))
------------------------------

#17 - LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADEJACENTE DE UM TRIANGULO RETANGULO, CALCULE E
#MOSTRE A HIPOTENUSA
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

ou

import math
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

ou

from math import hypot
co = float(input('Comprimento do cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
-------------------------------------

#18 - LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO COSSENO E TANGENTE DESSE ÂNGULO
import math
angulo = float(input('Digite o ângulo que você deseja'))
sen = math.sin(math.radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, sen))
cos = math.cos(math.radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, tan))

ou

from math import sen, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja'))
sen = sin(radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, sen))
cos = cos(radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ângulo de {}° e {:.2f}°'.format(angulo, tan))
-------------------------------------------

#19 - UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O
#NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO
import random
n1 = str(input('nome do aluno primeiro aluno'))
n2 = str(input('nome do aluno segundo aluno'))
n3 = str(input('nome do aluno terceiro aluno'))
n4 = str(input('nome do aluno quarto aluno'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

ou

from random import choice
n1 = str(input('nome do aluno primeiro aluno'))
n2 = str(input('nome do aluno segundo aluno'))
n3 = str(input('nome do aluno terceiro aluno'))
n4 = str(input('nome do aluno quarto aluno'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
------------------------------------------

#20 - O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM
#PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.
from random import shuffle
n1 = str(input('Digite o primeiro nome:'))
n2 = str(input('Digite o segundo nome:'))
n3 = str(input('Digite o terceiro nome:'))
n4 = str(input('Digite o quarto nome:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A sequência de apresentação será:')
print(lista)

ou

import random
n1 = str(input('Digite o primeiro nome:'))
n2 = str(input('Digite o segundo nome:'))
n3 = str(input('Digite o terceiro nome:'))
n4 = str(input('Digite o quarto nome:'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A sequência de apresentação será:')
print(lista)
-------------------------------------------

#21 - FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3
import pygame
pygame.init()
pygame.mixer.music.load('nomearquivo.mp3')#o arquivo tem q estar na pasta
pygame.mixer.music.play()
pygame.event.wait()
-------------------------------------------

#22 - crie um programa que leia o nome completo de uma pessoa e mostre
#1 o nome com todas as letras maiusculas
nome = str(input('Digite o nome completo de uma pessoa:'))
print('analisando seu nome...')'
print('Seu nome em maiúscula é {}'.format(nome.upper()))

#2 o nome com todas minusculas
nome = str(input('Digite o nome completo de uma pessoa:'))
print('analisando seu nome...')
print('Seu nome em minúscula é {}'.format(nome.lower()))

#3 quantas letras ao todo(sem considerar espaços)
nome = str(input('Digite o nome completo de uma pessoa:')).strip()
print('analisando seu nome...')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

#4 quantas letras tem o primeiro nome
nome = str(input('Digite o nome completo de uma pessoa:'))
dividido = nome.split()
print(dividido)
separa = nome.split()
print('Seu primeiro é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

ou

nome = str(input('Digite o nome completo de uma pessoa:'))
print('analisando seu nome...')
print('Seu primeiro nome tem {} letra'.format(nome.find(' ')))
--------------------------

#23 - faça um programa que leia um numero de 0 a 9999 e mostre 
#na tela cada um dos digitos separados
#tentar fazer com str
#tentar matemáticamente
#undade:4
#dezena:3
#centena:8
#milhar:1
num = int(input('Digite o número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
----------------------------------------------

#24 - crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = str(input('Digite o nome de uma cidade')).strip()
print(cidade[:5].upper() == 'SANTO')
---------------------------

#25 - crie um programa que leia o nome de uma pessoa e diga se ela tem ''silva'' no nome
nome = str(input('Qual é o seu nome completo')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
----------------------------

#26 - Faça um programa que leia uma frase pelo teclado e mostre:
#1quantas vezes aparece a letra ''A''
frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))
-----------------------------

#27 - faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#ex.: Ana Maria de Souza
#primeiro: Ana
#segundo: Souza

n = str(input('Digite um nome completo:')).strip()
nome = n.split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O segundo nome é: {}'.format(nome[len(nome)-1]))
--------------------------

#Aula 10
# Ex1.: Carro velho e novo
tempo = int(input('Quantos anos tem o seu carro?'))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')

ou

tempo = int(input('Quantos anos tem o seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')
--------------------------

#Aula 10 - Condições Simples, Compostas e Simplificadas
# Ex2.: Nota aluno
n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('SUA MÉDIA FOI BOA! PARABÉNS!')
else:
    print('ESTUDE MAIS!')

ou

n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')
--------------------------

                ### MUNDO 1 - CONDIÇÕES EM PYTHON(IF , ELSE) ###

#28 - faça um programa que faça o computador pensar em um número inteiro 
# entre 0 e 5 e peça para o usúario tentar descobrir qual foi o número escolhido pelo computador
#O programa escreve na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "Pensar"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Errou! Eu pensei no número {} e não no {}!'.format(computador, jogador))
--------------------------

#29 - escreva um programa que leia a velocidade de um carro
#1 se ele ultrapassar 80 km/h,mostre uma mensagem dizendo que ele foi multado.
#2 A multa vai custar R$7.00 por cada km acima do limite
velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! Vôce excedeu o limite permitido que é de 80Km/h')
    multa  = (velocidade-80) * 7
    print('Você deve pagar uma multa de R$: {:.2f}'.format(multa)) 
print('Tenha um bom dia! Diriga com segurança!')
--------------------------

#30 - crie um programa que leia um número inteiro qualquer e escreva se ele é par ou impar
numero = int(input('Me diga um número qualquer?'))
resultado = numero % 2
print('O resultado foi {}'.format(resultado))
if resultado == 0:

    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
--------------------------

#31 - desenvolva um programa que pergunte a distância de uma viagem em km.
#1 calcule o preço do passagem, cobrando R$0.50 por km para viagens de até 200km
#2 R$ 0.45 para viagens mais longas.
distancia = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {:.1f} Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem para esse trecho será de: R$ {:.2f}'.format(preco))

ou

distancia = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {:.1f} Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia *0.45
print('O preço da passagem para esse trecho será de: R$ {:.2f}'.format(preco))
--------------------------

#32 - faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('Que ano quer analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
-------

#32 extra - analise se o ano atual é bissexto
from datetime import date
ano = int(input('Que ano quer analisar?Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
--------------------------

#33 - faça um programa que leia 3 números e mostre qual é o número menor e maior
a = int(input('Digite o primeiro numero:'))
b = int(input('Digite o segundo numero:'))
c = int(input('Digite o terceiro numero:'))
#Verificando quem é o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
--------------------------

#34 - escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#1 para salários superiores a R$1250.00 calcule um aumento de 10%
#2 para os inferiores ou iguais, o aumento é de 15% 
#34 - escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários superiores a R$1250.00 calcule um aumento de 10%para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite o salário do funcionário:'))
if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)
print('O salário anterior era de R$: {:.2f} e com o aumento, passou a ser de R$: {:.2f}'.format(salario, novosalario))
--------------------------

#35 - desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triãngulo.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
--------------------------

                ### MUNDO 1 - Estilos de textos e cores ###

'''  Ex:. \033[0;33;44m - É o padrão para formatar as cores  '''

# Style de letra
# 0 - Nome
# 1 - Bold(normal)
# 4 - Underline(sublinhada)
# 7 - Negative(invertida)

# Text - Cor da letra
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - magenta
# 36 - ciano
# 37 - cinza

# Back - Cor de fundo
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - magenta
# 46 - iano
# 47 - cinza  

                ### MUNDO 2 - CONDIÇÕES ANINHADAS  ###

# AULA 12 #

#36 - Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual é o valor da casa?'))
salario = float(input('Salário comprador?'))
anos = float(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
minimo = salario - (salario * 30 /100) 
print('Para pagar uma casa de R$:{:.2f} em {} anos'.format(casa, anos))
print('a prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')
-----------------------------------

#37
