import requests

url = "http://webap.nkust.edu.tw/nkust/perchk.jsp"
payloads = {
    "uid": "",
    "pwd": ""
}

rs = requests.post(url, data=payloads)
print(rs.status_code)
print(rs.text)
