import requests

def BANKS(message):

    request = requests.get('https://brasilapi.com.br/api/banks/v1/' + message.text.replace(
        'https://', '').replace('http://', '').replace('@nomedoseubot', '').replace('/banks ', '')).json()

    if 'message' not in request:

        return f'''*
>>> ENCONTRADO <<<

ISPB: {request.get('ispb')}
Nome: {request.get('name')}
Codigo: {request.get('code')}
Nome completo: {request.get('fullName')}

>>> ENCONTRADO <<<*
'''
    else:
        return '*Codigo bancario não encontrado*'
