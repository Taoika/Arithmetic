import unittest
from src import ExprGenerate


class TestGenerate(unittest.TestCase):
    # 初始化
    def test_init(self):
        limit = 100
        eg = ExprGenerate(limit)
        self.assertEqual(eg.limit, limit)
        self.assertEqual(eg.expressions, [])
        self.assertEqual(eg.results, [])
        self.assertEqual(eg.count, 0)

    # 生成一个四则运算符列表
    # 生成一个操作数列表
    # 生成四则运算表达式
    # 添加记录生成的表达式及其结果
