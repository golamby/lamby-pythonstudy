import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def get_browser(headless:bool):
    service = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    chrome_options = Options()

    if headless:
        # 设置headless模式
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 防止selenium被检测出来
        chrome_options.add_argument('--disable-gpu')

    # 设置headless模式下的屏幕大小
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('--start-maximized')

    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    browser_ = webdriver.Chrome(service=service, options=chrome_options)
    return browser_


url = r'http://www.baidu.com'
browser = get_browser(headless=True)
browser.get(url)

time.sleep(1)
browser.save_screenshot('baidu.png')
print('拍摄完毕')
