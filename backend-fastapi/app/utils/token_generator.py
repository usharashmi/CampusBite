import random


def generate_token():
    return f"CB{random.randint(1000, 9999)}"