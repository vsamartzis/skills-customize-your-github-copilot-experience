# Legacy Code - Refactor This!

# This code needs refactoring. Follow best practices to improve it.

def calc(l):
    t = 0
    for i in l:
        if i % 2 == 0:
            t = t + i
    return t

def p(lst):
    result = []
    for item in lst:
        if item > 0:
            result.append(item)
    for idx, itm in enumerate(result):
        result[idx] = itm * itm
    return result

class S:
    def __init__(self, n):
        self.n = n
        self.v = []
    
    def a(self, x):
        if len(self.v) < self.n:
            self.v.append(x)
        else:
            print("Stack full")
    
    def r(self):
        if len(self.v) > 0:
            return self.v.pop()
        else:
            print("Stack empty")

# Example usage
nums = [1, 2, 3, 4, 5, 6]
print(calc(nums))
print(p(nums))

s = S(5)
s.a(10)
s.a(20)
s.a(30)
print(s.r())
