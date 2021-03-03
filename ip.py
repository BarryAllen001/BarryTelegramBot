import requests


def IP(message):

    request = requests.get('http://ip-api.com/json/' + message.text.replace(
        'https://', '').replace('http://', '').replace('@nomedoseubot', '').replace('/ip ', '')).json()

    if 'message' not in request:

        return f'''
*IP: {request.get('query')}
Pais: {request.get('country')}
Estado: {request.get('regionName')}
Cidade: {request.get('city')}
Provedor: {request.get('isp')}
Latitude: {request.get('lat')}
Longitude: {request.get('lon')}
Timezone: {request.get('timezone')}
As: {request.get('as')}*
'''
    else:
        return '*IP invalido*'
