from selenium import webdriver
from selenium.webdriver.common.by import By  # 类似于一个枚举类

path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

browser = webdriver.Chrome(path)

url = r'https://www.baidu.com'
browser.get(url)

import time

time.sleep(1)

# 元素定位
text_span = browser.find_element(By.ID, 'kw')
print(text_span)
text_span.send_keys('周杰伦')

time.sleep(2)
search_button = browser.find_element(By.ID, 'su')
search_button.click()

time.sleep(2)
# 执行js代码
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

next_button = browser.find_element(By.XPATH, '//a[@class="n"]')
next_button.click()

time.sleep(2)

# 回退
browser.back()

time.sleep(2)
# 向前
browser.forward()

time.sleep(2)

browser.quit()
