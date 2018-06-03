def count(n):
    x = 0
    while x < n:
        value = yield x
        if value is not None:
            print('Received value: %s' %value)
        x += 1

gen = count(5)
print("test")
print(next(gen))  # print 0
print(gen.send('Hello'))  # Received value: Hello, then print 1
print(next(gen))
"""
test
0
Received value: Hello
1
"""