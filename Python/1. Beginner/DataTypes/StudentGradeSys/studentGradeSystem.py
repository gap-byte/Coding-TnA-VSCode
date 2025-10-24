print("📚 Student Grade System 📚")

student_name = input("Enter student name: ")       # string
math_score = int(input("Enter Math score (0-100): "))  # int
science_score = int(input("Enter Science score (0-100): ")) # int
average_score = (math_score + science_score) / 2   # float
passed = average_score >= 60   # boolean

print("\n--- Report Card ---")
print(f"Student: {student_name}")
print(f"Math: {math_score}, Science: {science_score}")
print(f"Average Score: {average_score}")
print(f"Passed: {passed}")
