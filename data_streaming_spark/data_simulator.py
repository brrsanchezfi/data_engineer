import random
import time

def generate_data():
    while True:

        yield random.randint(1, 100)  # Genera números aleatorios del 1 al 100
        time.sleep(1)  # Espera 1 segundo entre cada dato
