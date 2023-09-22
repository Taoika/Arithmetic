import re


class ExprFormat:
    """
    格式化表达式字符串
    """
    def __init__(self):
        pass

    @staticmethod
    def fraction_to_mixed(match):
        numerator = int(match.group(1))  # 获取分子
        denominator = int(match.group(2))  # 获取分母
        if numerator > denominator:  # 如果是假分数
            quotient = numerator // denominator  # 计算商
            remainder = numerator % denominator  # 计算余数
            return f"{quotient}'{remainder}/{denominator}"  # 返回带分数形式
        else:  # 如果不是假分数
            return match.group()  # 返回原样

    def match_expression(self, expr_str):
        # 替换全部乘号
        expr_str = re.sub(r"\*", "x", expr_str)
        # 替换全部除号
        expr_str = re.sub(r"\s/\s", " ÷ ", expr_str)
        # 去除冗余括号
        expr_str = re.sub(r"\(\d", lambda m: m.group()[1], expr_str)  # 去除数字左括号‘(’
        expr_str = re.sub(r"\d\)", lambda m: m.group()[0], expr_str)  # 去除数字左括号‘)’
        # 替换假分数为带分数
        expr_str = re.sub(r"(\d+)/(\d+)", self.fraction_to_mixed, expr_str)
        # 返回处理结果
        return expr_str

    def match_result(self, result_str):
        # 替换假分数为带分数
        result_str = re.sub(r"(\d+)/(\d+)", self.fraction_to_mixed, result_str)
        # 返回处理结果
        return result_str

    def expr_format(self, expressions):
        expressions = list(map(self.match_expression, expressions))
        return list(map(lambda x: f'{x[0] + 1}. {x[1]}', enumerate(expressions)))

    def result_format(self, results):
        return list(map(self.match_result, results))