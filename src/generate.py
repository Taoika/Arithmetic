import random
from random import randrange
from sympy import Integer, Rational, sympify, S


class ExprGenerate:
    """
    四则运算式生成器。
    - 运算符1~3个，从[+、-、*、/]中选取，分别表示表示加减乘除的四则运算符。
    - 操作数数量比运算符的数量多一个，为0到limit之间的自然数或真分数。
    """

    def __init__(self, limit):
        self.limit = limit  # 初始化操作数大小上限
        self.expressions = []  # 初始化表达式列表
        self.results = []  # 初始化结果列表
        self.count = 0  # 初始化已经生成的表达式的数量

    @staticmethod
    def random_operators(k):
        """
        生成一个四则运算符列表
        :param k: 随机生成四则运算符个数
        :return: 四则运算符列表
        """
        return random.choices(['+', '-', '*', '/'], k=k)  # 从加减乘除中随机选择k个

    def random_numbers(self, k):
        """
        生成一个操作数列表，操作数大小由self.limit限制。
        :param k: 随机生成操作数个数
        :return: 操作数列表
        """
        nums = []
        for _ in range(k):
            # 以一半的概率生成一个自然数，以一半的概率生成一个分数
            if randrange(2) == 0:
                # 生成一个0到limit之间的自然数
                nums.append(Integer(randrange(self.limit)))
            else:
                # 生成一个分数
                numerator = Integer(randrange(1, self.limit))
                denominator = Integer(randrange(1, self.limit))
                fraction = Rational(numerator, denominator).cancel()  # 对分数进行化简
                if fraction.is_integer:
                    nums.append(fraction)  # 整数直接添加
                else:
                    nums.append(f"({fraction})")  # 分数转换成字符串并两侧添加括号，防止除以分数识别错误
        return nums

    # 生成表达式
    def generate(self):
        """
        组合生成四则运算表达式。
        :return: 四则运算表达式字符串
        """
        # 随机决定运算符个数（1~3个）
        k = random.randint(1, 3)

        # 随机生成两个运算符和三个操作数
        ops = self.random_operators(k)
        nums = self.random_numbers(k + 1)

        # 拼接成一个表达式字符串
        expr_str = ''
        for i in range(k):
            expr_str += f'{nums[i]} {ops[i]} '
        expr_str += f'{nums[-1]}'
        return expr_str

    def add_expression(self, expr_str):
        """
        添加记录生成的表达式及其结果。
        :param expr_str: 四则运算表达式字符串
        :return: None
        """
        result = sympify(expr_str)
        if result != S.ComplexInfinity:  # 判别非法运算式（除数为0）
            self.expressions.append(expr_str)
            self.results.append(str(result))
            self.count += 1
