import time
from multiprocessing import Process

from settings import TESTER_CYCLE
from api import app
from getter import Getter
from tester import Tester


class Scheluler(object):

    def schedule_tester(self, cycle=TESTER_CYCLE):
        '''
        定时测试代理
        :param cycle:
        :return:
        '''
        tester = Tester()
        while True:
            print('测试器开始运行！')
            tester.run()
            time.sleep(cycle)
