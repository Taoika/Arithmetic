from generate import ExprGenerate
from judge import ExprJudge

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

# 打印生成的四则运算表达式
for i, (expr, result) in enumerate(zip(eg.expressions, eg.results)):
    print(f'{i + 1}: {expr} = {result}')
