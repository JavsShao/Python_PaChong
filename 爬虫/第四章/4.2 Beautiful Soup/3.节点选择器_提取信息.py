from bs4 import BeautifulSoup


html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Hamdi"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

soup = BeautifulSoup(html, 'lxml')
# 获取名称
print(soup.title.name)

# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
# 简化后
print(soup.p['name'])
print(soup.p['class'])

# 嵌套选择
print(soup.head)
print(soup.head.title)
print(soup.head.title.string)
print(soup.head.title.string[1])

# 关联选择
# print(soup.p.contents)
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i,child)

# 提取信息
print(soup.a.next_sibling)