'''
 1、重新写的类需要继承unittest.TestCase；
 2、测试用例以test开头
 3、需要写main方法
 4、不要单独运行测试用例，因为可能有关联关系
 5、不用test开头的其他函数就是普通函数
 6、执行默认顺序 0-9,A-Z,a-z是默认顺序，排序规则是依照ASCII码排序规则
'''
import unittest
class UnitDomo(unittest.TestCase):
    def test_a01(self):
        print('01')
    def test_02(self):
        print('02')
    def ground(self):
        print('小帅哥')

# UnitTest的运行
if __name__ == '_main_':
    unittest.main()