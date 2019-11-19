import requests
from bs4 import BeautifulSoup

print("Yahoo!奇摩電影 上映中清單")
for page in range(1, 3):
    rs = requests.get(
        'https://movies.yahoo.com.tw/movie_intheaters.html?page=' + str(page))
    dom = BeautifulSoup(rs.text, 'lxml')
    name = dom.select('.release_list li div.release_movie_name a')
    en_name = dom.select('li .en')
    count = dom.select('li .count')
    span = dom.select('li dt .leveltext span')
    print("第" + str(page) + "頁")
    for idx in range(len(en_name)):
        print("  電影中文名稱：" + name[idx * 2].text)
        print("  電影英文名稱：" + en_name[idx].text)
        print("  滿意度：" + count[idx].attrs['data-num'])
        print("  期待度：" + span[idx].text)
        print()
