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
VALID_STATUS_CODES = [200]
# 最大批测试量
BATCH_TEST_SIZE = 10

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 200

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555