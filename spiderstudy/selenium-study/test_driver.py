from selenium import webdriver

path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome(path)
url = 'https://www.csdn.net/'
# 发送请求
browser.get(url)

content = browser.page_source
# browser.maximize_window()
