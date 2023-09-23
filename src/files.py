def save_generate(expressions, results):
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


def read_files(exercises_path, answers_path):
    """
    读取四则运算式及其对应结果
    :param exercises_path: 四则运算式文件路径
    :param answers_path: 结果文件路径
    :return: 格式化的四则运算式列表, 格式化的结果列表
    """
    with open(exercises_path, 'r') as f1, open(answers_path, 'r') as f2:
        return f1.readlines(), f2.readlines()
