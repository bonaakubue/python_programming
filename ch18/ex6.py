# Response Headers

import requests
# Send a GET request
response = requests.get('https://example.com')

# Access the response headers
headers = response.headers
# Print all the headers
# Access specific headers
content_type = headers.get('content-type')
server = headers.get('server')

# Print specific headers
print(f"Content-Type: {content_type}")
print(f"Server: {server}")

# Custom headers
headers = {
    'User-Agent': 'Custom User Agent',
    'Authorization': 'Token',
    'Custom-Header': 'Value'
}

# Send a GET request with custom headers
response = requests.get('https://example.com', headers=headers)
