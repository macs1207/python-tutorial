import requests

url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"

rs = requests.get(url)
with open("logo.png", "wb") as f:
    f.write(rs.content)
