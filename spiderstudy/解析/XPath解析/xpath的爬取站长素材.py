# 爬取站长素材唯美风景的图片描述和图片地址
# 定制请求对象
# 爬取网页源码
# xpath解析
import json
import urllib.request
from lxml import etree

headers_dic = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36 '
}


def creat_request(page):
    if page == 1:
        url = r'https://sc.chinaz.com/tupian/weimeifengjing.html'
    else:
        url = f'https://sc.chinaz.com/tupian/weimeifengjing_{page}.html'

    req = urllib.request.Request(url=url, headers=headers_dic)
    return req


def get_content(req) -> str:
    resp = urllib.request.urlopen(req)
    html_content = resp.read().decode('utf-8')

    return html_content


def down_load(html_content):
    tree = etree.HTML(html_content)

    pic_list = tree.xpath('//img[contains(@data-original,*)]/@data-original')
    # '/html/body/div[3]/div[2]/div[1]/img' 从浏览器复制的xpath路径
    name_list = tree.xpath('//img[contains(@data-original,*)]/@alt')
    for index, pic_uri in enumerate(pic_list):
        pic_list[index] = 'https:' + pic_uri.replace("_s", '')

    new_list = zip(pic_list, name_list)
    pic_dic = {}
    for item in new_list:
        print(item)
        pic_dic[f'{page}_{item[1][:-6]}'] = item[0]
    with open(f'../../../data/scene_pic.json', mode='w', encoding='utf-8') as f:
        json.dump(pic_dic, f, ensure_ascii=False)


if __name__ == '__main__':
    start_page = int(input("请输入起始页"))
    end_page = int(input("请输入终止页"))

    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        content = get_content(request)
        down_load(content)
    with open('../../../data/scene_pic.json', mode='r', encoding='utf-8') as f:
        res = json.load(f)
    print(res, type(res))
