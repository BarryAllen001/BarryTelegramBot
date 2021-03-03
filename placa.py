import requests

def PLACA(message):

    message = message.text.replace(
        '@nomedoseubot', '').replace('/placa ', '').replace('-', '')

    try:
        request = requests.get(
            f'https://apicarros.com/v2/consultas/{message}/f63e1e63dd231083d38ce929984aac7d', verify=False).json()

        mensagemRetorno = request.get('mensagemRetorno')
        modelo = request.get('modelo')
        marca = request.get('marca')
        ano = request.get('ano')
        anoModelo = request.get('anoModelo')
        chassi = request.get('extra')
        cor = request.get('cor')
        situacao = request.get('situacao')
        cidade = request.get('municipio')
        uf = request.get('uf')

        return f'''*
>>> ENCONTRADO!!! <<<

Retorno da api: {mensagemRetorno}
Placa: {message.upper()}
Modelo: {modelo.title()}
Marca: {marca}
Ano: {ano}/{anoModelo}
Cor: {cor}
Situacao: {situacao}
Municipio: {cidade.title()} - {uf}
Chassi: {chassi.get('chassi')}

>>> @NearShelby_yt <<<*'''

    except(ValueError, AttributeError):
        return '''*
>>> ERRO !!! <<<

Retorno da api: Placa Invalida favor usar o formato AAA0X00 ou AAA9999

>>> ERRO !!! <<<*'''
