import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

# Caso queira executar o codigo, refaça o caminho dos arquivos abaixo:
clientesDF = pd.read_csv(r'C:\Users\wever\PycharmProjects\AnaliseDeDados\Arquivos para análise\CadastroClientes.csv',
                         sep=';')
funcionariosDF = pd.read_csv(
    r'C:\Users\wever\PycharmProjects\AnaliseDeDados\Arquivos para análise\CadastroFuncionarios.csv', sep=';',
    decimal=',')
servicosDF = pd.read_excel(
    r'C:\Users\wever\PycharmProjects\AnaliseDeDados\Arquivos para análise\BaseServicosPrestados.xlsx',
    engine='openpyxl')

# Valor total da folha salarial
funcionariosDF['Salario Total'] = funcionariosDF[['Salario Base', 'Impostos', 'Beneficios', 'VT', 'VR']].sum(axis=1)
total_folha_sal = sum(funcionariosDF[
                          'Salario Total'])
print(f'Total da folha salarial é de: R${total_folha_sal:,}')

print('')

# Faturamento total
faturamentoDF = servicosDF[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(
    clientesDF[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')
faturamentoDF['Faturamento Total'] = faturamentoDF['Tempo Total de Contrato (Meses)'] * faturamentoDF[
    'Valor Contrato Mensal']
faturamento_total = sum(faturamentoDF['Faturamento Total'])
print(f'faturamento total da empresa foi de: R${faturamento_total:,}')

print('')

# Porcentagem de funcionarios que fecharam contrato de serviço
porcentagem_funcionarios = len(servicosDF['ID Funcionário'].unique()) / len(funcionariosDF['ID Funcionário'])
print(f'{porcentagem_funcionarios:.0%} dos funcionarios fecharam contratos')

print('')

# Calculando o total de contratos por área
contratos_area_DF = servicosDF[['ID Funcionário']].merge(funcionariosDF[['ID Funcionário', 'Area']],
                                                         on='ID Funcionário')
contratos_area_qtde = contratos_area_DF['Area'].value_counts()
print('')
print('-----------Quantidade de contratos por área------------')
print(contratos_area_qtde)

# Plotando gráfico da questão acima
contratos_area_qtde.plot(figsize=(5, 4), kind='bar')
plt.title('Quantidade de contratos por área')
plt.ylabel('Quantidade de contratos')
plt.show()

# Quantidade de funcionários por área
qtde_funcionario_area = funcionariosDF['Area'].value_counts()
print('')
print('-----------Quantidade de funcionários por área---------')
print(qtde_funcionario_area)

# TICKET MÉDIO
ticket_medio = clientesDF['Valor Contrato Mensal'].mean()
print(f'Ticket Médio Mensal é de: R${ticket_medio:,.2f}')
