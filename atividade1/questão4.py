#4) Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e
# imprima-o na tela por extenso.

def numero_extenso(numero):
    
    unidades = ['zero', 'um', 'dois',
                'três', 'quatro', 'cinco',
                'seis', 'sete', 'oito', 'nove'
                ]

    diferentes = ['dez', 'onze', 'doze',
                  'treze', 'quatorze', 'quinze',
                  'dezesseis', 'dezessete', 'dezoito', 'dezenove'
                  ]

    dezenas = ['', '', 'vinte', 'trinta', 'quarenta',
               'cinquenta', 'sessenta', 'setenta',
               'oitenta', 'noventa'
               ]

    if 0 <= numero <= 9:
        return unidades[numero]
    elif 10 <= numero <= 19:
        return diferentes[numero - 10]
    else:
        dezena = numero // 10
        unidade = numero % 10

        if unidade == 0:
            return dezenas[dezena]
        else:
            return f"{dezenas[dezena]} e {unidades[unidade]}"


numero = int(input('Digite um número de até dois digitos: '))

if 0 <= numero <= 99:
    print(numero_extenso(numero))
else:
    print('Número inválido')

        
        

    

