import requests

url = "http://httpbin.org/get"
my_params = {'key1': 'value1', 'key2': 'value2'}
rs = requests.get(url, params=my_params)
print("原本的URL:{}".format(url))
print("改變後URL:{}".format(rs.url))
