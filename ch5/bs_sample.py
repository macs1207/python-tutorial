from bs4 import BeautifulSoup
import requests

rs = requests.get('https://movies.yahoo.com.tw/movie_intheaters.html')
dom = BeautifulSoup(rs.text, 'lxml')
print(dom.prettify())  # 輸出排版後的HTML
