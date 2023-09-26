import unittest
from src import ExprJudge


class TestJudge(unittest.TestCase):
    # 初始化
    def test_judge_init(self):
        ej = ExprJudge()
        self.assertEqual(ej.expr_trees, [])

    # 除数为0
    def test_judge_negative(self):
        ej = ExprJudge()
        ej.judge_negative('1+2+3/0-4/0+5/0')

    # 重复添加
    def test_judge_repeat(self):
        ej = ExprJudge()
        ej.judge_repeat('1+2+3')
        ej.judge_repeat('1+2+3')
