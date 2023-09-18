import requests

url = 'https://httpbin.org/uuid'  # URL for retrieving a UUID4

# Make the GET request to retrieve the UUID4
res = requests.get(url)

# Check if the request was successful (status code 200)
if res.status_code == 200:
    uuid4 = res.text.strip()  # Get the UUID4 string from the response and remove leading/trailing whitespace
    print("UUID4:", uuid4)
else:
    print("Error:", res.status_code)