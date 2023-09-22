from generate import ExprGenerate
from judge import ExprJudge
from expression_format import ExprFormat

# 实例化四则运算式生成器
eg = ExprGenerate()

# 实例化四则运算式判别器
ej = ExprJudge()

# 循环生成表达式，直到达到10条或超时为止
while eg.count < 10:
    expr_str = eg.generate()

    # 检查表达式是否符合要求，如果是，就将其添加到列表中，并增加计数器
    if ej.judge(expr_str):
        eg.add_expression(expr_str)

print(len(eg.expressions))
print(len(eg.results))
print(len(ej.expr_trees))

# 字符串表达式列表处理
ef = ExprFormat()  # 实例化格式化器
expressions = ef.expr_format(eg.expressions)  # 格式化运算式
results = ef.result_format(eg.results)  # 格式化结果


# 打印生成的四则运算表达式
for expr, result in zip(expressions, results):
    print(f'{expr}')
    print(f'{result}')
