import pytest
from src.ej04_def2 import grados_celsius

def test_grados_celsius():
    # Pruebas directas con diferentes valores de Fahrenheit
    assert grados_celsius(32) == 0
    assert grados_celsius(212) == 100
    assert grados_celsius(0) == -17.78
    assert grados_celsius(-40) == -40
    assert grados_celsius(100) == 37.78

@pytest.mark.parametrize(
    "input_fahrenheit, expected",
    [
        (32, 0),
        (212, 100),
        (0, -17.78),
        (-40, -40),
        (100, 37.78),
    ]
)
def test_grados_celsius_params(input_fahrenheit, expected):
    assert grados_celsius(input_fahrenheit) == expected