costs = [1, 3, 2, 5, 1, 3]
students = [1, 2, 3, 4, 5, 6]

# 1. Pair, sort, and extract only the student (the second item 't[1]')
sorted_students = [t[2] for t in sorted(zip(costs, students))]

print(sorted_students)
# Output: [1, 5, 3, 2, 6, 4]
