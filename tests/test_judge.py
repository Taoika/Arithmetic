import unittest
from src import ExprJudge


class TestJudge(unittest.TestCase):
    # 初始化
    def test_init(self):
        ej = ExprJudge()
        self.assertEqual(ej.expr_trees, [])
    # 判定中间过程不为负数
    # 判定该四则运算表达式不重复
    # 总判定
