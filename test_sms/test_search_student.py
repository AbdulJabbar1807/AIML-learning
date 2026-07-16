from Project_01.student_management_system import search_student

def test_search_student_empty(capsys):
    test_list = []
    search = 1
    search_student(test_list,search)
    captured_output = capsys.readouterr()
    assert captured_output.out == "There are no student's to search in the list.\n"
    
def test_search_student_found(capsys):
    test_list = [{"id":1,"name":"Abdul"},
                 {"id":2,"name":"Jabbar"},
                 {"id":3,"name":"Khokhar"}]
    search_student(test_list,1)
    captured_output = capsys.readouterr()
    assert captured_output.out == "Student with ID: 1 and Name: Abdul is in the list.\n"
    
def test_search_student_not_found(capsys):
    test_list = [{"id":1,"name":"Abdul"},
                 {"id":2,"name":"Jabbar"},
                 {"id":3,"name":"Khokhar"}]
    search_student(test_list,4)
    captured_output = capsys.readouterr()
    assert captured_output.out == "Student with ID: 4 is not in the list.\n"
    