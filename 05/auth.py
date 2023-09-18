import requests

# Replace 'davi' and '1234' with your actual username and password
url = 'https://httpbin.org/basic-auth/davi/1234'

# Create a session and set the basic authentication credentials
session = requests.Session()
session.auth = ('davi', '1234')

# Make the GET request
res = session.get(url)

# Check the response
if res.status_code == 200:
    parsed = res.json() # JSON return
    print(parsed)
else:
    print("Authentication failed or other error:", res.status_code)