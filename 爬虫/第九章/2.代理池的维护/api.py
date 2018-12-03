from flask import Flask, g

from .db_redis import RedisClient


__all__ = ['app']

app = Flask(__name__)

def get_conn():
    '''
    连接
    :return:
    '''
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis