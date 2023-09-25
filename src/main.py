import argparse
from generate import ExprGenerate
from judge import ExprJudge
from expression_format import ExprFormat
from expression_reverse_format import ExprReverFormat
from grade import Grade
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
    print("正在生成四则运算式及其结果。。。。。")
    while eg.count < args.n:
        expr_str = eg.generate()
        # 检查表达式是否符合要求，如果是，就将其添加到列表中，并增加计数器
        if ej.judge(expr_str):
            eg.add_expression(expr_str)

    # 字符串表达式列表处理
    ef = ExprFormat()  # 实例化格式化器
    expressions = ef.expr_format(eg.expressions)  # 格式化运算式
    results = ef.result_format(eg.results)  # 格式化结果

    # 保存生成内容文件
    print("正在保存生成的四则运算式及其结果到文件。。。。。")
    try:
        save_generate(expressions, results)
        print("成功保存生成的四则运算式到当前路径下的文件Exercises.txt。")
        print("成功保存生成的参考答案到当前路径下的文件Answers.txt。")
    except PermissionError:
        print("ERROR: 写入文件错误。请检查写入权限和文件占用。")

elif not all([args.n, args.r]) and all([args.e, args.a]):  # 批改评分
    # 读文件
    print("正在读取提供的四则运算式文件及其结果文件。。。。。")
    try:
        expressions, results = read_files(args.e, args.a)
    except FileNotFoundError:
        print("ERROR: 读取文件错误。请检查输入参数路径是否存在。")
        exit(1)

    # 逆格式化
    erf = ExprReverFormat()
    expressions = erf.expr_reverse_format(expressions)
    results = erf.result_reverse_format(results)

    # 实例化打分器
    g = Grade(expressions)

    # 批改打分
    print("正在批改评分。。。。。")
    g.get_grade(results)

    # 保存打分文件
    print("正在保存批改结果到文件。。。。。")
    try:
        g.save_grade()
        print("成功保存批改结果至当前目录下的Grade.txt文件。")
    except PermissionError:
        print("ERROR: 写入文件错误。请检查写入权限和文件占用。")

else:  # 参数错误
    print("ERROR: 参数输入错误。请检查输入参数，仅能出现-n -r 或 -e -a 的输入参数组合。")
