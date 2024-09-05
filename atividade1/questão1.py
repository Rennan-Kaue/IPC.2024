#1) Dados. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um
# vetor . Depois, mostre quantas vezes cada valor foi conseguido.
#Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random 

dado = []
lados_dado = [0, 0, 0, 0, 0, 0]
quantidade = ''

for count in range (100):
    sorteado = random.randint(1,6)
    if sorteado == 1:
        lados_dado[0] += 1
    elif sorteado == 2:
        lados_dado[1] += 1
    elif sorteado == 3:
        lados_dado[2] += 1
    elif sorteado == 4:
        lados_dado[3] += 1
    elif sorteado == 5:
        lados_dado[4] += 1
    elif sorteado == 6:
        lados_dado[5] +=1

print(f'o lado de número 1 aparece {lados_dado[0]} vezes')
print(f'o lado de número 2 aparece {lados_dado[1]} vezes')
print(f'o lado de número 3 aparece {lados_dado[2]} vezes')
print(f'o lado de número 5 aparece {lados_dado[4]} vezes')
print(f'o lado de número 6 aparece {lados_dado[5]} vezes')
