import requests


# r = requests.get('https://www.baidu.com')
headers = {
    'Cookie':'_zap=cae92218-d222-4ec7-bf2a-2d89f57d61b3; d_c0="ADBif-82hw6PTkb-gfykxhh7KzYfxJRBgV0=|1542372266"; _xsrf=qjbIN7zXO8vBRsPaYLfE4yj2bgpe2TI1; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186; capsion_ticket="2|1:0|10:1542804771|14:capsion_ticket|44:MjM1Njg2MGRiZmE0NGJkYzk5M2M2MTgzNzM4NDU3MDg=|dfdf11fd2353a1dc29af4caea4367edaa68e27791874fc1240f0adebf0fbaaa7"; z_c0="2|1:0|10:1542804780|4:z_c0|92:Mi4xalo4QUFnQUFBQUFBTUdKXzd6YUhEaVlBQUFCZ0FsVk5MS1BpWEFDZEFtVFdxYmxRcFFzTWpRMWxIQnFGVnVjNWZR|4ec03db3b6d13d255f1f50c3d02b528222a0c83c7e0dbc1b12cda002473d524e"; tst=r; q_c1=d0bda32c28c44bdca9fc55208ee41553|1542804790000|1542804790000; __gads=ID=710cf2f6a7656b01:T=1542804792:S=ALNI_MZwSSr8NZECbDsFBTm27Ls9CV2xFg',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    # 'Host':'www.zhihu.com'
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
print(r.text)
