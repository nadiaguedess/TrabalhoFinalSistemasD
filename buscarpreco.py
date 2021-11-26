# -*- coding: utf-8 -*-
import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

cotacao = requisicao.json()

#retorno = 'Cotação do Dolar \n Moeda: ' + cotacao['USD']['name'] + '\n Data: ' + cotacao['USD']['create_date'] + '\nValor atual: R$' + cotacao['USD']['bid']
print ('Moeda: ' + cotacao['USD']['name'])
print ('Data: ' + cotacao['USD']['create_date'])
print('Valor atual: R$' + cotacao['USD']['bid'])

print('Cotação do Dolar')
print ('Moeda: ' + cotacao['USD']['name'])
print ('Data: ' + cotacao['USD']['create_date'])
print('Valor atual: R$' + cotacao['USD']['bid'])





