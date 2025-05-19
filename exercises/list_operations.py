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
        # 添加操作：args[0]为要添加的学生对象
        new_list.append(args[0])

    elif operation == "remove":
        # 删除操作：args[0]为要删除学生的id
        target_id = args[0]
        for i in range(len(new_list)):
            if new_list[i].get('id') == target_id:
                del new_list[i]
                break  # 只删除第一个匹配项

    elif operation == "update":
        # 更新操作：args[0]为学生id，args[1]为更新字段的字典
        target_id, update_data = args[0], args[1]
        for student in new_list:
            if student.get('id') == target_id:
                student.update(update_data)
                break

    return new_list

students = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]

# 添加学生
students = student_list_operations(students, 'add', {'id': 3, 'name': 'Charlie'})

# 删除id=2的学生
students = student_list_operations(students, 'remove', 2)

# 更新id=1的学生姓名
students = student_list_operations(students, 'update', 1, {'name': 'Alicia'})
print(students)