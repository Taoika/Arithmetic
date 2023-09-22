import random
from random import randrange
from sympy import Integer, Rational, sympify, S


class ExprGenerate:
    """
    四则运算式生成器。
    - 运算符1~3个，从[+、-、*、/]中选取，分别表示表示加减乘除的四则运算符。
    - 操作数数量比运算符的数量多一个，为0到100之间的自然数或真分数。
    """

    def __init__(self):
        self.expressions = []  # 初始化表达式列表
        self.results = []  # 初始化结果列表
        self.count = 0  # 初始化已经生成的表达式的数量

    # 定义一个函数，用于生成一个四则运算符列表
    @staticmethod
    def random_operators(k):
        # 从加减乘除中随机选择k个
        return random.choices(['+', '-', '*', '/'], k=k)

    # 定义一个函数，用于生成一个0到100之间的自然数或分数的操作数列表
    @staticmethod
    def random_numbers(k):
        nums = []
        for _ in range(k):
            # 以一半的概率生成一个自然数，以一半的概率生成一个分数
            if randrange(2) == 0:
                # 生成一个0到100之间的自然数
                nums.append(Integer(randrange(101)))
            else:
                # 生成一个分数
                numerator = Integer(randrange(1, 11))
                denominator = Integer(randrange(1, 11))
                fraction = Rational(numerator, denominator)
                nums.append(fraction.cancel())  # 对分数进行化简
        return nums

    # 生成表达式
    def generate(self):
        # 随机决定运算符个数（1~3个）
        k = random.randint(1, 3)

        # 随机生成两个运算符和三个操作数
        ops = self.random_operators(k)
        nums = self.random_numbers(k + 1)

        # 拼接成一个表达式字符串(开头结尾加空格方便匹配)
        expr_str = ''
        for i in range(k):
            expr_str += f'({nums[i]}) {ops[i]} '  # 操作数两侧加括号，防止除以分数识别错误
        expr_str += f'({nums[-1]})'
        return expr_str

    def add_expression(self, expr_str):
        result = sympify(expr_str)
        if result != S.ComplexInfinity:  # 判别非法运算式（除数为0）
            self.expressions.append(expr_str)
            self.results.append(str(result))
            self.count += 1
