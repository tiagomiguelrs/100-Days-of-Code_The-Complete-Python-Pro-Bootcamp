# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#-----------------------------------------------------------------------------------------
# Ideally do like this:
# Never change local variables to global variables. It is confusing and prone to error and bugs.


enemies = 1


def increase_enemies(enemy):
    enemy += 1
    print(f"enemies inside function: {enemy}")
    return enemy


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")
