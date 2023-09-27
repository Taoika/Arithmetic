![Arithmetic](https://github.com/Taoika/Arithmetic/assets/108986990/4c755f1b-cacb-4a4f-ad98-1e5f683313ca)# Arithmetic

四则运算题目生成器

## 主要结构
![Arithmetic](https://github.com/Taoika/Arithmetic/assets/108986990/82398cf4-6931-46be-a60f-f6546108f4d3)

## 依赖说明

1. 使用以下命令读取并下载依赖：

```
$ pip install -r requirements.txt
```

## 运行说明

1. 程序采用命令行的方式运行，**src/main.py是程序的入口**；
2. **题目生成**参数说明：
   + 使用 -n 参数控制生成题目的个数
   + 使用 -r 参数控制题目中数值（自然数、真分数和真分数分母）的范围
   + 用例： python src/main.py -n 100 -r 100   
3. **题目批改**参数说明：
   + 使用 -e 给出题目所在的文件
   + 使用 -a 给出需要批改的答案所在的文件
   + 用例：python src/main.py -e Exercises.txt -a Answers.txt
4. 题目生成时会产生一个Exerecises.txt及一个Answers.txt在当前运行目录下
5. 题目批改时会产生一个Grade.txt在当前运行目录下

## 测试说明

1. 工具：
   + 自动化测试：[unittest](https://docs.python.org/3/library/unittest.html)
   + 覆盖率分析：[coverage](https://coverage.readthedocs.io/en/7.3.1/)
2. 配置文件：.coveragerc，配置需要进行覆盖率分析的文件夹，现指定为src
3. 使用以下命令启动自动化测试：

```
$ coverage run -m unittest
```

3. 使用以下命令获取详细覆盖率分析结果：

```
$ coverage report -m
```

## 效能分析说明

1. 工具：[viztracer](https://github.com/gaogaotiantian/viztracer)

2. 使用之前请确保已下载viztracer依赖

3. 使用以下方法生成效能分析结果：

   + 假设我们的脚本需要这样运行：

   ```
   $ python src/main.py -n 10000 -r 100  
   ```

   + 那么效能分析需要这样使用命令：

   ```
   $ viztracer src/main.py -n 10000 -r 100  
   ```

4. 使用以下方法读取并可视化分析结果，如果程序没有出错，该结果将会在浏览器打开：

```
$ vizviewer path/to/result.json
```

## 主要文件结构说明

### src

1. 此文件夹是程序的主要代码部分
2. main.py是程序的入口

### tests

1. 此文件夹是程序的测试部分

### requirements.txt

1. 程序的依赖文件

### .coveragerc

2. coverage配置文件

