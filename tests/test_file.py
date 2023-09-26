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
            print(f"成功设置文件 '{exercise_path}' 为只读。")
        except OSError:
            print(f"无法设置文件 '{exercise_path}' 为只读。")

        main()

        try:
            os.chmod(exercise_path, 0o644)  # 取消只读属性，设置为可读写权限，即 0o644（八进制表示）
            print(f"成功取消文件 '{exercise_path}' 为只读。")
        except OSError:
            print(f"无法取消文件 '{exercise_path}' 的只读属性。")

        output = mock_stdout.getvalue().strip()
        self.assertIn(f"成功设置文件 '{exercise_path}' 为只读。", output)
        self.assertIn("ERROR: 写入文件错误。请检查写入权限和文件占用", output)
        self.assertIn(f"成功取消文件 '{exercise_path}' 为只读。", output)

    # 没有答案文件写权限
    @patch('sys.argv', ['src/main.py', '-n', '10', '-r', '10'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_answer_file(self, mock_stdout):
        answer_path = 'Answers.txt'
        try:
            os.chmod(answer_path, 0o444)  # 设置只读权限，即 0o444（八进制表示）
            print(f"成功设置文件 '{answer_path}' 为只读。")
        except OSError:
            print(f"无法设置文件 '{answer_path}' 为只读。")

        main()

        try:
            os.chmod(answer_path, 0o644)  # 取消只读属性，设置为可读写权限，即 0o644（八进制表示）
            print(f"成功取消文件 '{answer_path}' 为只读。")
        except OSError:
            print(f"无法取消文件 '{answer_path}' 的只读属性。")

        output = mock_stdout.getvalue().strip()
        self.assertIn(f"成功设置文件 '{answer_path}' 为只读。", output)
        self.assertIn("ERROR: 写入文件错误。请检查写入权限和文件占用", output)
        self.assertIn(f"成功取消文件 '{answer_path}' 为只读。", output)

    # 没有成绩文件写权限
    @patch('sys.argv', ['src/main.py', '-e', 'Exercises.txt', '-a', 'Answers.txt'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_grade_file(self, mock_stdout):
        grade_path = 'Grade.txt'
        try:
            os.chmod(grade_path, 0o444)  # 设置只读权限，即 0o444（八进制表示）
            print(f"成功设置文件 '{grade_path}' 为只读。")
        except OSError:
            print(f"无法设置文件 '{grade_path}' 为只读。")

        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("ERROR: 写入文件错误。请检查写入权限和文件占用", output)

        try:
            os.chmod(grade_path, 0o644)  # 取消只读属性，设置为可读写权限，即 0o644（八进制表示）
            print(f"成功取消文件 '{grade_path}' 为只读。")
        except OSError:
            print(f"无法取消文件 '{grade_path}' 的只读属性。")

        output = mock_stdout.getvalue().strip()
        self.assertIn(f"成功设置文件 '{grade_path}' 为只读。", output)
        self.assertIn("ERROR: 写入文件错误。请检查写入权限和文件占用", output)
        self.assertIn(f"成功取消文件 '{grade_path}' 为只读。", output)

    # 空文件路径
    @patch('sys.argv', ['src/main.py', '-e', '', '-a', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_file(self, mock_stdout):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("ERROR: 参数输入错误。请检查输入参数，仅能出现-n -r 或 -e -a 的输入参数组合", output)

    # 错误答案文件路径
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_err_answerFile(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.argv', ['src/main.py', '-e', 'Exercises.txt', '-a', 'exercise.txt']):
                main()
                output = mock_stdout.getvalue().strip()
                self.assertIn("ERROR: 读取文件错误。请检查输入参数路径是否存在", output)

        self.assertEqual(cm.exception.code, 1)

    # 错误题目文件路径
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_err_exeFile(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.argv', ['src/main.py', '-e', 'exercise.txt', '-a', 'Answers.txt']):
                main()
                output = mock_stdout.getvalue().strip()
                self.assertIn("ERROR: 读取文件错误。请检查输入参数路径是否存在", output)

        self.assertEqual(cm.exception.code, 1)
