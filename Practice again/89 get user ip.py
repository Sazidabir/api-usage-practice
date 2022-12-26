import requests
api_url = 'https://api64.ipify.org?format=json'
response = requests.get(api_url)
# print(response.status_code)
# print(response.json())

if response.status_code == 200:
    data = response.json()
    ip = data.get('ip')
    print('My IP address is', ip)