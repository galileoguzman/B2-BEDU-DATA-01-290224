import requests

url = 'https://api.github.com/users/pamelafox'

# Fetching user
response = requests.get(url)
user = response.json()

# Download avatar photo
avatar_response = requests.get(user['avatar_url'])
if avatar_response.status_code == 200:
    content = avatar_response.content
    filename = f'tmp/photo.png'
    with open(filename, 'wb') as image:
        image.write(content)
    print("Image downloaded")

else:
    print("User does not have a photo")