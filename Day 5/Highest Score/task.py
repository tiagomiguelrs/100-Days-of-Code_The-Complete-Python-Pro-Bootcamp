student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#----------------------------------------------------------------------------------------------------------------
total_exam_score = sum(student_scores)

sum = 0
for score in student_scores:
    sum += score

print(sum)

#-----------------------------------------------------------------------------------------------------------------
max_exam_score = max(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

print(range(1, 10))
