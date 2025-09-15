import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = {
    'Nome':['João', 'Maria', 'José', 'Ana', 'Pedro'],
    'Idade': [28, 34, 45, 29, 50],
    'Salário': [2500,3000, 3500, 4000, 4500],
    'Cargo': ['Analista', 'Desenvolvedor', 'Gerente', 'Diretor', 'CEO'],
}

df = pd.DataFrame(dados)
print(df)

media_Idade = df['Idade'].mean()
media_Salario = df['Salário'].mean()

print("\nMédia das idades e salários:")
print('Média Idade ',media_Idade)
print('Média Idade ',media_Salario)

Tabela_dois = pd.read_csv('alunos.csv')
print(Tabela_dois)

print(df['Idade'])