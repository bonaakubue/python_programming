import requests

# Create a session
session = requests.Session()

# Send a GET request using the session
response = session.get('https://example.com/')

# Close the session
session.close()
