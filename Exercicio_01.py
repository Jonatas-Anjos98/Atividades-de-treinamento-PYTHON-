def Tratar_Nums():
    while True:
        try:
            Num_01 = int(input('\nEscreva o primeiro número:'))
            break
        except:
            print('Você precisa digitar um número!')

    while True:
        try:
            Num_02 = int(input('Escreva o segundo número:'))
            break
        except:
            print('Você precisa digitar um número!')

    while True:
        try:
            Num_03 = int(input('Escreva o terceiro número:'))
            break
        except:
            print('Você precisNum_01 digitar um número!')
    Resul_Soma = Num_01 + Num_02

    print(f'\nA soma do primeiro e o segundo número e igual a: {Resul_Soma}\n')

    if(Resul_Soma < Num_03):
        print('A soma do primeiro e segundo número é menor que o terceiro!')
    else:
        print('A soma do primeiro e segundo número é maior que o terceiro!')

Tratar_Nums()