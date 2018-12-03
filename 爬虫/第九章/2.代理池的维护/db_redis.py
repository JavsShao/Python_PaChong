import redis
from .settings import *


class RedisClient(object):
    def __init__(self,host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        '''
        初始化
        :param host: Redis地址
        :param port: Redis端口
        :param password: Redis密码
        '''
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
