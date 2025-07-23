import pytest
from main1 import FileReader, UpperCaseFileReader, deco

def test_filename_property(tmp_path):
    f = tmp_path / "f.txt"
    f.write_text("abc\n")
    obj = FileReader(str(f))
    assert obj.filename == str(f)

def test_line_generator(tmp_path):
    f = tmp_path / "f.txt"
    f.write_text("x\ny\n")
    obj = FileReader(str(f))
    assert list(obj.line_generator()) == ["x", "y"]

def test_count_lines(tmp_path):
    f = tmp_path / "f.txt"
    f.write_text("a\nb\nc\n")
    assert FileReader.count_lines(str(f)) == 3

def test_from_string(tmp_path):
    file = tmp_path / "g.txt"
    obj = FileReader.from_string("one\ntwo", file)
    assert list(obj.line_generator()) == ["one", "two"]

def test_str_method(tmp_path):
    f = tmp_path / "f.txt"
    f.write_text("hi\nbye\nyo\nsup\n")
    obj = FileReader(str(f))
    assert str(obj) == "hi\nbye\nyo"

def test_add_operator(tmp_path):
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_text("1\n")
    f2.write_text("2\n")
    obj = FileReader(str(f1)) + FileReader(str(f2))
    text = open(obj.filename).read()
    assert "1" in text and "2" in text

def test_concat_files(tmp_path):
    f = tmp_path / "base.txt"
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    f.write_text("b\n")
    a.write_text("a\n")
    b.write_text("c\n")
    obj = FileReader(str(f))
    obj.concat_files(str(a), str(b))
    text = open(obj.filename).read()
    assert "a" in text and "c" in text

def test_uppercase_reader(tmp_path):
    f = tmp_path / "up.txt"
    f.write_text("abc\ndef\n")
    obj = UpperCaseFileReader(str(f))
    assert list(obj.line_generator()) == ["ABC", "DEF"]
    assert str(obj) == "ABC\nDEF\n"

@pytest.mark.xfail
def test_fail():
    assert 1 == 2

def test_decorator_color(capsys):
    @deco("red")
    def say():
        print("Test", end="")
    say()
    out, _ = capsys.readouterr()
    assert "\033[91m" in out
    assert "Test" in out
    assert "\033[0m" in out
