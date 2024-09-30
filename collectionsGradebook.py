
def gradebook(name, gradeList):

    studentName = name
    studentGrades = gradeList
    studentGrades = studentGrades.split(',')
    letterGrade = ""
    studentAverage = 0
    for i in range(len(studentGrades)):
        studentGrades[i] = int(studentGrades[i])



    for i in range(len(studentGrades)):
        studentAverage += studentGrades[i]

    studentAverage = studentAverage / len(studentGrades)

    if studentAverage >= 90:
        letterGrade = "A"
    elif studentAverage >= 80:
        letterGrade = "B"
    elif studentAverage >= 70:
        letterGrade = "C"
    elif studentAverage >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"

    print(studentName)
    print()
    print("Average:\n", studentAverage)
    print()
    print("Letter Grade:\n", letterGrade)
    print()


gradebook(input("Enter student name:\n"), input("Enter student grades separated by commas:\n"))
gradebook(input("Enter student name:\n"), input("Enter student grades separated by commas:\n"))
gradebook(input("Enter student name:\n"), input("Enter student grades separated by commas:\n"))
gradebook(input("Enter student name:\n"), input("Enter student grades separated by commas:\n"))
gradebook(input("Enter student name:\n"), input("Enter student grades separated by commas:\n"))
gradebook(input("Enter student name:\n"), input("Enter student grades separated by commas:\n"))
gradebook(input("Enter student name:\n"), input("Enter student grades separated by commas:\n"))