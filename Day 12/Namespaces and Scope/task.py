enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#-------------------------------------------------------------------------------------------
# Local Scope. Variable defined inside the function only
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)


# Global Scope. Variable defined outside the function.
# Variable and function in the same namespace (or indentation level)
# player_health = 10
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()


# function drink_potion outside the namespace of the callable drink_potion.
# Gives an unresolved reference error
# player_health = 10
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#
# drink_potion()