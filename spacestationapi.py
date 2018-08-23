import requests


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

data = response.json()

# Print the content of the response (the data the server returned)
print(type(data))
print(data)

# # This gets the same data as the command above
# response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# print(response.content)
