import requests


def MD5(message):

    request = requests.get('https://api.hashify.net/hash/md5/hex?value=' + message.text.replace(
        'https://', '').replace('http://', '').replace('@nomedoseubot', '').replace('/md5 ', '')).json()

    if 'message' not in request:

        return f'''*
>>> CRIPTOGRAFADO <<<

Hash: {request.get('Digest')}
Tipo: {request.get('Type')}

>>> CRIPTOGRAFADO <<<*
'''
