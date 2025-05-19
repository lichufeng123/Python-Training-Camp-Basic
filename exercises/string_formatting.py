"""
练习: 字符串格式化

描述：
使用f-strings格式化学生信息。

请补全下面的函数，使用f-strings将学生的姓名和年龄格式化为一个字符串。
"""

def format_student_info(name, age):
    """
    使用f-strings格式化学生信息
    
    参数:
    - name: 学生姓名
    - age: 学生年龄
    
    返回:
    - 格式化后的学生信息字符串
    """
    # 请在下方编写代码
    try:
        return f"学生信息 | 姓名：{name.upper():^12} | 年龄：{int(age):03d} 岁"
    except ValueError:
        return "错误：年龄必须是整数"

print(format_student_info("张三", 18))
# 输出：学生信息 | 姓名：张三        | 年龄：018 岁

print(format_student_info("李li", "20"))
# 进阶版输出：学生信息 | 姓名：   LI     | 年龄：020 岁

print(format_student_info("王五", "abc"))
# 进阶版输出：错误：年龄必须是整数