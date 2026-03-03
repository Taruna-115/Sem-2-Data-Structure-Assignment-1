"""
Algorithmic Efficiency & Recursion Toolkit (AERT)
Data Structures - Unit 1 Assignment

Name of the School:        	School of Engineering & Technology 
Program: 					B.Tech (AI and ML) 
Course Title:				Data Structures 
Course Code:				ETCCDS202 
Unit Title:					Foundations & Algorithmic Analysis 
Student Name:				Taruna Tewatia 
Roll Number:				2501730115 
Section:					A 
Semester:					2 
Batch:					    2025-26 
Submitted To:				Mrs. Neetu Chauhan 
Submission Date:			5 March 2026 
"""


# PART A – Stack ADT (using class)


class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)



# PART B – Recursive Factorial and Fibonacci


# Recursive Factorial
def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed as input")
    if n == 0:
        return 1
    return n * factorial(n - 1)



# Recursive Fibonacci (Naive + Memoized)
fib_calls_naive = 0
fib_calls_memo = 0

# Naive
def fib_naive(n):
    global fib_calls_naive
    fib_calls_naive += 1

    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# Memoized
def fib_memo(n, memo=None):
    global fib_calls_memo
    fib_calls_memo += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]




# PART C – Tower of Hanoi
# Using Stack to Store Moves


def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        stack.push(f"Move disk 1 from {source} to {destination}")
        return

    hanoi(n - 1, source, destination, auxiliary, stack)
    stack.push(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination, stack)




# PART D – Recursive Binary Search


def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)






# MAIN FUNCTION


def main():

    print("Algorithmic Efficiency & Recursion Toolkit (AERT)")
    print("=======================================================")

    

    # Stack ADT Demo

    print("\nStack ADT Demo")
    stack = StackADT()
    
    stack.push(100)
    stack.push(200)
    stack.push(300)
    
    print("Current size:", stack.size())
    print("Top element:", stack.peek())
    
    print("Popped:", stack.pop())
    print("Size after pop:", stack.size())
    
    print("Is stack empty?", stack.is_empty())



    # Factorial Test Cases

    print("\nFactorial Test Cases:")
    for n in [0, 1, 5, 10]:
        print(f"{n}! = {factorial(n)}")

    

    # Fibonacci Test Cases

    print("\nFibonacci Test Cases (Naive vs Memoized):")

    for n in [5, 10, 20, 30]:

        global fib_calls_naive, fib_calls_memo

        fib_calls_naive = 0
        result_naive = fib_naive(n)

        fib_calls_memo = 0
        result_memo = fib_memo(n, {})

        print(f"\nn = {n}")
        print(f"Naive Result: {result_naive}, Calls: {fib_calls_naive}")
        print(f"Memo Result:  {result_memo}, Calls: {fib_calls_memo}")

    

    # Tower of Hanoi (N = 3)

    print("\nTower of Hanoi (N = 3):")

    moves_stack = StackADT()
    hanoi(3, 'A', 'B', 'C', moves_stack)

    temp_stack = StackADT()                 # Print moves in correct order
    while not moves_stack.is_empty():
        temp_stack.push(moves_stack.pop())

    while not temp_stack.is_empty():
        print(temp_stack.pop())


    
    # Binary Search Test Cases

    print("\nRecursive Binary Search Test Cases:")

    arr = [1, 3, 5, 7, 9, 11, 13]

    for key in [7, 1, 13, 2]:
        index = binary_search(arr, key, 0, len(arr) - 1)
        print(f"Search {key} -- Index: {index}")

    empty_arr = []                          # Empty list case
    print("Empty array search -- Index:",
          binary_search(empty_arr, 5, 0, -1))






# To ensure run only if executed directly:
if __name__ == "__main__":
    main()