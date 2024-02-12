# Set read timeout to 10 seconds

import requests

timeout = 5
response = requests.get('https://example.com', timeout=timeout)
