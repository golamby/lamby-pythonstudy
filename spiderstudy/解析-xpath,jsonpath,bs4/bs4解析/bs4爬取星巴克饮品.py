import json
import urllib.request
from bs4 import BeautifulSoup

url = r'https://www.starbucks.com.cn/menu/beverages/'

req = urllib.request.Request(url=url)

resp = urllib.request.urlopen(req)

content = resp.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')

ul_list = soup.select('ul[class="grid padded-3 product"] ')

starBucks = {
    'drinks': []
}
drink_series = {
    'series_name': '',
    'products': []
}
print(ul_list[0])
print(ul_list[0].select('strong'))
print(ul_list[1].select('h3')[0].get_text())
print(len(ul_list))

for index, ul_ele in enumerate(ul_list):
    drink_series = {
        'series_name': '',
        'products': []
    }
    products = ul_list[index].select('strong')
    series_name = ul_list[index].select('h3')[0].get_text()
    drink_series['series_name'] = series_name
    for product in products:
        drink_series['products'].append(product.string)
    print(drink_series)
    starBucks['drinks'].append(drink_series)

print(starBucks)

with open('../../../data/bs4_starBucks.json', mode='w', encoding='utf-8') as f:
    json.dump(starBucks, f, ensure_ascii=False)
