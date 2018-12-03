import redis
from random import choice

from .settings import *
from .error import *


class RedisClient(object):
    def __init__(self,host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        '''
        初始化
        :param host: Redis地址
        :param port: Redis端口
        :param password: Redis密码
        '''
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        '''
        添加代理，设置分数为最高
        :param proxy:代理
        :param scores: 分数
        :return: 添加结果
        '''
        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, score,proxy)

    def random(self):
        '''
        随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，否则异常
        :return: 随机代理
        '''
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError

    def decrease(self, proxy):
        '''
        代理值减1分，分数小于最小值，则代理删除
        :param proxy: 代理
        :return: 修改后的分数
        '''
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理：', proxy, '当前分数：', score, '减1')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理：',proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)
