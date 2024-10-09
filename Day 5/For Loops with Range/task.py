for number in range(1, 11, 3):  # Start, Stop (excluding), Step
    print(number)

#-----------------------------------------------------------------------------------------------------------------
final_sum = 0
for number in range(1, 101):
    final_sum += (number + (101 - number)) / 2

print(final_sum)