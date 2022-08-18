import urllib.request
import urllib.parse
import json

url = r'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers_dic = {

    'Cookie': 'BIDUPSID=6961115F6294E574EF56F1C8DD8C2CEC; PSTM=1612252142; '
              '__yjs_duid=1_92fae3e99bb8e250c45245965921d95c1620133723004; REALTIME_TRANS_SWITCH=1; '
              'FANYI_WORD_SWITCH=1; '
              'HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; '
              'BDUSS=hoSEg1a2dTdmxtWDNvaVRad0hGSnZ'
              '-NExXQldtbTljT3JTeDBMVVBsV3Z4SzFpSVFBQUFBJCQAAAAAAAAAAAEAAADmB9VgeXl5YmJjY2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK83hmKvN4ZiRT; BDUSS_BFESS=hoSEg1a2dTdmxtWDNvaVRad0hGSnZ-NExXQldtbTljT3JTeDBMVVBsV3Z4SzFpSVFBQUFBJCQAAAAAAAAAAAEAAADmB9VgeXl5YmJjY2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK83hmKvN4ZiRT; BAIDUID=AA1941E64E5F1DEF4D91231DE90C261C:SL=0:NR=10:FG=1; APPGUIDE_10_0_2=1; newlogin=1; BAIDUID_BFESS=AA1941E64E5F1DEF4D91231DE90C261C:SL=0:NR=10:FG=1; BDRCVFR[Zh1eoDf3ZW3]=mk3SLVN4HKm; delPer=0; PSINO=1; H_PS_PSSID=26350; BA_HECTOR=akah8g200la4050l8l06192j1hfr8ua16; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; ZFY=eaODg5AOFHQHGVf6ZO6MR8SZF8gwkzetShqCyT17PRQ:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1659957970,1660789708; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1660790462; ab_sr=1.0.1_MGM5YjVjOGFhYzJlM2M5NjFkNWQ4OWEzYWYxZGFiOTFiNTQ0ODEzMWEyOTc5ODFkOWJmZmU1OWM0MTA4NDE3OTc2ODVmOGIzNjBhNmY4MTNlMTY0OTJhNTcxOGUyY2Y0ZmRmMzU1YjJjMTE3ZmJmZGMyNTkwZDkwMDUwMmQxNTIwZGQ3ZGI4ZDJjMzQzMjU0ZGM2MjkwOGY1OTlhMjJiNDZmMWRiODI1YzJlNzcxNDBiZTE5MDU3MTA4MWIzMmE4',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
    'X-Requested-With': 'XMLHttpRequest',
}

data_dic = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '10c19387d412cddceb6b9c02c285f07d',
    'domain': 'common',
}

data = urllib.parse.urlencode(data_dic).encode('utf-8')
request = urllib.request.Request(url=url, headers=headers_dic, data=data)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

result = json.loads(content)
print(result)
