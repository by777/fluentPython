# -*- coding: utf-8 -*-
# @TIME : 2021/3/11 11:24
# @AUTHOR : Xu Bai
# @FILE : 5-10.tag函数生成HTML标签
# @DESCRIPTION :
def tag(name, *content, cls=None, **attrs):
    '''
    生成一个或多个HTML标签
    :param name:
    :param content:
    :param cls:
    :param attrs:
    :return:
    '''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s" ' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='testing', name='img'))
    my_tag = {
        'name': 'img',
        'tittle': 'Sunset',
        'src': 'https://www.baidu.com',
        'cls': 'framed'
    }

    print(tag(**my_tag))  # 加上**，字典中所有元素作为单个参数传入，同名键会绑定到对应的具名参数上


    def f(a, *, b):
        return a, b


    print(f(1, b=2))
