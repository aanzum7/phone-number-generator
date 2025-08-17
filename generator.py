# generator.py
import random
import pandas as pd

RNG = random.SystemRandom()

def generate_numbers(operator: str, prefix: str, count: int) -> pd.DataFrame:
    results = set()
    while len(results) < count:
        suffix = str(RNG.randrange(0, 100_000_000)).zfill(8)
        results.add(prefix + suffix)
    return pd.DataFrame({"Mobile_Number": list(results)})
