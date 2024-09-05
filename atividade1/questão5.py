#5) Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

import random

def escolher_palavra():
    with open('palavras.txt', 'r') as arquivo:
        palavras = arquivo.read().splitlines()
    
    palavra_secreta = random.choice(palavras)
    return palavra_secreta

def jogo_forca():
    palavra = escolher_palavra()
    letras_descobertas = ['_'] * len(palavra)
    tentativas = 6
    letras_erradas = []

    print('Bem-vindo ao Jogo da Forca!')
    print('A palavra oculta é: ' + ' '.join(letras_descobertas))

    while tentativas > 0 and '_' in letras_descobertas:
        letra = input('Digite uma letra: ').lower()

        if letra in letras_erradas or letra in letras_descobertas:
            print(f'Você já tentou a letra {letra}. Tente outra.')
            continue

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra
            print('A palavra é: ' + ' '.join(letras_descobertas))
        else:
            tentativas -= 1
            letras_erradas.append(letra)
            print(f'-> Você errou pela {6 - tentativas}ª vez. Tente de novo!')

        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")

    if '_' not in letras_descobertas:
        print('Parabéns! Você adivinhou a palavra:', palavra)
    else:
        print('Você foi enforcado! A palavra era:', palavra)

jogo_forca()
