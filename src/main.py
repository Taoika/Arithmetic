import argparse
from generate import ExprGenerate
from judge import ExprJudge
from expression_format import ExprFormat
from expression_reverse_format import ExprReverFormat
from files import *

# 命令行参数
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, choices=range(1, 10001), default=None,
                    help="The number of generated four arithmetic expressions.")
parser.add_argument("-r", type=int, choices=range(1, 101), default=None,
                    help="The range of operands.")
parser.add_argument("-e", default=None, help="The path of expressions file.")
parser.add_argument("-a", default=None, help="The path of answers file.")
args = parser.parse_args()

if all([args.n, args.r]) and not all([args.e, args.a]):  # 生成四则运算式
    # 实例化四则运算式生成器
    eg = ExprGenerate(args.r)

    # 实例化四则运算式判别器
    ej = ExprJudge()

    # 循环生成表达式，直到达到指定数量
    while eg.count < args.n:
        expr_str = eg.generate()

        # 检查表达式是否符合要求，如果是，就将其添加到列表中，并增加计数器
        if ej.judge(expr_str):
            eg.add_expression(expr_str)

    # print(len(eg.expressions))
    # print(len(eg.results))
    # print(len(ej.expr_trees))

    # 字符串表达式列表处理
    ef = ExprFormat()  # 实例化格式化器
    expressions = ef.expr_format(eg.expressions)  # 格式化运算式
    results = ef.result_format(eg.results)  # 格式化结果

    # 打印生成的四则运算表达式
    # for expr, result in zip(expressions, results):
    #     print(f'{expr}')
    #     print(f'{result}')

    # 保存文件
    save_files(expressions, results)

elif not all([args.n, args.r]) and all([args.e, args.a]):  # 批改评分
    # 读文件
    expressions, results = read_files(args.e, args.a)
    # 逆格式化
    erf = ExprReverFormat()
    expressions = erf.expr_reverse_format(expressions)
    results = erf.result_reverse_format(results)
    print(expressions)
    print(results)
else:  # 参数错误
    print("ERROR: 参数输入错误。请检查输入参数，仅能出现-n -r 或 -e -a 的输入参数组合。")
