# student score management

students = {}  # dictionary {name:[scores]}

students_name = set()  # to avoid duplication

# Add_students
for i in range(5):
    name = input("Enter name: ")

    if name in students_name:
        print("Student already exist!")
        continue

    students_name.add(name)

    scores = []

    for j in range(5):
        score = int(input(f"Enter score{j+1} for {name}: "))
        scores.append(score)
    students[name] = scores

    # Process data
print("\n------Results-------")

top_student = ("", 0)  # tuple (name, average)
for name, scores in students.items():
    avg = sum(scores) / len(scores)

    # Assign Grade
    if avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"{name}: Avg = {avg:.2f}, grade = {grade}")

    # Track top_student
    if avg > top_student[1]:
        top_student = (name, avg)

print(f"\nTop_student: {top_student[0]} with {top_student[1]:.2f}")
