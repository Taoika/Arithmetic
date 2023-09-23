import re


class ExprReverFormat:
    """
    逆格式化表达式字符串
    """
    def __init__(self):
        pass

    @staticmethod
    def mixed_to_fraction(match):
        quotient = int(match.group(1))  # 获取整数部分
        numerator = int(match.group(2))  # 获取分子
        denominator = int(match.group(3))  # 获取分母
        numerator_new = quotient * denominator + numerator  # 计算新分子
        return f"{numerator_new}/{denominator}"  # 返回假分数形式(顺便添加括号防止除以分数识别出错)

    def match_common(self, s):
        # 去除开头标号
        s = re.sub(r"\d+\.\s", "", s)
        # 去除结尾换行
        s = re.sub(r"\n", "", s)
        # 替换带分数为假分数
        s = re.sub(r"(\d+)'(\d+)/(\d+)", self.mixed_to_fraction, s)
        # 返回处理结果
        return s

    def match_result(self, result_str):
        return self.match_common(result_str)

    def match_expression(self, expr_str):
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
        return list(map(self.match_expression, expressions))

    def result_reverse_format(self, results):
        return list(map(self.match_result, results))

