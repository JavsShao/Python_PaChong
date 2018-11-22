from lxml import etree


html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)

result = html.xpath('//li/@class')
print(result)