import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

n = random.randint(0, len(friends)-1)

pick = friends[n]

print(f"Chosen friend is {pick}")

# OR

pick = random.choice(friends)

print(f"Chosen friend is {pick}")