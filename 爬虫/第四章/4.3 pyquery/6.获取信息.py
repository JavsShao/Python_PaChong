from pyquery import PyQuery


html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = PyQuery(html)
a = doc('a')
# print(a.text())
# print(a.attr('href'))
for item in a.items():
    print(item.attr('href'),type(item.attr('href')))

# 获取文本内容
doc = PyQuery(html)
text = doc('li')
for item in text.items():
    print(item.text())

