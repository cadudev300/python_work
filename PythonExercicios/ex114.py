import requests

try:
    site = requests.get('https://pudim.com.br/')
except:
    print('Não foi possivel acessar o site do pudim :( )')
else:
    print('Consegui acessar o site do pudim com sucesso :)')
    print(site.request.url)