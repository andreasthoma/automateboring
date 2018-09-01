import requests

'Authorization: Token 2415d176baf5bc53c2f748d5ca7df85dfd374e18'


parameters = {'wine': 'id'}

response = requests.get('https://api.globalwinescore.com/globalwinescores/latest/?114959')

data = response.json()

print(response)
