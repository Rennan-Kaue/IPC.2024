#2) Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda
# ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
# uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

texto = input('digite uma palavra ou uma frase: ')

texto_novo = texto.replace(' ','').lower()

palindromo = False

for i in range(len(texto_novo)):
    if texto_novo[i] == texto_novo[(len(texto_novo)-1)-i]:
        palindromo = True

if palindromo == True:
    print('seu texto é um palindromo')

if palindromo == False:
    print('seu texto não é um palindromo')

