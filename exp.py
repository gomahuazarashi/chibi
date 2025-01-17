
class Expr(object):
    pass

class Val(Expr):
    __slots__ = ['value']
    def __init__(self, value = 0):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

v = Val(1)
print(v)
assert v.eval() == 1

assert isinstance(v, Expr) # ==> True
assert isinstance(v, Val) # ==> True
assert not isinstance(v, int) 

def toExper(a):
    if not isinstance(a, Expr):
            a = Val(a)
    return a

class Add(Expr):
    __slots__=['left', 'right']
    def __init__(self, a, b):
        self.left = toExper(a)  
        self.right = toExper(b)
    def eval(self):
        return self.left.eval() + self.right.eval()
    def __repr__(self):
        classname = self .__class__.__name__
        return f'{classname}({self.left},{self.right})'

e = Add(1,Add(1,2))
print(e.eval())
assert e.eval() ==4


e = Add(Val(1),Add(Val(2),Val(3)))
print(e.eval())
assert e.eval() == 6