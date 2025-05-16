"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    vaild_opration = ("add", "remove", "update", "get")
    if operation not in vaild_opration:
        return f"错误：无效操作类型''{operation}’,支持{vaild_opration}"
    try:
        if operation == "add":

            if len(args) != 2:
                return "错误，必须要有两个参数"
            name,scope = args[0],args[1]

            if name in students_dict:
                return f"错误,'{name}'已存在"
            students_dict[name] = scope
            return students_dict.copy()
        elif operation =="remove":
            if len(args)!=1:
                return "错误，必须要有名字"
            name = args[0]

            if name not in students_dict:
                return f"错误'{name}'不存在"
            del students_dict[name]
            return  students_dict.copy()
        elif operation == "update":
            if len(args)!= 2:
                return "更新操作必须有两个修改参数"
            name, new_scope = args[0], args[1]
            if name not in students_dict:
                return f"错误,'{name}'不存在"
            students_dict[name] = new_scope
            return students_dict.copy()
        elif operation == "get":
            if len(args)!=1:
                return "错误,必须要有一个参数"
            name = args[0]
            return students_dict[name]
    except KeyError as e:
        return f"错误：学生 '{e.args[0]}' 不存在"
    except TypeError:
        return "错误：成绩必须是数字类型"

students = {"流川枫": 86, "苏哲":92}
#添加学生
print(student_dict_operations(students,"add","夏雨泽",88))
#删除学生
print(student_dict_operations(students,"remove","夏雨泽"))
#更新学生
print(student_dict_operations(students,"update","苏哲",90))
#查询学生
print(student_dict_operations(students,"get","苏哲"))