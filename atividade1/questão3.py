#3) Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
#indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

cpf = input('Digite o número de cpf no formato xxx.xxx.xxx-xx: ')


ultimos = cpf[12] + cpf[13]


if (len(cpf) < 11) or (len(cpf) > 14):
    print('Cpf inválido')
elif (cpf[3] != '.') or (cpf[7] != '.'):
    print('Cpf inválido')
elif (cpf[11] != '-'):
    print('Cpf inválido')
else:
    cpf_novo = cpf.replace(".","").replace("-","")
    

    verificacao = (((int(cpf_novo[0])*1) + (int(cpf_novo[1])*2) + (int(cpf_novo[2])*3) +
                    (int(cpf_novo[3])*4) + (int(cpf_novo[4])*5) + (int(cpf_novo[5])*6) +
                    (int(cpf_novo[6])*7) +(int(cpf_novo[7])*8) + (int(cpf_novo[8])*9))%11)

    verificacao2 = (((int(cpf_novo[0])*0) + (int(cpf_novo[1])*1) + (int(cpf_novo[2])*2) +
                     (int(cpf_novo[3])*3) + (int(cpf_novo[4])*4) + (int(cpf_novo[5])*5) +
                     (int(cpf_novo[6])*6) +(int(cpf_novo[7])*7) + (int(cpf_novo[8])*8) +
                     (verificacao)*9)%11)

    validacao = str(verificacao) + str(verificacao2)


    if ultimos == validacao:
        print('Cpf válido')
    
    else:
        print('Cpf inválido')
    
    
    
        






