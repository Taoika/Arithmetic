from sympy import sympify, S


class ExprJudge:
    """
    四则运算式判别器，判别以下几种情况的算式，返回false：
    - 判别非法运算式（例如除数为0等）
    - 判别重复
    - 判别运算过程出现负数
    """

    def __init__(self):
        expr_tree = []

    @staticmethod
    def judge_illegal(expr_str):
        return sympify(expr_str) != S.ComplexInfinity

    # def judge_repeat(self):
    #
    #
    # def judge_negative(self):

    def judge(self, expr_str):
        return self.judge_illegal(expr_str)
