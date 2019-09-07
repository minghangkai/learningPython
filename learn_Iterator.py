# 可迭代对象Iterable：可以直接作用于for循环的对象
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable

isinstance([], Iterable)

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
from collections import Iterator

isinstance((x for x in range(10)), Iterator) #true
isinstance([], Iterator) #flase
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]), Iterator)#True
isinstance(iter('abc'), Iterator)#True