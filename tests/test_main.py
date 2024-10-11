import pytest
from otros.main import suma

def test_suma():
    assert suma(10, 20) == 30
    assert suma(0, 50) == 50
    assert suma(-5, 5) == 0
    assert suma(0, 0) == 0
    assert suma(0, 20) == 20

@pytest.mark.parametrize(
    "input_num1, input_num2, expected",
    [
        (10, 20, 30),
        (0, 50, 50),
        (-5, 5, 0),
        (0, 0, 0),
        (0, 20, 20),
    ]
)
def test_suma_params(input_num1, input_num2, expected):
    assert suma(input_num1, input_num2) == expected