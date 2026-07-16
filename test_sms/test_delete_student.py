from Project_01.student_management_system import delete_student

def test_delete_student_empty(capsys):
    test_list = []
    delete = 1
    delete_student(test_list,delete)
    captured_output = capsys.readouterr()
    assert captured_output.out == "Nothing to delete as no student are there in the list.\n"
    
def test_delete_student_found(capsys):
    test_list = [{"id":1,"name":"Abdul"},
                 {"id":2,"name":"Jabbar"},
                 {"id":3,"name":"Khokhar"}]
    delete = 2
    delete_student(test_list,delete)
    captured_output = capsys.readouterr()
    assert captured_output.out == "Student successfully removed from the list.\n"
    
def test_delete_student_not_found(capsys):
    test_list = [{"id":1,"name":"Abdul"},
                 {"id":2,"name":"Jabbar"},
                 {"id":3,"name":"Khokhar"}]
    delete = 4
    delete_student(test_list,delete)
    captured_output = capsys.readouterr()
    assert captured_output.out == "no student with ID: 4 exist to remove from the list.\n"