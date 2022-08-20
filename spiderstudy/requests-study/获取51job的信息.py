import json
import time

import requests
import re
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_browser(headless: bool):
    service = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_options = Options()

    if headless:  # 设置headless模式'
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 防止selenium被检测出来
        chrome_options.add_argument('--disable-gpu')

    # 设置headless模式下的屏幕大小
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('--start-maximized')

    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    browser_ = webdriver.Chrome(service=service, options=chrome_options)
    return browser_


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_uab_collina=164657151283206417808163; guid=3ef94edcb57349daf29ffa90e6de9291; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%223ef94edcb57349daf29ffa90e6de9291%22%2C%22first_id%22%3A%22182ba434b72dc8-080f977e3584878-45647f52-1327104-182ba434b73b63%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgyYmE0MzRiNzJkYzgtMDgwZjk3N2UzNTg0ODc4LTQ1NjQ3ZjUyLTEzMjcxMDQtMTgyYmE0MzRiNzNiNjMiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIzZWY5NGVkY2I1NzM0OWRhZjI5ZmZhOTBlNmRlOTI5MSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%223ef94edcb57349daf29ffa90e6de9291%22%7D%2C%22%24device_id%22%3A%22182ba434b72dc8-080f977e3584878-45647f52-1327104-182ba434b73b63%22%7D; acw_tc=ac11000116609870559532861e00dd6ebb73701806b4ada4fdf60220fbfa6c; acw_sc__v3=6300a6b2854ab2ac1f064ef04759b8ab004d8d2b; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAc%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FAjava%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%CA%FD%BE%DD%B7%D6%CE%F6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%600%7C%21; ssxmod_itna=YqfOY5D5DIPIhDUxBPGKiQud0IZbP6egWx=1BAx0yP2eGzDAxn40iDt==H2Q=jW7r+YfYliqx5kWp7TPFoHKERRPfFBk4GLDmKDyCQ7b+oD4SKGwD0eG+DD4DWUx03DoxGASpx0+kSBcu=nDAQDQ4GyDitDKkixxG3D0R=tQR6MB32xHeDSCBUdU0=DjqGgDBd4t1xyDDtWa1h/UMuixYPaiM0qxBQD7u2Sl8rDCoUVRLQkZgExf74jKGQ472hdbBG3z0odFYnqRF4RUU4PCAhP9iqAHsxDGSGAciD==; ssxmod_itna2=YqfOY5D5DIPIhDUxBPGKiQud0IZbP6egWx=1BDnFfuKDs5kaDLQQj=ySbis6QH2aP4uYzg+Ld5/=Y2QsebtM5KHD82gpOXjtByXdrUb0oBewo4tAc=psz9fN6qf=Bfq0NrRKHXAFoD55zbQL8xAyU3d4XMEvFwKSU0LMn8i59uK5qkQ6DL0e+73KOMdbLD50B+mrgBfk8Ptp8pLdKejVAguL0oUvBREUYcvFdCROjf5OM10d/kD8Dmnxn3ghEu8twqMIgfH6CcfqiUOwwFR8qKl4Z4OodnxjMhZfvV3+y=UxptCjEux5B+sBLdYL+1Nmcw8hQwl+x8e9hQCBfxfQxSUvepx/Ud8YK6XUc2coPh2EfhtrRAiaetm2eBiQUhDzbK26some/rj=dlmejhwHiG3/NMBQm1mk9drORZEiHYNK=0j0Pj=t6P6KfACf=V=QKKcXSff6W2iQLi9mndL/4QGQnKhfhWtPwwIaqY2OCDheQvWhWDG2UiPKG70uQbD1l4BKChc4+L24Dy4KDDFqD+6DxD==',
    'Host': 'search.51job.com',
    'Pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
}


def verifying(job_name, page):
    askURL(job_name, page)
    slider_btn = browser.find_element(By.ID, 'nc_1_n1z')
    track = get_track(260)  # 获取滑动的轨迹，此函数定义在第9点
    move_to_gap(browser, slider_btn, track)  # 进行滑动，此函数定义在第10点

    # job_details = re.findall(r'engine_jds":(.*)"adid":""}]', content)
    # print(type(job_details), len(job_details))
    # print(job_details)
    # res = json.loads(job_details)
    # print(res, type(res))


def askURL(name, pageNum):
    url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,{name},2,{pageNum}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    # 浏览器访问登录页面
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(5)
    # resp = requests.get(url=url, headers=headers)
    # resp.encoding = 'utf-8'
    # print(resp.text)
    # return resp.text


def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0

    while current < distance:
        if current < mid:
            # 加速度为正 2
            a = 40
        else:
            # 加速度为负 3
            a = -30
        # 初速度 v0
        v0 = v
        # 当前速度 v = v0 + at
        v = v0 + a * t
        # 移动距离 x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track


def move_to_gap(browser, slider, tracks):
    """
    拖动滑块到缺口处
    :param slider: 滑块
    :param tracks: 轨迹
    :return:
    """
    ActionChains(browser).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(browser).release().perform()


if __name__ == '__main__':
    job_name = input("请输入您要在前程无忧网爬取的岗位名称：")
    start_page = input('请输入要爬取python岗位的起始页数')
    end_page = input('请输入要爬取python岗位的终止页数')
    time.sleep(2)
    browser = get_browser(headless=False)

    # for page in range(start_page,end_page+1)':
    verifying(job_name, 1)
