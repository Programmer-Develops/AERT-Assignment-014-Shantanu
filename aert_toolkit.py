# Algorithmic Efficiency & Recursion Toolkit (AERT) in Python

class StackADT:
    def __init__(self, items = []):
        self.items = items
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        if self.is_empty():
            return self.items.pop()
        else:
            self.items.pop(item)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)



class AERT(StackADT):
    def __init__(self, num):
        super().__init__()
        self.num = num
    
    def factorial(self):
        if self.num < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        else:
            return 1 if self.num == 0 else self.num * self.factorial(self.num - 1)
    
    def fib_naive(self): # simple recursive Fibonacci
        if self.num < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        elif self.num == 0:
            return 0
        elif self.num == 1:
            return 1
        else:
            return self.fib_naive(self.num - 1) + self.fib_naive(self.num - 2)
        
    def fib_memo(self, memo=None): # recursive fibonacci with memrization (store results)
        if memo is None:
            memo = {}
        if self.num in memo:
            return memo[self.num]
        if self.num < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        elif self.num == 0:
            return 0
        elif self.num == 1:
            return 1
        else:
            result = self.fib_memo(self.num - 1, memo) + self.fib_memo(self.num - 2, memo)
            memo[self.num] = result
            return result