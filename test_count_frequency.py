import pytest
from read_file import read_file
from count_frequency import count_frequency


def test_read_file_valid():
    assert read_file("input_directory/input.txt") == "which is better python 2 or python 3"


def test_file_name_invalid():
    with pytest.raises(FileNotFoundError):
        read_file("input_directory/sfssfs")


def test_directory():
    with pytest.raises(PermissionError):
        read_file("input_directory")


def test_frequency_valid():
    assert count_frequency("which is better python 2 or python 3") == [('2', 1), ('3', 1), ('better', 1), ('is', 1), ('or', 1), ('python', 2), ('which', 1)]


def test_frequency_invalid():
    with pytest.raises(TypeError):
        count_frequency(7)
    with pytest.raises(TypeError):
        count_frequency([('2', 1), ('3', 1), ('better', 1)])
    with pytest.raises(TypeError):
        count_frequency({1, 2, 3})
    with pytest.raises(TypeError):
        count_frequency({'2': 1, '3': 1, 'better': 1})
