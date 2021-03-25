# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 16:39
# @AUTHOR : Xu Bai
# @FILE : 5-19.有注解的clip函数
# @DESCRIPTION :
print('python3 提供了一种句法，用于为函数声明中的参数和返回值附加元数据')


def clip(text: str, max_len: 'int > 0' = 80) -> str:  # 区别在第一行，有注解的函数声明
    end = None
    if len(text) > max_len:
        # 返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end == None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


if __name__ == '__main__':
    # 注解不做任何处理，但存储在下面，解释器不做检查、不做强制、不做验证
    print(clip.__annotations__)
