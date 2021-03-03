def UserID(message):

    return f'''
*Ola {message.from_user.first_name}*

*Nome ✗*: `{message.from_user.first_name}`
*Username ✗*: `{message.from_user.username}`
*ChatID ✗*: `{message.from_user.id}`

*Identificado {message.from_user.first_name}*'''

