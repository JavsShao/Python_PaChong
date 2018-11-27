
from=search_tab&pd=synthesis


# 获取页面信息
def get_page(offset):
    # 请求的参数信息
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis'
    }