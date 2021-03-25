# -*- encoding: utf-8 -*-
# @Time : 20/09/27 10:21 
# @Author : Xu Bai
# @File : 2-8.用嵌套元组来获取经度.py 
# @Desc :
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.21341444142, 139.23241)),
    ('Delhi NCR', 'IN', 21.935, (28.21323123, 77.20422442)),
    ('Mexico City', 'MX', 20.142, (19.42112, -99.1333333)),
    ('New York-Newark', 'US', 20.104, (40.821321, -74.020123)),
    ('Sao Paulo', 'BR', 19.632, (-23.2134124, -46.231332))
]
# 居中对齐 (:^) 靠左对齐 (:<)
# 靠右对齐 (:>)
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:  # 西半球
        print(fmt.format(name, latitude, longitude))
