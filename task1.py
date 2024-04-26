

import queue
import threading
import time

# Створюємо лічильник для генерації унікальних номерів заявок
request_counter = 0

# Створюємо черги заявок
request_queue = queue.Queue()

# Генеруємо заявки
def generate_request():
    global request_counter
    while True:
        # Сворюємо унікальний номер заявки
        request_counter += 1
        new_request = f"Request-{request_counter}"
        # Додаємо заявку до черги
        request_queue.put(new_request)
        print("Заявка створена і додана до черги:", new_request)
        time.sleep(2)  # Затримка для імітації інтервалу між заявками

# Обробляємо заявки та видаляємо з черги 
def process_request():
    while True:
        if not request_queue.empty():
            request = request_queue.get()
            print("Заявка оброблена:", request)
            time.sleep(1)  # Затримка для імітації часу обробки заявки
        else:
            print("Черга порожня")
        time.sleep(1)  # Затримка перед наступною перевіркою черги

# Створюємо потоки для генерації та обробки заявок
generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

# Запускаємо потоки
generator_thread.start()
processor_thread.start()

# Очікуємо завершення потоків
generator_thread.join()
processor_thread.join()
