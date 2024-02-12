# Sending a POST request

import requests

# Sending the POST request
url = 'https://example.com'

data = {
    'key1': 'value1',
    'key2': 'value2'
}
response = requests.post(url, data=data)
