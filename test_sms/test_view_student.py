from Project_01.student_management_system import view_student

def test_view_student_empty(capsys):
    test_list = []
    view_student(test_list)
    captured = capsys.readouterr()
    assert captured.out == "There is no student list to show!\n"
    
def test_view_student_details(capsys):
    test_list = [{"id":1,"name":"Abdul Jabbar"}]
    view_student(test_list)
    captured = capsys.readouterr()
    expected_output = (
        "Student's Info-\n"
        "ID     Name\n"
        "--------------------------------------------------\n"
        "1     Abdul Jabbar\n"
    )
    assert captured.out == expected_output
                   