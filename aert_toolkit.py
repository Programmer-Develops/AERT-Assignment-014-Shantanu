# Algorithmic Efficiency & Recursion Toolkit (AERT)

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class AERT:
    def __init__(self):
        self.stack = StackADT()           
        self.fib_naive_counter = 0
        self.fib_memo_counter = 0

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def fib_naive(self, n):
        self.fib_naive_counter += 1
        if n < 0:
            raise ValueError("Fibonacci not defined for negative numbers")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib_naive(n - 1) + self.fib_naive(n - 2)

    def fib_memo(self, n, memo=None):
        self.fib_memo_counter += 1
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n < 0:
            raise ValueError("Fibonacci not defined for negative numbers")
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = self.fib_memo(n - 1, memo) + self.fib_memo(n - 2, memo)
        memo[n] = result
        return result

    # ── Tower of Hanoi (recursive) + uses stack to store moves
    def hanoi(self, n, source="A", aux="B", dest="C"):
        if n == 1:
            move = f"Move disk 1 from {source} to {dest}"
            print(move)
            self.stack.push(move)
            return

        self.hanoi(n - 1, source, dest, aux)
        move = f"Move disk {n} from {source} to {dest}"
        print(move)
        self.stack.push(move)
        self.hanoi(n - 1, aux, source, dest)

    def binary_search(self, arr, key, low=0, high=None):
        if high is None:
            high = len(arr) - 1
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return self.binary_search(arr, key, low, mid - 1)
        else:
            return self.binary_search(arr, key, mid + 1, high)

if __name__ == "__main__":
    aert = AERT()

    print("=== AERT - Algorithmic Efficiency & Recursion Toolkit ===\n")

    print("Factorial:")
    for n in [0, 1, 5, 10]:
        print(f"  {n}! = {aert.factorial(n)}")
    print()

    print("Fibonacci (naive vs memo):")
    tests = [5, 10, 20, 30]
    for n in tests:
        aert.fib_naive_counter = 0
        res_n = aert.fib_naive(n)
        calls_n = aert.fib_naive_counter

        aert.fib_memo_counter = 0
        res_m = aert.fib_memo(n)
        calls_m = aert.fib_memo_counter

        print(f"  fib({n:2}) = {res_n:10}   naive calls: {calls_n:6}")
        print(f"             = {res_m:10}   memo calls:  {calls_m:6}")
    print()

    print("Tower of Hanoi (N=3):")
    print("-" * 35)
    aert.hanoi(3)
    print("\nMoves stored in StackADT (size =", aert.stack.size(), "):")
    while not aert.stack.is_empty():
        print("  " + aert.stack.pop())
    print()

    print("Binary Search:")
    arr = [1, 3, 5, 7, 9, 11, 13]
    for key in [7, 1, 13, 2]:
        idx = aert.binary_search(arr, key)
        print(f"  Search {key:2} → index {idx}")
    print("  Empty list search for 10 →", aert.binary_search([], 10))
    print()

    print("=== End of output ===")