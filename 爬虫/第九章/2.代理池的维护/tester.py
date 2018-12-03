import asyncio
import aiohttp
import time
import sys

try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from .db_redis import RedisClient
from .settings import *


class Tester(object):
    def __init__(self):
        '''
        测试初始化
        '''
        self.redis = RedisClient()