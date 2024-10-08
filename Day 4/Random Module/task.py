import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print(my_module.my_favourite_number)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

def heads_or_tails():
    out = random.random()
    if out < 0.5:
        print(f"Heads: {out}")
    else: print(f"Tails: {out}")

heads_or_tails()