import json
import urllib.request
import urllib.parse


def creat_request(start):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
    }
    data_dic = {
        'start': (start - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data_dic)
    url = base_url + data

    return urllib.request.Request(url=url, headers=headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    return content


def down_load(start, content):
    with open('../../data/douban' + str(start) + '.json', mode='w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页'))
    end_page = int(input('请输入终止页'))

    for start in range(start_page, end_page + 1):
        request = creat_request(start)
        content = get_content(request)
        down_load(start, content)
