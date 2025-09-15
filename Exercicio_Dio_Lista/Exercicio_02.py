def Tratar_Num():
    while True:
        try:
            Num_01 = int(input('Escreva um número qualquer: '))
            break
        except:
            print('Você precisa digitar um Num_01ero inteiro!')

    if Num_01 > 0:
        print('Seu número é positivo')
    elif Num_01 < 0:
        print('Seu número é negativo')
    else:
        print('Seu número é zero')

    if Num_01 % 2 == 0:
        print('Seu número é par')
    else:
        print('Seu número é ímpar')

Tratar_Num()