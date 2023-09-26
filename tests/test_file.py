import sys

sys.path.append('src')  # 添加路径 不然执行main函数的时候找不到其他模块
import unittest
from unittest.mock import patch
import os
import io
from src.main import main


class TestFile(unittest.TestCase):
    # 没有题目文件写权限
    @patch('sys.argv', ['src/main.py', '-n', '10', '-r', '10'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_exercise_file(self, mock_stdout):
        exercise_path = 'Exercises.txt'
        try:
            os.chmod(exercise_path, 0o444)  # 设置只读权限，即 0o444（八进制表示）
        except OSError:
            print(f"无法设置文件 '{exercise_path}' 为只读。")

        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("ERROR: 写入文件错误。请检查写入权限和文件占用", output)

        try:
            os.chmod(exercise_path, 0o644)  # 取消只读属性，设置为可读写权限，即 0o644（八进制表示）
        except OSError:
            print(f"无法取消文件 '{exercise_path}' 的只读属性。")

    # 没有答案文件写权限
    @patch('sys.argv', ['src/main.py', '-n', '10', '-r', '10'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_answer_file(self, mock_stdout):
        answer_path = 'Answers.txt'
        exercise_path = 'Exercises.txt'
        try:
            os.chmod(answer_path, 0o444)  # 设置只读权限，即 0o444（八进制表示）
        except OSError:
            print(f"无法设置文件 '{answer_path}' 为只读。")

        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("ERROR: 写入文件错误。请检查写入权限和文件占用", output)
        try:
            os.chmod(answer_path, 0o644)  # 取消只读属性，设置为可读写权限，即 0o644（八进制表示）
        except OSError:
            print(f"无法取消文件 '{answer_path}' 的只读属性。")
