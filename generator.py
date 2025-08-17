# generator.py
import random

RNG = random.SystemRandom()  # more secure random generator

def generate_numbers(operator: str, prefix: str, count: int) -> list[str]:
    """
    Generate `count` unique mobile numbers for a given operator and prefix.
    All numbers are 11 digits (prefix + 8-digit suffix).
    """
    numbers = set()
    while len(numbers) < count:
        suffix = ''.join(str(RNG.randint(0, 9)) for _ in range(8))
        numbers.add(prefix + suffix)
    return list(numbers)
