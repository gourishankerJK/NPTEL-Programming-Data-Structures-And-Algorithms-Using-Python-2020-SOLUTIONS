"""For this assignment, you have to write a complete Python program.

You may define additional auxiliary functions as needed.
In all cases you may assume that the input to your program has the expected format, so your program does not have to check for malformed inputs.
There are 2 public test cases and 6 (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases and report a score on 100.
Ignore warnings about "Presentation errors".
The academic office at the Hogwarts School of Witchcraft and Wizardry has compiled data about students' grades. The data is provided as text from standard input in three parts: information about courses, information about students and information about grades. Each part has a specific line format, described below..

Information about courses
Line format: Course Code~Course Name~Semester~Year~Instructor
Information about students
Line format: Roll Number~Full Name
Information about grades
Line format: Course Code~Semester~Year~Roll Number~Grade
The possible grades are A, AB, B, BC, C, CD, D with corresponding grade points 10, 9, 8, 7, 6, 5 and 4. The grade point average of a student is the sum of his/her grade points divided by the number of courses. For instance, if a student has taken two courses with grades A and C, the grade point average is 8.50 = (10+7)÷2. If a student has not completed any courses, the grade point average is defined to be 0.

You may assume that the data is internally consistent. For every grade, there is a corresponding course code and roll number in the input data.

Each section of the input starts with a line containing a single keyword. The first section begins with a line containing Courses. The second section begins with a line containing Students. The third section begins with a line containing Grades. The end of the input is marked by a line containing EndOfInput.

Write a Python program to read the data as described above and print out a line listing the grade point average for each student in the following format:

Roll Number~Full Name~Grade Point Average
Your output should be sorted by Roll Number. The grade point average should be rounded off to 2 digits after the decimal point. Use the built-in function round().

Here is a sample input and its corresponding output.

Sample Input

Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput
Sample Input

SLY2301~Hannah Abbott~9.5
SLY2302~Euan Abercrombie~7.5
SLY2303~Stewart Ackerley~8.0
SLY2304~Bertram Aubrey~0
SLY2305~Avery~8.5
SLY2306~Malcolm Baddock~6.5
SLY2307~Marcus Belby~8.0
SLY2308~Katie Bell~9.5
SLY2309~Sirius Orion Black~9.0"""


def courses():
    while True:
        s = input()
        if (s == "Students"):
            break


def students():
    studentinfo = []
    while True:
        s = input()
        if (s == "Grades"):
            break
        else:
            studentinfo.append((s.split("~")[0], s.split("~")[1]))
    return studentinfo


def grades(studentinfo):
    grade = {}
    freq = {}
    points = {"A": 10, "AB": 9, "B": 8, "BC": 7, "C": 6, "CD": 5, "D": 4}
    while True:
        s = input()
        if (s == "EndOfInput"):
            break
        else:
            roll_no = s.split("~")[3]
            freq[roll_no] = freq.get(roll_no, 0) + 1
            try:
                grade[roll_no] = (grade[roll_no] + points[s.split("~")[4]])
            except:
                grade[roll_no] = grade.get(roll_no, points[s.split("~")[4]])
    for i, v in studentinfo:
        try:
            grade[i] = round(grade[i] / freq[i], 2)
        except:
            grade[i] = 0
    return grade


faltu = input()
courses()
studentinfo = students()
grade = grades(studentinfo)
final_result = []
for roll_no, name in studentinfo:
    final_result.append((roll_no, name, grade[roll_no]))
final_result.sort()
for student in final_result:
    print("{}~{}~{}".format(student[0], student[1], student[2]))
