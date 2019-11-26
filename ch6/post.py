import requests

rs = requests.post("http://127.0.0.1:8080/", data={"name": "IAMPOST"})
print(rs.text)