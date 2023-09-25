import unittest
import subprocess


class TestMain(unittest.TestCase):
    def test_lackArgs(self):  # 缺少参数
        result = subprocess.run(['python', 'D:/code/gitcode/软件工程/结对编程/Arithmetic/src/main.py'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        expected_output = "ERROR: 参数输入错误。请检查输入参数，仅能出现-n -r 或 -e -a 的输入参数组合。\n"
        self.assertIn(expected_output, result.stdout)

    def test_generate_Args(self):   # 生成四则运算的命令参数
        result = subprocess.run(
            ['python', 'D:/code/gitcode/软件工程/结对编程/Arithmetic/src/main.py', '-n', '10', '-r', '10'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        expected_output1 = "正在生成四则运算式及其结果"
        expected_output2 = "正在保存生成的四则运算式及其结果到文件"
        expected_output3 = "成功保存生成的四则运算式到当前路径下的文件Exercises.txt"
        expected_output4 = "成功保存生成的参考答案到当前路径下的文件Answers.txt"
        self.assertIn(expected_output1, result.stdout)
        self.assertIn(expected_output2, result.stdout)
        self.assertIn(expected_output3, result.stdout)
        self.assertIn(expected_output4, result.stdout)
