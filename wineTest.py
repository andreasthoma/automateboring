import requests

headers = {
  'Accept': 'application/json',
  'Authorization': 'Token 2415d176baf5bc53c2f748d5ca7df85dfd374e18'
}

# parameters = {'wine'}

response = requests.get('https://api.globalwinescore.com/globalwinescores/latest/?114959', headers=headers)

responseBody = response.json()

print(responseBody.items())

# parameters = {'wine': 'id'}
#
# response = requests.get('https://api.globalwinescore.com/globalwinescores/latest/?114959', params = parameters)
#
# data = response.json()
#
# print(response)
