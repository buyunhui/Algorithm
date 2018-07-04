class CountIter:
    """
    iter
    """
    def __init__(self, n):
        self.n = n
 
    def __iter__(self):
        self.x = -1
        return self
 
    def __next__(self):  # For Python 3.x
        self.x += 1
        if self.x < self.n:
            return self.x
        else:
            raise StopIteration
 
for i in CountIter(5):
    print(i)



def count(n):
    """
    generator
    """
    x = 0
    while x < n:
        yield x
        x += 1
 
for i in count(5):
    print(i)


# CountIter类就是一个迭代器，它的__iter__()方法返回可迭代对象，next()方法则执行下一轮迭代。
#上面的代码执行后也会打印序列0到4，看上去跟生成器效果一样，
#就是代码长一点。不仅如此，生成器自带next()方法，而且在越界时也会抛出StopIteration异常。
#那区别到底是什么，在何种情况下，我们应该使用生成器呢？
#
#每次执行迭代器的next()方法并返回后，该方法的上下文环境即消失了，也就是所有在next()方法中定义的局部变量就无法被访问了。
#而对于生成器，每次执行next()方法后，代码会执行到yield关键字处，并将yield后的参数值返回，同时当前生成器函数的上下文会被保留下来。
#也就是函数内所有变量的状态会被保留，同时函数代码执行到的位置会被保留，感觉就像函数被暂停了一样。
#当再一次调用next()方法时，代码会从yield关键字的下一行开始执行。很神奇吧！
#如果执行next()时没有遇到yield关键字即退出（或返回），则抛出StopIteration异常。
#
#python 中的生成器表达式：（expr for iter_var in iterable if cond_expr）



def count(n):
    x = 0
    while x < n:
        value = yield x
        if value is not None:
            print('Received value: %s' %value)
        x += 1

gen = count(5)
print(next(gen))  # print 0

#send()就是next()的功能，加上传值给yield。如果你有兴趣看下Python的源码，你会发现，其实next()的实现，就是send(None)。
print(gen.send('Hello'))  # Received value: Hello, then print 1

def consumer():
    last = ''
    while True:
        receival = yield last
        if receival is not None:
            print('Consume %s' % receival)
            last = receival
 
def producer(gen, n):
    next( gen)
    x = 0
    while x < n:
        x += 1
        print('Produce %s' % x)
        last = gen.send(x)
 
    gen.close()
 
gen = consumer()
producer(gen, 5)
"""
Produce 1
Consume 1
Produce 2
Consume 2
Produce 3
Consume 3
Produce 4
Consume 4
Produce 5
Consume 5
"""
