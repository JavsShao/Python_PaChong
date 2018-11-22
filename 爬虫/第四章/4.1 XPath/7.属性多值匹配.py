from lxml import etree


text = '''
    <li class="li li-first"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()')
# result = html.xpath('//li[@class="li li-first"]/a/text()')
result = html.xpath('//li[contains(@class, "li-first")]/a/text()')
print(result)