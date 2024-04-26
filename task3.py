

class Stack:
    def __init__(self):
        self.stack = []

    # Додаємо елемент до стеку
    def push(self, item):
        self.stack.append(item)

    # Видаляємо елемент зі стеку
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # Перевіряємо, чи стек порожній
    def is_empty(self):
        return len(self.stack) == 0

    # Переглядаємо верхній елемент стеку без його видалення
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

def check_balanced(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if opening_brackets.index(top_char) != closing_brackets.index(char):
                return False
    return stack.is_empty()

# Приклади
expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }:"
]

for exp in expressions:
    if check_balanced(exp):
        print(f"{exp}: Симетрично")
    else:
        print(f"{exp}: Несиметрично")
