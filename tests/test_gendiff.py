import pytest
from gendiff.parser.parse_files import parse_files


@pytest.fixture
def file1():
    return 'tests/test1.json'


@pytest.fixture
def file2():
    return 'tests/test2.yml'


@pytest.fixture
def expected_result():
    with open('tests/expected_result.txt') as file:
        return file.read()


def test_parse(file1, file2, expected_result):
    result = parse_files(file1, file2)
    assert result == expected_result
