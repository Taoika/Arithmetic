from sympy import sympify, S
from sympy import preorder_traversal, Add
from sympy import parse_expr, srepr


class ExprJudge:
    """
    四则运算式判别器，判别以下几种情况的算式，返回false：
    - 判别非法运算式（除数为0）
    - 判别重复
    - 判别运算过程出现负数
    """

    def __init__(self):
        self.expr_trees = []

    @staticmethod
    def judge_illegal(expr_str):
        return sympify(expr_str) != S.ComplexInfinity

    @staticmethod
    def judge_negative(expr_str):
        expr = parse_expr(expr_str, evaluate=False)  # 转换为表达式对象
        for sub_expr in preorder_traversal(expr):  # 遍历子表达式
            if sub_expr.func == Add and sympify((srepr(sub_expr))) < 0:  # 筛选多项式（乘除不可能生成负数）并计算中间结果
                # print(sub_expr, "  ", type(sub_expr))
                return False
        return True

    def judge_repeat(self, expr_str):
        expr_tree = srepr(parse_expr(expr_str, evaluate=False))  # 将表达式字符串转换为二叉树形式字符串
        is_unique = expr_tree not in self.expr_trees  # 判断二叉树形式字符串是否已存在（即重复）
        if is_unique:
            self.expr_trees.append(expr_tree)
        return is_unique

    def judge(self, expr_str):
        return self.judge_illegal(expr_str) and self.judge_negative(expr_str) and self.judge_repeat(expr_str)
