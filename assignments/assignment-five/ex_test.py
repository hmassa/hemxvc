import pytest
import System
import Staff
import Professor
import Student

def test_login(grading_system):
    username = 'saab'
    password =  'boomr345'
    grading_system.login(username, password)
    assert isinstance(grading_system.usr, Professor.Professor)
    assert grading_system.usr.name == username
    assert grading_system.usr.courses == grading_system.users[username]['courses']
    assert grading_system.usr.password == grading_system.users[username]['password']
    #pass

def test_password(grading_system):
    username = 'saab'
    password =  'boomr345'
    assert grading_system.check_password(username, password)
    password =  'wrongPassword'
    assert grading_system.check_password(username, password) == False
    password =  ''
    assert grading_system.check_password(username, password) == False
    #pass

def test_change_grade(grading_system):
    user = 'hdjsr7'
    course = 'databases'
    assignment = 'assignment2'
    grade = 95
    username = 'goggins'
    password =  'augurrox'
    grading_system.login(username,password)
    grading_system.usr.change_grade(user, course, assignment, grade)
    assert grade == grading_system.users[user]['courses'][course][assignment]['grade']
    # fail

def test_create_assignment(grading_system):
    assignment_name = 'assignment3'
    due_date = '3/15/20'
    course = 'databases'
    username = 'goggins'
    password =  'augurrox'
    grading_system.login(username, password)
    grading_system.usr.create_assignment(assignment_name, due_date, course)
    assert due_date == grading_system.courses[course]['assignments'][assignment_name]['due_date']
    #pass

def test_add_student(grading_system):
    student_name = 'abc123'
    course = 'software_engineering'
    username = 'goggins'
    password =  'augurrox'
    grading_system.login(username, password)
    grading_system.usr.add_student(student_name, course)
    assert course in grading_system.users[student_name]['courses']
    #fail

def test_drop_student(grading_system):
    student_name = 'hdjsr7'
    course = 'databases'
    username = 'goggins'
    password =  'augurrox'
    grading_system.login(username, password)
    grading_system.usr.drop_student(student_name, course)
    assert course not in grading_system.users[student_name]['courses']
    #pass

def test_submit_assignment(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'databases'
    assignment_name = 'assignment2'
    submission = 'I hope this works'
    submission_date = '2/20/20'
    grading_system.login(username, password)
    grading_system.usr.submit_assignment(course, assignment_name, submission, submission_date)
    assert assignment_name in grading_system.users[username]['courses'][course]
    assert submission == grading_system.users[username]['courses'][course][assignment_name]['submission']
    assert submission_date == grading_system.users[username]['courses'][course][assignment_name]['submission_date']
    assert False == grading_system.users[username]['courses'][course][assignment_name]['ontime']
    #fail

def test_check_ontime(grading_system):
    username = 'akend3'
    password = '123454321'
    grading_system.login(username, password)
    due_date = '2/5/20'
    submission_date = '2/7/20'
    assert grading_system.usr.check_ontime(submission_date, due_date) == True
    submission_date = '2/4/20'
    assert grading_system.usr.check_ontime(submission_date, due_date) == False
    #fail

def test_check_grades(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'databases'
    grading_system.login(username, password)
    grades = grading_system.usr.check_grades(course)
    actual_grades = []
    assignments = grading_system.users[username]['courses'][course]
    for key in assignments:
        actual_grades.append([key, grading_system.users[username]['courses'][course][key]['grade']])
    assert actual_grades == grades
    #pass

def test_view_assignments(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'databases'
    grading_system.login(username, password)
    assignments = grading_system.usr.view_assignments(course)
    actual_assignments = []
    list = grading_system.courses[course]['assignments']
    for key in list:
        actual_assignments.append([key, grading_system.courses[course]['assignments'][key]['due_date']])
    assert actual_assignments == assignments
    #fail

def test_drop_nonstudent(grading_system):
    student_name = 'hdjsr7'
    course = 'comp_sci'
    username = 'goggins'
    password =  'augurrox'
    grading_system.login(username, password)
    grading_system.usr.drop_student(student_name, course)
    assert course not in grading_system.users[student_name]['courses']
    # fail - student is not enrolled in specified course

def test_wrong_professor_add(grading_system):
    username = 'saab'
    password =  'boomr345'
    grading_system.login(username, password)
    student = 'yted91'
    course = 'databases'
    grading_system.usr.add_student(student, course)
    assert username == grading_system.courses[course]['professor']
    # fail - even if add_student worked, saab should not be able to add a student
    # to a course he does not teach

def test_wrong_staff_assignment(grading_system):
    username = 'cmhbf5'
    password =  'bestTA'
    grading_system.login(username, password)
    course = 'comp_sci'
    grading_system.usr.create_assignment('test', '1/1/20', course)
    assert username in grading_system.courses[course]['ta']
    # fail - TA/professor can create an assignment for a course they do not teach

def test_grade_wrong_class(grading_system):
    username = 'cmhbf5'
    password =  'bestTA'
    grading_system.login(username, password)
    student = 'akend3'
    course = 'comp_sci'
    assignment = 'assignment1'
    grade = 10
    grading_system.usr.change_grade(user, course, assignment, grade)
    assert username in grading_system.courses[course]['ta']
    # fail - TA/professor can change an assignment grade for a course they do not teach

def test_check_nonstudent_grades(grading_system):
    username = 'cmhbf5'
    password =  'bestTA'
    grading_system.login(username, password)
    student = 'akend3'
    course = 'comp_sci'
    grading_system.usr.check_grades(student, course)
    assert username in grading_system.courses[course]['ta']
    # fail - TA/professor can view grades for a student not in their course


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
