import requests

def DDD(message):

    request = requests.get('https://brasilapi.com.br/api/ddd/v1/' +
                           message.text.replace('@nomedoseubot', '').replace('/ddd ', '')).json()

    if 'message' not in request:
        Estado = request.get('state')

        return f'''*
Estado: {Estado}
*'''

    else:
        return '*DDD invalido*'
