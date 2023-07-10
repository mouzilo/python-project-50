import json
from gendiff.scripts.gendiff_json import gendiff_json
import pytest

@pytest.fixture
def file1_path():
    return 'tests/test1.json'

@pytest.fixture
def file2_path():
    return 'tests/test2.json'

def test_gendiff_json(file1_path, file2_path):
    expected_result = {
        "- key4": "value4",
        "+ key2": "value2",
        "key1": "value1",
        "key3": "value3"
    }

    result = gendiff_json(file1_path, file2_path)
    result_dict = json.loads(result)

    assert result_dict == expected_result


