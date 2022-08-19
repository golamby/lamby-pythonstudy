import requests

# requests库的几个方法：
# 1.get
# 2.post
# 3.cookie
# 4.代理


url = r'https://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36 ',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'BIDUPSID=6EA6A380F5DC1B26B15A6EA2876DB709; PSTM=1604118013; HMACCOUNT_BFESS=E28F012124B58945; '
              '__yjs_duid=1_7a519174a2e5ae18f51eff6d6f75a8041628700661308; '
              'BDUSS=gyZ2VyUEwxUzRSbXVPTTh4ZERmYmp4NzFGakEybmxVVzNVVm5iYVIxYTNmNHRpSVFBQUFBJCQAAAAAAAAAAAEAAABrEgz'
              '-eWJjMTIxMjQ0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALfyY2K38mNiM3; '
              'BDUSS_BFESS'
              '=gyZ2VyUEwxUzRSbXVPTTh4ZERmYmp4NzFGakEybmxVVzNVVm5iYVIxYTNmNHRpSVFBQUFBJCQAAAAAAAAAAAEAAABrEgz'
              '-eWJjMTIxMjQ0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALfyY2K38mNiM3; '
              'BAIDUID=57EC0EC28D299E8B3A1238447B36A47E:FG=1; ZFY=8v:BJg04favKRB9aPqUbpKNOnr1E5By7DAPPhyL4vOOU:C; '
              'BAIDUID_BFESS=57EC0EC28D299E8B3A1238447B36A47E:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; '
              'BA_HECTOR=202ka18h8k000g04ah2n8d861hftsa217; BDRCVFR[bOqe_OrD6-R]=mk3SLVN4HKm; delPer=0; BDRCVFR['
              'feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; BDRCVFR[cr1WKeKsI5T]=OjjlczwSj8nXy4Grjf8mvqV; '
              'H_PS_PSSID=37149_36554_36625_36884_36917_37003_37123_37136_26350_36863_37203; '
              'ab_sr=1.0'
              '.1_NjEwZDE2ZTY4NDViYjViNWZhNmMyN2VlOGFkMTkyY2IzN2UxZjU1MjkyOGU0OGM4ZDRhNjI0MWE2MTg3NmYxOTFhMDc5MTEzNGJiNTY3YWJkNGU0YThiNDViYTVkYTFjYWJjNWNkMWQ0ZjVlMzczZmNiZjIwYmYyYTQ3MTcxNjdiNGZhZjEzNmI5ZDVkODFhYWRkNGIwYjJhMTE5MDUzZg== '
}
data = {
    'wd': '长沙'
}

resp = requests.get(url=url, params=data, headers=headers)
resp.encoding = 'utf-8'
content = resp.text
print(content)

# 相比于urllib的优势：
# 1.不需要Request的定制
# 2.params传递参数
# 3.不需要urlencode编码
# 4.请求地址后面的？可以不加
