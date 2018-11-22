from lxml import etree


text = '''
    <li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
# result = html.xpath('//li[@class="li"]/a/text()')
# result = html.xpath('//li[@class="li li-first"]/a/text()')
result = html.xpath('//li[contains(@class, "li-first") and @name="item"]/a/text()')
print(result)