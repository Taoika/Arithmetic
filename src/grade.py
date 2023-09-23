from sympy import sympify
import numpy as np


class Grade:
    """
    打分器，用于对提交的题目和答案进行批改。
    """

    def __init__(self, expressions):
        self.refer_results = list(map(lambda e: str(sympify(e)), expressions))  # 计算参考答案
        self.right_list = []  # 正确题目编号列表
        self.wrong_list = []  # 错误题目编号列表
        self.right_count = 0  # 正确题目数量
        self.wrong_count = 0  # 错误题目数量

    def get_grade(self, results):
        """
        比较参考答案和答案文件得到正确与错误的题目信息。
        :param results: 提供的答案列表
        :return: None
        """
        bools = np.array(self.refer_results) == np.array(results)
        self.right_list = np.where(bools)[0] + 1  # 获取正确题目标号
        self.wrong_list = np.where(~bools)[0] + 1  # 获取错误题目标号
        self.right_count = len(self.right_list)  # 获取正确题目数量
        self.wrong_count = len(self.wrong_list)  # 获取错误题目数量

    def save_grade(self):
        """
        保存批改结果到文件Grade.txt。
        :return: None
        """
        with open('Grade.txt', 'w') as f:
            f.write(f"Correct: {self.right_count} ({', '.join(list(map(str, self.right_list)))})\n")
            f.write(f"Wrong: {self.wrong_count} ({', '.join(list(map(str, self.wrong_list)))})\n")

