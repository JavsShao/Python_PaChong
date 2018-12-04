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
