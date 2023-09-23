import re


class ExprReverFormat:
    """
    逆格式化表达式字符串，与ExprFormat类功能互逆。
    """
    def __init__(self):
        pass

    @staticmethod
    def mixed_to_fraction(match):
        """
        字符串带分数转换为假分数。
        :param match: 正则匹配得到的对象，包含带分数信息
        :return: 假分数字符串（两侧包含括号）
        """
        quotient = int(match.group(1))  # 获取整数部分
        numerator = int(match.group(2))  # 获取分子
        denominator = int(match.group(3))  # 获取分母
        numerator_new = quotient * denominator + numerator  # 计算新分子
        return f"{numerator_new}/{denominator}"  # 返回假分数形式(添加括号防止除以分数识别出错)

    def match_common(self, s):
        """
        通用的正则匹配处理，即表达式和结果的逆格式化都需要执行。
        :param s: 待处理的字符串
        :return: 处理后的字符串
        """
        # 去除开头标号
        s = re.sub(r"\d+\.\s", "", s)
        # 去除结尾换行
        s = re.sub(r"\n", "", s)
        # 替换带分数为假分数
        s = re.sub(r"(\d+)'(\d+)/(\d+)", self.mixed_to_fraction, s)
        # 返回处理结果
        return s

    def match_result(self, result_str):
        """
        对结果字符串的正则处理。
        :param result_str: 待处理的结果字符串
        :return: 处理后的结果字符串
        """
        return self.match_common(result_str)

    def match_expression(self, expr_str):
        """
        对四则运算表达式字符串的正则处理。
        :param expr_str: 待处理的四则运算表达式字符串
        :return: 处理后的四则运算表达式字符串
        """
        expr_str = self.match_common(expr_str)
        # 分数两侧添加括号
        expr_str = re.sub(r"(\d+)/(\d+)", lambda m: f"({m.groups()[0]}/{m.groups()[1]})", expr_str)
        # 替换全部乘号
        expr_str = re.sub(r"x", "*", expr_str)
        # 替换全部除号
        expr_str = re.sub(r"÷", "/", expr_str)
        # 返回处理结果
        return expr_str

    def expr_reverse_format(self, expressions):
        """
        对四则运算表达式列表的逆格式化，将人类可读的格式转换为机器能够直接计算的格式。
        :param expressions: 可读的四则运算表达式列表
        :return: 可计算的四则运算表达式列表
        """
        return list(map(self.match_expression, expressions))

    def result_reverse_format(self, results):
        """
        对结果列表的逆格式化，方便后续进行结果比对批改。
        :param results: 格式化的结果（不含假分数，包含序号）
        :return: 逆格式化的结果（包含假分数，不含序号）
        """
        return list(map(self.match_result, results))

