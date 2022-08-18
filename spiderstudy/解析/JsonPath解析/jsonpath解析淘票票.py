import json
import jsonpath

import urllib.request

url = r'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1660832974915_108&jsoncallback=jsonp109&action' \
      r'=cityAction&n_s=new&event_submit_doGetAllRegion=true '

headers_dic = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1660832974915_108&jsoncallback=jsonp109&action=cityAction&n_s=new'
    #          '&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v': '2.2.2',
    'cache-control': 'no-cache',
    'cookie': 'cna=0S2hGInTHjICAXjQEH11wJeE; miid=77524880237734988; t=1b55928e89b77be56832ab4ee2ebf389; '
              'cookie2=1405add9ccfecddb07df747560c0cfe4; v=0; _tb_token_=7830bfe583333; xlly_s=1; tb_city=140800; '
              'tb_cityName="1Muzxw=="; l=eBQBTuE4jUhYvZLfBO5CPurza77OoIRb4PVzaNbMiInca6GRtFGjJNCH8ZPDSdtjgtCAAeKrn'
              '-NCCdLHR3ji5c0c07kqm0Sr3xvO.; tfstk=caRhBNw3ppWQj3Y2zB1IZ4cBMBMAZEDFAQRw_2ie5A-pa6RNiYya3BojSMnjY81..; '
              'isg=BICAfKHI9r36E4gOQN268r7WUQ5SCWTTaK-SofoRzRsudSCfoxiYYwYLjd21QByr',
    'pragma': 'no-cache',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
    'x-requested-with': 'XMLHttpRequest',
}

req = urllib.request.Request(url=url, headers=headers_dic)
resp = urllib.request.urlopen(req)

content = resp.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]

with open('../../../data/jsonpath_淘票票.json', mode='w', encoding='utf-8') as f:
    f.write(content)

with open('../../../data/jsonpath_淘票票.json', mode='r', encoding='utf-8') as f:
    json_obj = json.load(f)

print(jsonpath.jsonpath(json_obj, '$.returnValue.Y[?(@.regionName == "运城")]'))
