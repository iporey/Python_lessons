students_num = int(input("Enter number students: "))

total_score = 0

# Initial value for both highest and lowest score
highest_score = None

lowest_score = None

for i in range(students_num):
    student_score = int(input(f"Enter student score{i+1}: "))
    print(f"score entered: {student_score}")

    # Add to total

    total_score += student_score

    # set first value

    if highest_score is None:
        highest_score = student_score
        lowest_score = student_score

    else:

        if student_score > highest_score:
            highest_score = student_score

        if student_score < lowest_score:
            lowest_score = student_score
# Average
average_score = total_score / students_num

print("\n=====RESULTS=====")
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
