# import requests
import requests

#send a GET request
response = requests.get('https://example.com')

#check the status
status = response.status_code
print(status)

#get content
content = response.text
print(content)

#get headers
headers = response.headers
print(headers['Content-Type'])

# Send the GET request with the query parameters
query = {
    'key1': 'value 1',
    'key2': 'value 2',
}
url = "https://example.com"
response = requests.get(url, params=query)
