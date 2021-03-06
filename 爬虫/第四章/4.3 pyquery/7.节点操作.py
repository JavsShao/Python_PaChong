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
# li = doc('.item-0.active')
# print(li)

# li.remove_class('active')
# print(li)
#
# li.add_class('qq')
# print(li)

li = doc('.item-0.active')
li.attr('name','link')
print(li)

li.text('我是Hamdi')
print(li)

print(li.html())
print(li.text())

li.html('<span>我是HAMDI')
print(li)