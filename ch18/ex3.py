# JSON contents

import requests

# URL of the API endpoint
url = 'https://api.example.com'

# Sending a GET request
response = requests.get(url)

#fetching JSON contents
json_data = response.json()
print(json_data)

# using the json parameter 
# URL of the API endpoint
url = 'https://api.example.com'

# JSON data to send in the request body
data = {
    'key1': 'value1',
    'key2': 'value2'
}
# Sending a POST request
response = requests.post(url, json=data)
