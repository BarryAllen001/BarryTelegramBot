import requests

def BIN(message):

    try:
        request = requests.get(
            'https://lookup.binlist.net/' + message.text.replace('@nomedoseubot', '').replace('/bin ', '')).json()
        bandeira = request.get('scheme')
        tipo = request.get('type')
        pais = request.get('country')
        banco = request.get('bank')
        nivel = request.get('brand')

        return f'''*
>>> ENCONTRADO !! <<<

Bandeira: {bandeira}
Tipo: {tipo}
Nivel: {nivel}
Pais: {pais.get('name')} {pais.get('emoji')}
Banco: {banco.get('name')}

>>> @BarryDc <<<*'''

    except(ValueError, AttributeError):
        return '''*
>>> Bin não encontrada <<<*'''
