'''
限定符：
    x* # x出现0次或多次
    x+ # x出现1次或多次
    x? # x出现0次或1次
    x{5} # x出现5次
    x{2,5} # x出现2-5次
    x{2,} # x出现2次及以上
192.167.12
32.12.11
或运算符：
    (x|y)     # 匹配x或y
    (xy)|(gy) # 匹配xy或gy

字符类:
    [abc]   # 匹配a或b或c
    [a-c]   # 匹配a或b或c
    [a-zA-Z0-9] # 匹配小写字母或者大写字母或者数字
    [^0-9] # 匹配非数字字符

元字符:
    \d # 匹配数字字符
    \D # 匹配非数字字符
    \w # 匹配单词字符（字母、数字、下划线）
    \W # 匹配非单词字符
    \s # 匹配空白字符（包括空格、换行符、制表符）
    \S # 匹配非空白字符
    .  # 匹配任意字符（换行符除外）
    \b # 标注字符的边界
    ^  # 匹配行首
    $  # 匹配行尾

贪婪匹配、懒惰匹配
    + # 贪婪匹配任意字符（换行符除外）
    +? # 懒惰匹配任意字符（换行符除外）

注：如果需要匹配正则里面的特殊字符，可以在符号前面加\，和Python里面字符串防止转义一样


分组语法 捕获
    (exp) 匹配exp,并捕获文本到自动命名的组里
    (?<name>exp) 匹配exp,并捕获文本到名称为name的组里，也可以写成(?'name'exp)
    (?:exp) 匹配exp,不捕获匹配的文本
位置指定
    (?=exp) 匹配exp前面的位置
    (?<=exp) 匹配exp后面的位置
    (?!exp) 匹配后面跟的不是exp的位置
    (?<!exp) 匹配前面不是exp的位置
    注释
    (?#comment) 这种类型的组不对正则表达式的处理产生任何影响，只是为了提供让人阅读注释
    match方法的语法为：re.match(pattern,string,[flags=0])
        match方法是从头开始匹配的，从中间截取字符串，是无法匹配到的。这也是match方法的局限性。
        match方法匹配不到结果时，返回的是None，匹配到结果时，返回的是match对象。
        match方法匹配到结果时，使用match对象的group方法，获取匹配结果
    search方法的语法为：re.search(pattern,string,[flags=0])
        search方法是全字符串匹配的，匹配到第一个结果，即返回结果，不再继续。
        search方法匹配不到结果时，返回的是None，匹配到结果时，返回的是match对象。
        search方法匹配到结果时，使用match对象的group方法，获取匹配结果。
    findall方法的语法是：re.findall(pattern, string, flags=0)
        findall是查找字符串中所有可匹配的，并将匹配结果以列表的形式返回。如果匹配不到，则返回一个空列表。
    sub(pattern,repl,str[,count])
        sub方法使用repl替换string中每一个匹配的子串后返回替换后的字符串。
        count默认为0时，会默认替换全部，指定count值时，则按照指定次数替换。
        可匹配到时，则返回匹配到的字符串。
        无法匹配到时，则返回原始的字符串。



'''

s = '''
xg
xyyg
xyyyg
xyg
xzg
xzzzzzg
xyyyyyyg
'''

import re

print(re.findall('.+', 'abc\nef\ng\n'))
print(re.findall('.+', 'abc\nef\ng\n', flags=re.DOTALL))

# flags参数:
# re.I 不区分大小写
# re.M 让^匹配每一行的开头
# re.S #让.匹配所有字符（包括换行符）

print(re.findall('^x', s, flags=re.M))

s2 = r'''
<p> 11-13   <a   href=/bj/11/109/4969873.html   target=_blank> 中介   -   3400元/3居   -   紫竹桥兵器大厦附近大三居   (紫竹院)   </a>
clip_image001[1]<p> 11-13   <a   href=/bj/11/104/4969872.html   target=_blank> 1200元/3居   -   出租上地三居室合住（免中介费）   (上地)   </a>
clip_image001[2]<p> 11-13   <a   href=/bj/11/114/4969866.html   target=_blank> 中介   -   2600元/2居   -   北太平庄43号院二居出租   (北太平庄)   </a>
clip_image001[3]<p> 11-13   <a   href=/bj/11/914/4969865.html   target=_blank> 400元/1居   -   单间独立卫浴免供暖费   (北七家)   </a>
clip_image001[4]<p> 11-13   <a   href=/bj/11/301/4969864.html   target=_blank> 中介   -   2400元/2居   -   东直门春秀路太平庄南里二居室出租   (东直门外三里屯工人体育馆)   </a>
clip_image001[5]<p> 11-13   <a   href=/bj/11/208/4969863.html   target=_blank> 中介   -   2400元/4居   -   出租定福家园新房四居室   (团结湖)   </a>
clip_image001[6]<p> 11-13   <a   href=/bj/11/214/4969862.html   target=_blank> 中介   -   2600元/3居   -   花家地北里三室一厅出租   (酒仙桥 将台路)   </a>
clip_image001[7]<p> 11-13   <a   href=/bj/11/209/4969859.html   target=_blank> 1300元/1居   -   十里堡华堂附近新公寓合租   (京广桥 红庙 八里庄)   </a>
clip_image001[8]<p> 11-13   <a   href=/bj/11/70/4969846.html   target=_blank> 中介   -   600元/3居   -   出租丰益桥西盛鑫家园4室2厅2卫精装修的房子(免收中介费   (丰益桥西盛鑫家园)   </a>
clip_image001[9]<p> 11-13   <a   href=/bj/11/901/4969844.html   target=_blank> 750元/3居   -   田园风光雅园３居中的一居室出租   (回龙观)   </a>
clip_image001[10]<p> 11-13   <a   href=/bj/11/1101/4969840.html   target=_blank> 350元/1居   -   找一女孩跟我合租   (亦庄)   </a>
clip_image001[11]<p> 11-13   <a   href=/bj/11/102/4969839.html   target=_blank> 中介   -   3400元/3居   -   出租知春里小区三居室   (北京大学)   </a>
clip_image001[12]<p> 11-13   <a   href=/bj/11/217/4969838.html   target=_blank> 1100元/3居   -   双井桥 三居 出租 （新装修的）合租   (双井)   </a>
clip_image001[13]<p> 11-13   <a   href=/bj/11/70/4969837.html   target=_blank> 中介   -   3500元/3居   -   丰台区兆丰园精装修房子一套低价出租   (玉泉路 吴家村)   </a>
clip_image001[14]<p> 11-13   <a   href=/bj/11/70/4969835.html   target=_blank> 中介   -   2900元/3居   -   我有一套长安新城精装修的三居室要出租   (青塔 大成路 长安新城)   </a>
clip_image001[15]<p> 11-13   <a   href=/bj/11/201/4969834.html   target=_blank> 中介   -   2200元/1居   -   房屋出租，北辰附近   (亚运村)   </a>

'''
# (?<=<a\s+href=(?<link>.*?(?=\starget=)).*?>(?<content>.*?)(?=</a>))
#
p1 = r'((?<=<a).*href=(?P<link>.*?(?=\starget=)).*k)>'
pattern1 = re.compile(p1)
pattern1.search(s2)

list = pattern1.findall(s2)
for sublist in list:
    print(sublist)
