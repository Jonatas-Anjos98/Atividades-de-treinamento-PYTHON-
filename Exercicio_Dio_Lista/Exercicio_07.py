def Apresentacao():
    while True:
        try:
            Nome_01 = input('Digite o seu nome:')
            break
        except:
            print('Você preciasa digitar um nome!')
    while True:
        try:
            Idade_01 = input('Digite a sua idade: ')
            break
        except:
            print('Você precisa digitar uma idade válida\n')
    if(Idade_01 >= '18'):
        Idade_01 = True
    else:
        Idade_01 = False
    while True:
        try:
            Estado_Civil = input('Qual o seu estado civil?(solteiro/casado)')
            break
        except:
            print('Digite apenas solteiro ou casado!')
    if (Estado_Civil == 'casado'):
        Estado_Civil = True
    else:
        Estado_Civil = False

    print (f'Olá{Nome_01} bem vindo ao meu site.\n Você e de maior: {Idade_01}\n Você e casado: {Estado_Civil}')

Apresentacao()