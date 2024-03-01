user_1 = {
    'username': 'galo',
    'email': 'galo@gmail.com',
    'age': 34,
    'is_married': True,
    'city': 'Puerto Escondido',
    'bin_number': '4111-1111-1111-1111',
    'expiration_credit_card': '03/26',
    'is_credit_card_default': False
}

user_2 = {
    'username': 'galo 2',
    'email': 'galo@gmail.com',
    'age': 34,
    'is_married': True,
    'city': 'Puerto Escondido',
    'is_credit_card_default': False
}

users = []
users.append(user_1)
users.append(user_2)

for u in users:
    # print(u['expiration_credit_card'])
    print(u.get('expiration_credit_card', '00/00'))

# Acceso a llave/propiedad

print('Proceso finalizado')