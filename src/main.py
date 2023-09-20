from generate import *
from sympy import *

# 实例化四则运算式生成器
eg = ExprGenerate()

# 循环生成表达式，直到达到10条或超时为止
while eg.count < 10:
    try:
        expr_str = eg.generate()
        expr = sympify(expr_str)  # 表达式对象的表达改一下

        # 检查表达式是否符合要求，如果是，就将其添加到列表中，并增加计数器
        # if check_expression(expr):
        #     expressions.append(expr_str)
        #     count += 1

        eg.expressions.append(expr_str)
        eg.count += 1
    except:
        # 如果发生任何异常，就跳过这个表达式，继续下一个循环
        continue

# 打印生成的四则运算表达式
for i, expr in enumerate(eg.expressions):
    print(f'{i + 1}: {expr} = {simplify(expr)}')
