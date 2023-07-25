import requests # biblioteca Requests
import json # biblioteca Json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") # Onde fica as informações das cotações
cotacoes = cotacoes.json() # Convertendo as cotações para um Json

cotacao_dolar = cotacoes['USDBRL']["bid"] # Solicitando a cotação em Dolar
print(f'Cotaçao do Dolar atual: R$ {cotacao_dolar}') # Mostrando a cotação em Dolar

cotacao_euro = cotacoes['EURBRL']["bid"] # Solicitando a cotação em Euro
print(f'Cotaçao do Euro atual: R$ {cotacao_euro}') # Mostrando a cotação em Euro

cotacao_bitcoin = cotacoes['BTCBRL']["bid"] # Solicitando a cotação em Bitcoin
print(f'Cotaçao do Bitocin atual: R$ {cotacao_bitcoin}') # Mostrando a cotação em Bitcoin

