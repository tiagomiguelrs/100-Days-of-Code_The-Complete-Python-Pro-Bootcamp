bmi = 84 / 1.65 ** 2
print(bmi)

# Using int() floors the number
print(int(bmi))

# Using round() rounds the number to the nearest integer
print(round(bmi))

# But round() takes to positional arguments
print(round(bmi, 2))

# Assignment will take the variable value (integer or float) and perform the
# operation before the equal sign like score = score + value
score = 10

score += 2
print(score)

score -= 5
print(score)

# f-strings
is_winning = True
print(f"The score is {score} and your bmi is {bmi}, but are you winning?\n")
print(f"{is_winning==True}")
