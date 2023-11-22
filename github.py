import requests

print('GitHub Users')

username = input('Digit the username ... ')

url = f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f'Name: {data["name"]}')
    print(f'Bio: {data["bio"]}')
else:
    print('Cannot find this user')