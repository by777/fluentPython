# -*- coding: utf-8 -*-
# @TIME : 2021/3/10 16:38
# @AUTHOR : Xu Bai
# @FILE : 3-8.dict的优势与劣势
# @DESCRIPTION :
# 字典在内存的开销巨大
# 键的查询很快（）基于散列
# 键的次序取决于添加顺序
# 往字典里添加新键可能会改变已有键的顺序 ---- 由于字典可能会扩容

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Saf Odc'),
    (55, 'Dwd jo'),
    (92, 'Ok ko'),
    (880, 'Poc Cad')
]
d1 = dict(DIAL_CODES)
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('d2:',d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3 # 是相等的，因为所包含的数据是相同的