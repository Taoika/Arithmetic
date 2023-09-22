def save_files(expressions, results):
    """
    保存生成的四则运算式及其对应结果
    :param expressions: 格式化的四则运算式列表
    :param results: 格式化的结果列表
    :return: None
    """
    with open('Exercises.txt', 'w') as f:
        f.writelines(expressions)
    with open('Answers.txt', 'w') as f:
        f.writelines(results)
