import sqlite3

connection = sqlite3.connect(':memory:')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE collegeStudent1(
                  student_id integer, name text, birthYear integer, 
                  major text, gpa real, gradYear integer)""")

def displayTable():
    cursor.execute("SELECT * FROM collegeStudent1")
    return cursor.fetchall()

def get_uniqueStudent(id):
    cursor.execute("SELECT * FROM collegeStudent1 WHERE student_id = :student_id", {'student_id': id})
    return cursor.fetchone()

def add_newStudent(id, name, birthYear, gpa, major, gradYear ):
    with connection:
        cursor.execute("INSERT INTO collegeStudent1 VALUES(:student_id, :name, :birthYear, :gpa, :major, :gradYear)",
                       {'student_id': id, 'name': name, 'birthYear': birthYear, 'gpa': gpa,
                        'major': major, 'gradYear': gradYear})
        return cursor.fetchone()

def update_gpa(stu, gpa):
    with connection:
        cursor.execute("""UPDATE collegeStudent1 SET gpa = :gpa
                       WHERE name = :name""", {'name': stu, 'gpa': gpa})

def remove_student(name):
    with connection:
        cursor.execute("DELETE from collegeStudent1 WHERE name = :name",
                       {'name': name})

cursor.execute("INSERT INTO collegeStudent1 VALUES(1, 'Gorge', '03/26/96', 3.0, 'Computer Science', 2020)")
cursor.execute("INSERT INTO collegeStudent1 VALUES(2, 'Kennard', '10/24/97', 3.6, 'Health Science', 2021)")
cursor.execute("INSERT INTO collegeStudent1 VALUES(3, 'DeAndre', '11/13/96', 2.9, 'Math', 2020)")
cursor.execute("INSERT INTO collegeStudent1 VALUES(4, 'Jonny', '09/26/94', 2.5, 'English', 2017)")
cursor.execute("INSERT INTO collegeStudent1 VALUES(5, 'Johanna', '04/03/94', 3.2, 'Computer Science', 2018)")

cursor.execute("SELECT * FROM collegeStudent1")

result = add_newStudent(7, 'Larry', 1990, 2.9, 'Sports Mgmt', 2014)
result2 = get_uniqueStudent(3)
result3 = cursor.execute("SELECT * FROM collegeStudent1")
result3 = cursor.fetchall()
resultALL = displayTable()

print(resultALL)

connection.commit()
connection.close()








