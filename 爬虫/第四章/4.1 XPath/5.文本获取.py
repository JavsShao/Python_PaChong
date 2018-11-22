from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

print("------获取li标签下的所有文本----------")
result = html.xpath('//li/a/text()')
print(result)
