from flask import Flask, g

from db_redis import RedisClient


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

@app.route('/')
def index():
    '''
    主页
    :return:
    '''
    return '<h2>欢迎进入代理池系统</h2>'

@app.route('/count')
def get_counts():
    '''
    获取代理池总数
    :return: 代理池总数
    '''
    conn = get_conn()
    return str(conn.count())

if __name__ == '__main__':
    app.run()
