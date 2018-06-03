code_global = compile('''
sum = 0
for x in range(500000):
    sum += x
''', '<string>', 'exec')
code_local = compile('''
def f():
    sum = 0
    for x in range(500000):
        sum += x
''', '<string>', 'exec')

def test_global():
    exec(code_global)

def test_local():
    locals()
    exec(code_local,locals())

class Foo(object):
    def __del__(self):
        print('Deleted')
foo = Foo()
