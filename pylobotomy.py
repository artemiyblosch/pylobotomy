def end(f):
    """Evaluates the function itself(ends your lobotomy code):

@end
...some lobotomy code...
def main(): pass

does this code"""
    return f()

def selfeq(thing):
    """
@selfeq(14)
def main(): pass

main = 14 now"""
    return lambda f: thing

def eq(d):
    """Makes every assignment from d:

@eq({'a':12,'b':4})
def main(): pass

a = 12; b = 4 now"""
    def _(F):
        def __(*a,**k):
            F(*a,**k)
            for prop in d:
                globals()[prop] = d[prop]
        return __
    return _

def do(f, after=True):
    """Calls lambda before(if after == False) of after the function itself

@end
@do(lambda: print("Hello world"))
def main(): pass

Hello world program in pylobotomy"""
    def _(F):
        def __(*a,**k):
            if not after: f()
            F(*a,**k)
            if after: f()
        return __
    return _

def ret(v):
    """Returns a value from function

@ret(14)
def main(): pass

main returns 14"""
    def _(F):
        def __(*a,**k):
            F(*a,**k)
            return v
        return __
    return _

class ddict:
    """dict but with default"""
    def __init__(self,D = {},E = None):
        self.D = D
        self.E = E
    
    def __getitem__(self, __name: str):
        return self.D[__name] if __name in self.D else self.E

def forever():
    """iterator that yields True forever(until you send False to it)"""
    done = True
    while done: 
        done = (yield True)
        done = True if done == None else done
    yield False

class ListNodeError(BaseException):
    """Linked list, but it's an exception????"""
    def __init__(self, val, __context__=None): 
        super().__init__()
        self.__context__ = __context__
        self.val = val

    def last_elem(self):
        res = self
        while res.__context__ != None: res = res.__context__
        return res
    
    def __add__(self, other):
        self.last_elem().__context__ = other
        return self
    
    def __next__(self):
        res = self
        while res.__context__ != None:
            yield res.val
            res = res.__context__
        return False
    
    def __iter__(self):
        res = self
        while res != None:
            yield res.val
            res = res.__context__
        return False
    
    def __repr__(self):
        return f"<{self.val.__repr__()}, {self.__context__.__repr__()}"
    
    def __str__(self) -> str:
        return self.__repr__()

def pass_do[A](f : callable, thing : A) -> A:
    """Calls f on thing and returns thing"""
    f(thing)
    return thing

def tryexc(tr,ex,el,fin):
    """Tries to do tr. If exception have been raised, finds it in ex and executes a corresponding function(with an argument: exception itself). if no exception have been raised, executes el. Finally fin.
@end
@tryexc(lambda: print(1/int(input())), {ZeroDivisionError : lambda e: print(e)}, lambda: 0, lambda: print("ok bye"))
def main(): pass

Prints the recipocal of input, but if division by zero occurs, prints the exception, then prints "ok bye"."""
    def _(F):
        def __(*a,**k):
            F(*a,**k)
            try: tr()
            except Exception as e:
                res = []
                for i in ex:
                    if isinstance(e,i):
                        res.append(ex[i](e))
                if res == []: raise e from None
            else: el()
            finally: fin()
        return __
    return _

def repeat(f : callable, t : int):
    """iterator. 
    Repeats f (gets countdown as an argument) t times.
    (or you can send False to stop) As a bonus yields countdown value back.
    (you can send a new counter's value)"""
    countdown = t
    while countdown > 0:
        f(countdown)
        countdown -= 1
        t = countdown
        countdown = (yield countdown)
        if countdown == False: break
        countdown = t if countdown == None else countdown
    f(countdown)
    return False

class inflist:
    """List but with infinitely repeating part."""
    def __init__(self, finite : list, infinite : list) -> None:
        self.finite = finite
        self.infinite = infinite
        for i in range(1,len(infinite)//2 + 1):
            if len(infinite) % i != 0: continue
            a = [infinite[x : x+i] for x in range(0,len(infinite),i)]
            res = True
            for j in range(1,len(a)): 
                if a[j] != a[j-1]: res = False
            if res: 
                self.infinite = a[0]
                break
        while self.finite[-len(self.infinite):] == self.infinite: self.finite = self.finite[0:-len(self.infinite)]
    
    def __getitem__(self,index : int | slice) -> any:
        if isinstance(index,slice): 
            index = slice(index.start if index.start != None else 0, index.stop if index.stop != None else -1, index.step if index.step != None else 1)
            return [self[i] for i in range(index.start,index.stop, index.step)]
        if index < 0:
            return self.infinite[index % -len(self.infinite)]
        if index >= len(self.finite): return self.infinite[(index - len(self.finite)) % len(self.infinite)]
        return self.finite[index]

    def __hash__(self):
        if self.infinite == []: return hash(self.finite)
        if self.finite == []: return ~hash(self.infinite)
        else: (hash(self.finite) * ~hash(self.infinite)) ^ 6
    
    def __bool__(self) -> bool:
        return self.finite == [] and self.infinite == []
    
    def __setitem__(self,index : int | slice, thing):
        if index < 0:
            return NotImplemented
        if index >= len(self.finite):
            index += 1
            self.infinite, self.finite = self[index : index+len(self.infinite)], [self[i] for i in range(index)]
            self.finite[-1] = thing
            return
        self.finite[index] = thing
    
    def __str__(self):
        return f"[{str(self.finite)[1:-1]} | {str(self.infinite)[1:-1]}, ...>"
    
    def __len__(self):
        """returns the length of finite part."""
        return len(self.finite)
    
    def __add__(self,other):
        """Adds two lists, but if the second is just a list, adds it to the finite part."""
        if isinstance(other, type(self)):
            self.finite += other.finite
            self.infinite += other.infinite
        self.finite += other

    def __radd__(self,other):
        """Same as add, but reversed..."""
        if isinstance(other, type(self)):
            self.finite = other.finite + self.finite
            self.infinite = other.infinite + self.infinite
        self.finite = other + self.finite
    
    def __matmul__(self,other):
        """Adds two lists, but if the second is just a list, adds it to the infinite part."""
        if isinstance(other, type(self)):
            self.finite += other.finite
            self.infinite += other.infinite
        self.infinite += other
    
    def __radd__(self,other):
        """Same as matmul(sus add), but reversed..."""
        if isinstance(other, type(self)):
            self.finite = other.finite + self.finite
            self.infinite = other.infinite + self.infinite
        self.infinite = other + self.infinite
    
    def zip(self,other):
        fl = max(len(self.finite),len(other.finite))
        offself = inflist([], self[fl : fl + len(self.infinite)])
        offother = inflist([], other[fl : fl + len(other.infinite)])
        return inflist([(self[i],other[i]) for i in range(fl)],[(offself[i],offother[i]) for i in range(len(offself.infinite) * len(offother.infinite))])
    
    def map(self,f : callable): 
        return inflist([f(i) for i in self.finite],[f(i) for i in self.infinite])

