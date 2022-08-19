from bs4 import BeautifulSoup

# 根据标签名查找,只能找到第一个
soup = BeautifulSoup(open('BeautifulSoup的基本使用.html', mode='r', encoding='utf-8'), 'lxml')
print(soup.a)  # 标签元素
print(soup.a.attrs)  # 返回一个字典

# bs4的函数
# 返回的是第一个符合条件的元素
print('*' * 50 + 'find')
print(soup.find('a'))
print(soup.find('a', title="a2"))
print(soup.find('a', class_="a1"))  # 注意这个class_加了下划线
# 返回的是所有符合条件的元素

print('*' * 50 + 'find_all')
all_a = soup.find_all('a')
print(all_a, type(all_a[0]))
print(soup.find_all(['a', 'span']))
print(soup.find_all('li', limit=2))

# 根据选择器得到
# 这个和js的选择器操作DOM很像
# soup.select()
print('*' * 50 + 'select')
print(soup.select('li'))  # 元素选择器
print(soup.select('.a1'))  # 类选择器
print(soup.select('#fa'))  # id选择器
# 属性选择器
print(soup.select('a[title]'))
print(soup.select('a[class="a1"]'))

# 层级选择器
# 后代选择器
print(soup.select('div a'))

# 子代选择器
print(soup.select('div > ul > li'))

# 所有的li和a
print(soup.select('li,a'))

d1_obj = soup.select('#d1')[0]

# 如果元素中还有其他标签，那么string获取不到文本数据
# get_Text()可以正常获取，
# print(d1_obj.string)
print(d1_obj.get_text())

p1_obj = soup.select('#p1')[0]
print(p1_obj.name)
print(p1_obj.attrs)  # 返回一个字典
