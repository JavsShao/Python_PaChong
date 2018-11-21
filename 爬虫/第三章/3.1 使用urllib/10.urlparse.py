from urllib.parse import urlparse


# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
result = urlparse('https://www.baidu.com/s?wd=fragment&rsv_spt=1&rsv_iqid=0xe1d236230004ed21&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=2&rsv_sug1=1&rsv_sug7=001')
print(type(result),result)