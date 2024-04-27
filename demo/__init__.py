# random模块
# 生成随机浮点数，帧数，字符串，甚至帮助你随机选择列表中的一个元素，打乱一组数据等；
from random import *
print(random()) #生成0-1之间的浮点数，但是能取到0，不能取到1
print(randint(1,100)) #生成指定范围内整数，包括开始值和结束值
print(randrange(1,100,2)) # 生成指定范围内的奇数
print(randrange(0,100,2)) #生成指定范围内的偶数
f=[1,2,3,6,7,2]
print(sample(f,3)) #生成从一个固定集合中选n个数随机
print(choice(f)) #随机生成一个字符
shuffle(f)
print(list(f))