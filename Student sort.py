student_list = [
    ["john", 17, 88]
]

classroom = {"students": student_list}

name = input("Enter student name: ")
age = int(input("Enter student age: "))
score = int(input("Enter student score: "))

New = [name, age, score]
classroom["students"].append(New)

Remove = input("Enter student name to remove: ")

for s in classroom["students"]:
    if s[0] == Remove:
        classroom["students"].remove(s)
        print(f"{Remove} has been removed.")
        break
else:
    print(f"{Remove} not found in the list.")
    
highest_grade = max(s[2] for s in classroom["students"])
print("Highest Grade:", highest_grade)

n = len(classroom["students"])

for i in range(n - 1):  
    for j in range(n - 1):  
        score_now = classroom["students"][j][2]
        score_next = classroom["students"][j + 1][2]

        if score_now < score_next:  
            classroom["students"][j], classroom["students"][j + 1] = classroom["students"][j + 1], classroom["students"][j]

print("Final Classroom Dictionary:")
print(classroom)