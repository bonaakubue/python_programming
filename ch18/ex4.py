# Sending files

import requests

# URL of where you want to send the POST request
url = 'https://example.com'

# File to send in the request
file_path = 'data.txt'

# Sending the POST request with the file
with open(file_path, 'rb') as file:
    files = {'file': file}
response = requests.post(url, files=files)
