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
# li = doc('.item-0.active')
# print(li)
# print(str(li))

# 对于多个节点的结果，我们就需要遍历来获取了。
lis = doc('li').items()
for li in lis:
    print(li)