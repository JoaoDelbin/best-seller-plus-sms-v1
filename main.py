import pandas as pd
from twilio.rest import Client

account_sid = 'AC4d73a69a422ddbe04ae86358a89c794a'
auth_token = 'b8353529aa5f0085e5261c0ffceaa0ea'
client = Client(account_sid, auth_token)



lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} um vendedor conquistou a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            body=f'No mês {mes} um vendedor conquistou a meta. Vendedor: {vendedor}, Vendas: {vendas}',
            from_='+13184968298',
            to='+5511965811022')
        print(message.sid)