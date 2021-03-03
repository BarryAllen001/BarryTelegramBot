import requests

def GeradorCNS(message):

    request = requests.get('http://geradorapp.com/api/v1/cns/generate?token=f01e0024a26baef3cc53a2ac208dd141').json()
    dados = request.get('data')
    numero = dados.get('number_formatted')

    return f'''
CNS: {numero}'''
