import math

# 1. Faça uma função que receba o nome de uma pessoa como entrada e retorne uma saudação.
# Exemplo:
# Boa tarde, Samuel. Seja bem vindo!
def saudacao(nome):
    mensagem = f"Boa tarde, {nome}. Seja bem vindo!"
    return mensagem

print(saudacao("carol"))

# 2. Faça uma função que peça o raio de um círculo e retorne sua área.
def area_circulo(raio):
    area = (math.pi * (raio ** 2))
    return area
raio = 2
print(f"A área do círculo é: {area_circulo(raio):.2f}")
pass

# 3. Faça uma função que converta a temperatura de Fahrenheit para Celsius.
# C = 5 * ((F-32) / 9).
def fahrenheit_para_celsius():
    pass

# 4. Faça uma função que calcule a multa por excesso de peso de peixes.
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma funçao que receba como 
# entrada o peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# Exemplos de saidas para os parâmetros 70 e 25 respectivamente:
#
# Excesso de peso: 20 kg.
# Multa a pagar: R$ 80.00.
#
# Peso dentro do limite. Nenhuma multa aplicada.
def calculo_multa():
    pass

# 5. Faça uma função para calcular a quantidade de tinta necessária para pintar uma área.
# O função deverá receber o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
# de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.

## Exemplo de saída para uma área de 100 metros quadrados
# Quantidade de latas de 18L: 2
# Preço total: R$ 160.00
# 
# Quantidade de galões de 3,6L: 6
# Preço total: R$ 150.00
#
# Quantidade de latas: 1, Quantidade de galões: 1
# Preço total: R$ 105.00

def calcular_tinta():
    pass

# 6. Faça uma função que receba dois números e retorne o maior deles.
def maior_numero(n , m):
    if n > m :
        return n
    else: 
        return m
    
    print(maior_numero(10, 5))
    
    pass

# 7. Faça uma função que verifique se uma letra é vogal ou consoante.
def verificar_letra():
    pass

# 8. Faça um Programa que receba três números e retorne o maior deles.
def maior_tres_numeros(n1, n2, n3):
    if n1 > n2 & n3:
        return n1
    elif n2 > n1 & n3:
        return n2
    else:
        return n3
print(maior_tres_numeros(3, 7, 5))


# 9. Faça uma função que retorne o menor valor entre três numeros informados.
def produto_mais_barato(x, y, z):
    if x < y & z:
        return x
    elif y < x & z:
        return y
    else:
        return z
    
print(produto_mais_barato(15, 20, 10))

# 10. Faça uma funçao que retorne uma saudação com base no turno de estudo.
# A entrada deverá ser M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def saudacao_turno():
    pass

# 11. Faça uma função para um caixa eletrônico que informe quantas notas de cada valor serão fornecidas
# ao ser solicitado um saque.
# A função receberá como entrada o valor do saque e e retornará quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo de saída para uma entrada de 346
# Notas fornecidas:
# 3 nota(s) de R$ 100
# 4 nota(s) de R$ 10
# 1 nota(s) de R$ 5
# 1 nota(s) de R$ 1

def caixa_eletronico():
    pass

# 12. Desenvolva uma lógica que classifique uma pessoa com base nas respostas sobre um crime.
# A função deverá receber receba a resposta as seguintes perguntas:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
def classificar_participacao():
    pass

# 13. Faça um Programa que calcule o preço da carne em uma promoção com desconto opcional.
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva uma função que receba o tipo e a quantidade de
# carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def calcular_preco_carne():
    pass

# 14. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.
def potencia():
    pass

# 15. Faça um Programa que retorne o menor, maior e a soma de um conjunto de números.
def estatisticas_numeros():
    pass

# 16. Faça uma função que valide se uma nota está entre 0 e 10.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# Exemplos de saídas para as entradas -1 e 5.5 respectivamente:
# Erro: A nota deve estar entre 0 e 10. Tente novamente.
# Nota válida: 5.5

def validar_nota():
    pass

# 17. Faça uma funçao que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
# Exemplos de saídas com as entradas "user" "user" "user123" respectivamente
# "Erro: A senha não pode ser igual ao nome de usuário. Tente novamente."
# "Usuário e senha cadastrados com sucesso!"
def validar_usuario_senha():
    pass

# 18. Faça um Programa que calcule a média aritmética de um conjunto de N notas.
def media_notas(p1, p2, p3):
    media = ((p1 + p2 + p3) / 3)
    return media 
print(media_notas(7, 8, 9))    


# 19. Faça um programa que mostre os n termos da Série a seguir:
#     S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
def calcular_serie():
    pass

# 20. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
#  A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas 
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima 
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: João Silva
# Nota: 7.9
# Nota: 8.5
# Nota: 9.4
# Nota: 7.0
# Nota: 8.8
# Nota: 9.8
# Nota: 7.9

# Resultado final:
# Atleta: João Silva
# Melhor nota: 9.8
# Pior nota: 7.0
# Média: 8.50
def calcular_media_ginastica():
    pass

# 21. Faça um Programa que desenhe uma pirâmide alinhada à esquerda.
def piramide_esquerda():
    pass

# 22. Faça um Programa que desenhe uma pirâmide alinhada à direita.
def piramide_direita():
    pass

# 23. Faça um Programa que desenhe duas pirâmides lado a lado.
def piramides_lado_a_lado():
    pass

# 24. Faça um Programa que calcule o troco com a menor quantidade de moedas possível.
def calcular_troco():
    pass

# 25. Faça um Programa que valide um número de cartão de crédito usando o algoritmo de Luhn.
def validar_cartao():
    pass
