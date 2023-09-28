import sys

sys.path.append('src')  # 添加路径 不然执行main函数的时候找不到其他模块

import unittest
from unittest.mock import patch
import io
from src.main import main


class TestArgs(unittest.TestCase):
    # 缺少参数
    @patch('sys.argv', ['src/main.py'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lackArgs(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("ERROR: 参数输入错误。请检查输入参数，仅能出现-n -r 或 -e -a 的输入参数组合", output)

    # 多余参数1
    @patch('sys.argv', ['src/main.py', '-n', '10', '-r', '10', '-e', 'Exercises.txt'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lastArgs1(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("成功保存生成的参考答案到当前路径下的文件", output)

    # 多余参数2
    @patch('sys.argv', ['src/main.py', '-n', '10', '-e', 'Exercises.txt', '-a', 'Answers.txt'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lastArgs2(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("成功保存批改结果至当前目录下的", output)

    # 生成四则运算的命令参数
    @patch('sys.argv', ['src/main.py', '-n', '10', '-r', '100'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gen_Args(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("正在保存生成的四则运算式及其结果到文件", output)
        self.assertIn("成功保存生成的四则运算式到当前路径下的文件Exercises.txt", output)
        self.assertIn("成功保存生成的参考答案到当前路径下的文件Answers.txt", output)

    # 部分错误答案
    @patch('sys.argv', ['src/main.py', '-e', 'Exercises.txt', '-a', 'Answers_err.txt'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_err_answers(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("正在读取提供的四则运算式文件及其结果文件", output)
        self.assertIn("正在批改评分", output)
        self.assertIn("正在保存批改结果到文件", output)
        self.assertIn("成功保存批改结果至当前目录下的Grade.txt文件", output)

    # 判对错的命令参数
    @patch('sys.argv', ['src/main.py', '-e', 'Exercises.txt', '-a', 'Answers.txt'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_grade_Args(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("正在读取提供的四则运算式文件及其结果文件", output)
        self.assertIn("正在批改评分", output)
        self.assertIn("正在保存批改结果到文件", output)
        self.assertIn("成功保存批改结果至当前目录下的Grade.txt文件", output)

    # 100
    @patch('sys.argv', ['src/main.py', '-n', '100', '-r', '100'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gen_100(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("正在保存生成的四则运算式及其结果到文件", output)
        self.assertIn("成功保存生成的四则运算式到当前路径下的文件Exercises.txt", output)
        self.assertIn("成功保存生成的参考答案到当前路径下的文件Answers.txt", output)

    # 1000
    @patch('sys.argv', ['src/main.py', '-n', '1000', '-r', '100'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gen_1000(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("正在保存生成的四则运算式及其结果到文件", output)
        self.assertIn("成功保存生成的四则运算式到当前路径下的文件Exercises.txt", output)
        self.assertIn("成功保存生成的参考答案到当前路径下的文件Answers.txt", output)

    # 范围外参数n
    def test_outRange_n(self):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.argv', ['src/main.py', '-n', '0', '-r', '0']):
                main()

        self.assertEqual(cm.exception.code, 1)

    # 范围外参数r
    def test_outRange_r(self):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.argv', ['src/main.py', '-n', '10', '-r', '0']):
                main()

        self.assertEqual(cm.exception.code, 1)
