from lxml import etree


html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//*')
print(result)

# 获取的是HTML文件中的所有节点