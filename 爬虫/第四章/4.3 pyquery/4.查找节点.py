from pyquery import PyQuery


html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc = PyQuery(html)
# # items = doc('#container .list li')
# items = doc('.list')
# lis = items.find('li')
# print(items)

# 父节点和祖先节点
items = doc('.list')
container = items.parents()
print(container)