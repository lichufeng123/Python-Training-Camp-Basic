"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    new_list = list(students)
    if operation == "add":
        new_list.append(args[0])
    elif operation == "remove":
        target = args[0]
        try:
            new_list.remove(target)  # 直接删除匹配元素
        except ValueError:
            pass  # 元素不存在时不处理
    elif operation == "update":
        index, new_name = args[0], args[1]
        if 0 <= index < len(new_list):
            new_list[index] = new_name
    return new_list

