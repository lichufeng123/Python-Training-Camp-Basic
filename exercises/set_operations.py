"""
练习: 集合操作

描述：
实现两个学生集合的并集、交集和差集操作。

请补全下面的函数，对两个学生集合进行各种操作。
"""

def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作
    
    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ("union", "intersection", "difference")
    
    返回:
    - 集合操作的结果
    """
    # 请在下方编写代码
    if operation == "union":
        return set1.union(set2)  # 或 set1 | set2[2,4](@ref)
    elif operation == "intersection":
        return set1.intersection(set2)  # 或 set1 & set2[2,6](@ref)
    elif operation == "difference":
        return set1.difference(set2)  # 或 set1 - set2[2,8](@ref)
    else:
        return set()  # 默认返回空集（根据需求可扩展其他操作）

# 定义两个测试集合
students_A = {"Alice", "Bob", "Charlie"}
students_B = {"Bob", "David", "Eve"}

# 并集运算（合并所有学生）
print(student_set_operations(students_A, students_B, "union"))
# 输出：{'Alice', 'Bob', 'Charlie', 'David', 'Eve'}

# 交集运算（共同存在的学生）
print(student_set_operations(students_A, students_B, "intersection"))
# 输出：{'Bob'}

# 差集运算（仅在A中存在且B没有的学生）
print(student_set_operations(students_A, students_B, "difference"))
# 输出：{'Alice', 'Charlie'}