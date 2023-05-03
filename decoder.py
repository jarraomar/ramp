import base64
import urllib.request

url = "https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev"
response = urllib.request.urlopen(url)
data = response.read()
decoded_data = base64.b64decode(data)

with open("base64_prompt.txt", "wb") as f:
    f.write(decoded_data)