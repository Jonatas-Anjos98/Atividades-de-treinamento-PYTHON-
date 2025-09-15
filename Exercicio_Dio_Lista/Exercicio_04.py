def Tratar_num():
    while True:
        try:
            Num_01 = int(input('Digite  o primeiro número:'))
            break
        except:
            print('Você precisa digitar um número')
    
    Num_Suc = Num_01 + 1
    Num_Ant = Num_01 - 1

    print(f'\nO antecessor do número escolhido é {Num_Ant}')
    print(f'O sucessor do número escolhido é {Num_Suc}')

Tratar_num()