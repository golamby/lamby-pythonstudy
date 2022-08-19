from lxml import etree

#xpath解析
# 本地解析   etree.parse()
# response.read().decode('utf-8')直接解析 etree.HTML()

"""
xpath的基本用法：
    1.路径查询
        //:
        /:
    2.谓词查询
        //div[@id="maincontent"]
    3.属性查询
        //@class @id @value
    4.模糊查询
        //div[contains(@class,"fli")]
        //dic[starts-with(@id,"f"))]
    5.逻辑查询
        //div[@class="aa" and @class="cc"]

"""



tree = etree.parse('01-xpath的基本使用.html')

# ele_list = tree.xpath('//ul[@id="su"]//li/text()')
# ele_list = tree.xpath('//ul//li[contains(@class,"aa")]/text()')
# ele_list = tree.xpath('//ul//li[contains(@class,"aa") or contains(@class,"cc") ]/text()')
ele_list = tree.xpath('//ul//li[@class="aa" or @class="bb"]/text()')

print(ele_list)