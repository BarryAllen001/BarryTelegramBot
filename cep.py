import requests


def CEP(message):

    request = requests.get('https://brasilapi.com.br/api/cep/v1/' +
                           message.text.replace('@ghostvd_bot', '').replace('/cep ', '')).json()

    if 'message' not in request:
        cep = request.get('cep')
        cidade = request.get('city')
        uf = request.get('state')
        vizinhanca = request.get('neighborhood')
        rua = request.get('street')

        return f'''*
>>> ENCONTRADO !! <<<

CEP: {cep}
Município: {cidade} - {uf}
Vizinhança: {vizinhanca}
Rua: {rua}

>>> @BarryDc <<<*'''

    else:
        return '''*
>>> ERRO <<<

CEP invalido

>>> ERRO <<<*'''
