import requests

def ConCNPJ(message):

    request = requests.get('https://www.receitaws.com.br/v1/cnpj/' + message.text.replace(
        'https://', '').replace('http://', '').replace('@nomedoseubot', '').replace('/cnpj ', '')).json()

    if 'message' not in request:

        return f'''*
>>> ENCONTRADO !! <<<

Nome: {request.get('nome')}
Telefone: {request.get('telefone')}
Email: {request.get('email')}
Situação: {request.get('situacao')}
Porte: {request.get('porte')}
Abertura: {request.get('abertura')}
Natureza juridica: {request.get('natureza_juridica')}
Ultima atualização: {request.get('ultima_atualizacao')}
CNPJ: {request.get('cnpj')}

>>> @BarryDc <<<
*
'''
    else:
        return '*CNPJ invalido*'
