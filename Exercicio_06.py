def Reajuste_05():
    while True:
        try:
            Num_01 = int(input('escreva um número para saber o seu reajuste de 5%: '))
            break
        except:
            print('Você precisa digitar um número válido!')
    
    Num_01 % 5
    Reajuste = Num_01 * 1.05
    print(f'O reajuste de 5% terá o tatal de {Reajuste: .2f}.')

Reajuste_05()