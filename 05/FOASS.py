import requests

url = "http://foass.1001010.com/pink/Davi"

headers = {
	"Accept": "application/json",
}

res = requests.get(url, headers=headers)

print(res)

if res.status_code == 200:
    parsed = res.json() # JSON return
    print(parsed)
else:
    print("Authentication failed or other error:", res.status_code)