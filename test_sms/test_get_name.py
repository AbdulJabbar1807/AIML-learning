import io
import sys

from Project_01.student_management_system import get_name

def test_get_name_valid(monkeypatch):
    fake_input_stream = io.StringIO("Abdul\n")
    monkeypatch.setattr(sys,"stdin",fake_input_stream)
    result = get_name("Enter your name: ")
    
    assert result == "Abdul"
    
def test_get_name_for_integer_input(monkeypatch,capsys):
    fake_input_stream = io.StringIO("123\nAbdul\n")
    monkeypatch.setattr(sys,"stdin",fake_input_stream)
    
    result = get_name("Enter your name: ")
    captured_output = capsys.readouterr()
    
    assert result == "Abdul"
    assert "Please enter alphabetical letter's only.\n" in captured_output.out
    
def test_get_name_empty(monkeypatch,capsys):
    fake_input_stream = io.StringIO(" \nJabbar\n")
    monkeypatch.setattr(sys,"stdin",fake_input_stream)
    
    result = get_name("Enter your name: ")
    captured_output = capsys.readouterr()
    
    assert result == "Jabbar"
    assert "Name cant be empty!" in captured_output.out
     