from redis import StrictRedis
from weixin.config import *
from pickle import dumps, loads
from weixin.requests import WeixinRequest


class RedisQueue():
    def __init__(self):
        '''
        初始化Redis
        '''
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self, request):
        '''
        向队列添加序列化后的Request
        :param request: 失败次数
        :return: 添加结果
        '''
        if isinstance(request, WeixinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))
        return False

    def pop(self):
        '''
        取出下一个Request并反序列化
        :return:
        '''
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop((REDIS_KEY)))
        else:
            return False
