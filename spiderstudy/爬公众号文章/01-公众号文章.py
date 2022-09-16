import time
import urllib.parse

import requests
import parsel
import csv

f = open('公众号文章.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '公众号', '文章发布时间', '文章地址'])
csv_writer.writeheader()

keywords = input('请输入你的关键字')
data_dic = {
    'query':keywords
}
keystr = urllib.parse.urlencode(data_dic)
print(keystr)
for page in range(1, 3):
    url = f'https://weixin.sogou.com/weixin?{keystr}&_sug_type_=&sut=2644&lkt=1%2C1663055195439%2C1663055195439&s_from=input&_sug_=y&type=2&sst0=1663055195540&page={page}&ie=utf8&w=01019900&dr=1'
    print(url)
    headers = {
        'Cookie': 'IPLOC=CN4301; SUID=814127771639960A0000000063203417; SUV=1663054878462212; ld=Glllllllll20wRytlllllpGk2xZlllllNhNxkyllll9lllllRylll5@@@@@@@@@@; LSTMV=217,80; LCLKINT=2477; ABTEST=0|1663054879|v1; JSESSIONID=aaaLGYMcYTmkJaitTAWky; PHPSESSID=5pf8e8p3oq8riltmbre8juqmu0; SNUID=1ACAADFD8A8F6300D1307AB68B1A420B; ariaDefaultTheme=undefined',
        'Host': 'weixin.sogou.com',
        'Referer': f'https://weixin.sogou.com/weixin?{keystr}&_sug_type_=&sut=2644&lkt=1,1663055195439,1663055195439&s_from=input&_sug_=y&type=2&sst0=1663055195540&page=2&ie=utf8&w=01019900&dr=1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
    }
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    lis = selector.css('.news-list li')
    for li in lis:
        title_list = li.css('.txt-box h3 a::text').getall()
        num = len(title_list)
        if num == 1:
            title_str = keywords + title_list[0]
        else:
            title_str = keywords.join(title_list)

        href = li.css('.txt-box h3 a::attr(href)').get()
        article_url = 'https://weixin.sogou.com' + href
        name = li.css('.s-p a::text').get()
        date = li.css('.s-p::attr(t)').get()
        timeArray = time.localtime(int(date))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        dit = {
            '标题': title_str,
            '公众号': name,
            '文章发布时间': otherStyleTime,
            '文章地址': article_url,
        }
        csv_writer.writerow(dit)
        print(title_str, name, otherStyleTime, article_url)
        time.sleep(1)
