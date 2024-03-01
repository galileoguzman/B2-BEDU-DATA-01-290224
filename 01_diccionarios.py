user = {
    'username': 'galo',
    'email': 'galo@gmail.com',
    'age': 34,
    'is_married': True,
    'city': 'Puerto Escondido',
    'bin_number': '4111-1111-1111-1111',
    'expiration_credit_card': '03/26',
    'is_credit_card_default': False
}

print(type(user))

# Acceso a llave/propiedad

email = user['email']
print(email)
print(type(email))

is_married = user['is_married']
print(is_married)
print(type(is_married))

# Acceso a llave/propiedad

student = {
    'name': 'Galileo Guzman',
    'scores': [
        9,
        5,
        7,
        8,
        8,
        9
    ]
}

print(type(student))

scores = student['scores']
scores_sum = 0

for s in scores:
    scores_sum = scores_sum + s

total_scores = len(student['scores'])
mean = scores_sum / total_scores
print(mean)