import ctypes  
   
lib = ctypes.cdll.LoadLibrary("D:\\Algorithm\\python_other\\tipsTest\\Project5.dll")    
lib.foo(1, 3)  
print('***finish***')  
def t(a):
    """[summary]
    
    Arguments:
        a {[type]} -- [description]
    """

