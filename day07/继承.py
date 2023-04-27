# 例如，一起来完成：
# （1）Father类有一个性别属性，默认为男，同时，Father跑步速度快；
# （2）如果Son类也想要拥有这些属性和方法，该怎么做呢？
# （3）执行程序，观察程序效果。

class Father():
    gender = 'male'

    def run_fast(self):
        print('run fast')

class Son(Father):
    pass

s =Son()
print(s.gender)
s.run_fast()