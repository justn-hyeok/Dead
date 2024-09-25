import random

def lotto():
    n = list(range(1, 46)) 
    random.shuffle(n)
    return sorted(n[:6])

print(f"로또 번호 : {lotto()}")
