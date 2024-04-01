import pytest
import yaml
from dataDriver.yamlDriver.func.operation_yaml import my_add


def get_data():
    with open('../datas/data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


class TestWithYAML:
    @pytest.mark.parametrize('x,y,expected', get_data())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
