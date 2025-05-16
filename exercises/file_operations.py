"""
练习: 文件处理

描述：
本练习帮助您学习如何在Python中进行文件的读取和写入操作。

请补全下面的函数，实现文件的读取和写入功能。
"""
from pathlib import Path


def read_file(file_path):
    """
    读取文本文件内容
    
    参数:
    - file_path: 文件路径
    
    返回:
    - 文件内容字符串
    """
    # 请在下方编写代码
    # 使用open()函数打开文件并读取内容

    try:
        with open(file_path, "r", encoding="UTF-8") as f:
            return f.read()
    except FileNotFoundError:
        print("文件不存在！")
    except UnicodeDecodeError:
        print("检查文件编码格式！")

def write_file(file_path, content):
    """
    写入内容到文本文件
    
    参数:
    - file_path: 文件路径
    - content: 要写入的内容
    
    返回:
    - 是否写入成功的布尔值
    """
    # 请在下方编写代码
    # 使用with语句和open()函数写入内容到文件
    try:
        path = Path(file_path)
        # 自动创建父目录（关键修复点）
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="UTF-8") as f:
            f.write(content)
            return True
    except Exception as e:
        print(f"错误详情：{str(e)}")  # 增加错误日志
        return False


print(write_file("test/data_types.py","hello world"))
print(read_file("test/data_types.py"))