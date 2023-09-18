import requests

url = 'https://httpbin.org/image/png'  # URL for downloading the image

# Make the GET request to download the image
res = requests.get(url)

# Check if the request was successful (status code 200)
if res.status_code == 200:
    # You can save the image to a file
    with open('downloaded_image.png', 'wb') as file:
        file.write(res.content)
    print("Image downloaded successfully.")
else:
    print("Error:", res.status_code)