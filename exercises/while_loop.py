"""
练习: while循环

描述：
在数字列表中查找第一个偶数。

请补全下面的函数，使用while循环在数字列表中查找并返回第一个偶数。
如果列表中没有偶数，则返回None。
"""

def find_first_even(numbers):
    """
    在数字列表中查找第一个偶数
    
    参数:
    - numbers: 整数列表
    
    返回:
    - 列表中的第一个偶数，如果没有偶数则返回None
    """
    # 请在下方编写代码
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            return numbers[index]
        index += 1
    return None
print(find_first_even([1,3,5,7,8,9]))  # 输出:8
print(find_first_even([9,11,13]))      # 输出:None
print(find_first_even([]))             # 输出:None