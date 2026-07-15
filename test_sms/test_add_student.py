from Project_01.student_management_system import add_student
    
def test_add_student():
    test_list = []
    add_student(test_list,"Abdul Jabbar")
    assert test_list == [{"id":1,"name":"Abdul Jabbar"}]