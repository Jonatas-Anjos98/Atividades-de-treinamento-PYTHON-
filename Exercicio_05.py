def Calcular_Salario():
    Salario_minimo = 1518.00
    while True:
        try:
            Salario_User = float(input('\n Digite seu Salário: '))
            break
        except:
            print('Você precisa digitar um número')

    Quant_Salario = Salario_User / Salario_minimo

    print(f'\n Você possue {Quant_Salario: .2f} Salários minimos ')

Calcular_Salario()