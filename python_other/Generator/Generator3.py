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