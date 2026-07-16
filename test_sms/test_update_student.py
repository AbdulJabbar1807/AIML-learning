from Project_01.student_management_system import update_student

def test_update_student_empty(capsys):
    test_list = []
    update = 1
    name = "AJ"
    update_student(test_list,update,name)
    captured_output = capsys.readouterr()
    assert captured_output.out == "No such student to update in the list.\n"
    
def test_update_student_list(capsys):
    test_list = [{"id":1,"name":"Abdul"},
                 {"id":2,"name":"Jabbar"},
                 {"id":3,"name":"Khokhar"}]
    update = 1
    name = "AJ"
    update_student(test_list,update,name)
    
    assert test_list == [ {"id":1,"name":"AJ"},
                        {"id":2,"name":"Jabbar"},
                        {"id":3,"name":"Khokhar"}]
    
def test_update_list_not_found(capsys):
    test_list = [{"id":1,"name":"Abdul"}]
    update = 2
    name = "AJ"
    update_student(test_list,update,name)
    captured_output = capsys.readouterr()
    
    assert captured_output.out == "No student with ID: 2 found in the list.\n"
    
    