from app.io.input import read_file_builtin

def test_read_file():
    result = read_file_builtin("data/input.txt")
    assert result is not None

def test_read_file_not_empty():
    result = read_file_builtin("data/input.txt")
    assert len(result) > 0

def test_read_file_type():
    result = read_file_builtin("data/input.txt")
    assert isinstance(result, str)