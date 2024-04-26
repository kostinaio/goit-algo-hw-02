
import re
from collections import deque

def is_palindrome(s: str) -> bool:
    # Перетворюємо рядок у нижній регістр та видалємо пробіли та спеціальні символи
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    # Створюємо двосторонню чергу
    queue = deque(s)
    
    # Порівнюємо символи з обох кінців черги
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True

# Приклади використання
print(is_palindrome("tenet"))                                 # Виведе: True
print(is_palindrome("race car"))                              # Виведе: True
print(is_palindrome("hello"))                                 # Виведе: False
print(is_palindrome("Я НаВчаюсь у GOIT!"))                    # Виведе: False
print(is_palindrome("І розморозь зором зорі"))                # Виведе: True
print(is_palindrome("Козак з казок «Бувалу булаву б… »"))     # Виведе: True