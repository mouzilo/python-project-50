import pytest
import yaml
from gendiff.parser.parse_files import parse_files

@pytest.fixture
def file1():
    return 'tests/test1.json'

@pytest.fixture
def file2():
    return 'tests/test2.yml'

def test_parse(file1, file2):
    expected_result = {
        "- key4": "value4",
        "+ key2": "value2",
        "key1": "value1",
        "key3": "value3"
    }

    result = parse_files(file1, file2)
    result_dict = yaml.safe_load(result)

    assert result_dict == expected_result
