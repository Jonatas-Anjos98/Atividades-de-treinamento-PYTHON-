def Tratar_num():
    while True:
        try:
            Num_01 = int(input('Escreva o primeiro número: '))
            break
        except:
            print('Você precisa digitar um número!')
    
    while True:
        try:
            Num_02 = int(input('Escreva o segundo número: '))
            break
        except:
            print('Você precisa digitar um número!')
    if Num_01 == Num_02:
        Resul = Num_01 + Num_02
        print(f'A soma dos dois números e igual à {Resul}.')
    else:
        Resul = Num_01 * Num_02
        print(f'A multiplicação dos dois números e igual à {Resul}.')
    

Tratar_num()