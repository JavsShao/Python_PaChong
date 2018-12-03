# Redis数据库地址
REDIS_HOST = '127.0.0.1'
# Redis端口
REDIS_PORT = 6379
# Redis密码
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

# 代理分数
# 最大分数
MAX_SCORE = 100
# 最小分数
MIN_SCORE = 0
# 默认的分数
INITIAL_SCORE = 10

# 测试网址
TEST_URL = 'https://www.baidu.com'
VALID_STATUS_CODES = [200, 302]
# 最大批测试量
BATCH_TEST_SIZE = 10