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


# CountIter�����һ��������������__iter__()�������ؿɵ�������next()������ִ����һ�ֵ�����
#����Ĵ���ִ�к�Ҳ���ӡ����0��4������ȥ��������Ч��һ����
#���Ǵ��볤һ�㡣������ˣ��������Դ�next()������������Խ��ʱҲ���׳�StopIteration�쳣��
#�����𵽵���ʲô���ں�������£�����Ӧ��ʹ���������أ�
#
#ÿ��ִ�е�������next()���������غ󣬸÷����������Ļ�������ʧ�ˣ�Ҳ����������next()�����ж���ľֲ��������޷��������ˡ�
#��������������ÿ��ִ��next()�����󣬴����ִ�е�yield�ؼ��ִ�������yield��Ĳ���ֵ���أ�ͬʱ��ǰ�����������������Ļᱻ����������
#Ҳ���Ǻ��������б�����״̬�ᱻ������ͬʱ��������ִ�е���λ�ûᱻ�������о�����������ͣ��һ����
#����һ�ε���next()����ʱ��������yield�ؼ��ֵ���һ�п�ʼִ�С�������ɣ�
#���ִ��next()ʱû������yield�ؼ��ּ��˳����򷵻أ������׳�StopIteration�쳣��
#
#python �е����������ʽ����expr for iter_var in iterable if cond_expr��



def count(n):
    x = 0
    while x < n:
        value = yield x
        if value is not None:
            print('Received value: %s' %value)
        x += 1

gen = count(5)
print(next(gen))  # print 0

#send()����next()�Ĺ��ܣ����ϴ�ֵ��yield�����������Ȥ����Python��Դ�룬��ᷢ�֣���ʵnext()��ʵ�֣�����send(None)��
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
