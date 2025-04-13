# Python Practice Solutions 🐍

This repository contains Python practice questions along with their solved code. Each solution includes the question, approach, and implementation.

## 📚 Topics Covered
- Functions
- Loops
- Recursion
- Strings
- Lists
- File Handling
- OOP Basics

## 🔧 How It's Organized
Each `.py` file contains:
- The original question as a comment
- A solution written in Python

## 💡 Example

### 01.py
```python
# Question: Write a Python program to compute factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
