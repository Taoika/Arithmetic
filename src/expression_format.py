import re


class ExprFormat:
    """
    格式化表达式字符串，与ExprReverFormat类功能互逆。
    """
    def __init__(self):
        pass

    @staticmethod
    def fraction_to_mixed(match):
        """
        字符串假分数转换为带分数。
        :param match: 正则匹配得到的对象，包含分数信息
        :return: 真分数字符串或带分数字符串
        """
        numerator = int(match.group(1))  # 获取分子
        denominator = int(match.group(2))  # 获取分母
        if numerator > denominator:  # 如果是假分数
            quotient = numerator // denominator  # 计算商
            remainder = numerator % denominator  # 计算余数
            return f"{quotient}'{remainder}/{denominator}"  # 返回带分数形式
        else:  # 如果不是假分数
            return match.group()  # 返回原样

    def match_common(self, s):
        """
        通用的正则匹配处理，即表达式和结果的格式化都需要执行。
        :param s: 待处理的字符串
        :return: 处理后的字符串
        """
        # 替换假分数为带分数
        s = re.sub(r"(\d+)/(\d+)", self.fraction_to_mixed, s)
        # 返回处理结果
        return s

    def match_expression(self, expr_str):
        """
        对四则运算表达式字符串的正则处理。
        :param expr_str: 待处理的四则运算表达式字符串
        :return: 处理后的四则运算表达式字符串
        """
        # 替换全部乘号
        expr_str = re.sub(r"\*", "x", expr_str)
        # 替换全部除号
        expr_str = re.sub(r"\s/\s", " ÷ ", expr_str)
        # 去除分数的冗余括号
        expr_str = re.sub(r"\((\d+/\d+)\)", lambda m: m.groups()[0], expr_str)
        return self.match_common(expr_str)

    def match_result(self, result_str):
        """
        对结果字符串的正则处理。
        :param result_str: 待处理的结果字符串
        :return: 处理后的结果字符串
        """
        return self.match_common(result_str)

    def expr_format(self, expressions):
        """
        对四则运算表达式列表的格式化，将机器能够直接计算的格式转换为人类可读的格式。
        :param expressions: 可计算的四则运算表达式列表
        :return: 可读的四则运算表达式列表
        """
        expressions = list(map(self.match_expression, expressions))
        return list(map(lambda x: f'{x[0] + 1}. {x[1]}\n', enumerate(expressions)))

    def result_format(self, results):
        """
        对结果列表的格式化，方便人类阅读和后续写入文件。
        :param results: 逆格式化的结果（包含假分数，不含序号）
        :return: 格式化的结果（不含假分数，包含序号）
        """
        results = list(map(self.match_result, results))
        return list(map(lambda x: f'{x[0] + 1}. {x[1]}\n', enumerate(results)))
