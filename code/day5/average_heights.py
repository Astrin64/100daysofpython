#day5
#180 156 170 199 175

student_heights = input("Enter a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

#find total height
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

#find num count of heights
num_of_heights = 0
for height in student_heights:
    num_of_heights += 1
print(num_of_heights)

#find average height
avg_height = total_height / num_of_heights
print(avg_height)