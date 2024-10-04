import pytest

from otros.prueba1 import  es_mayor


def test_es_mayor():
    assert es_mayor(1, 1) == 0
    assert es_mayor(0, 0) == 0
    assert es_mayor(-99, -100) == -99
    assert es_mayor(23, 6) == 23
    assert es_mayor(11, -11) == 11


@pytest.mark.parametrize(
"input_n1, input_n2, expected",
[
    (1, 1, 0),
    (0, 0, 0),
    (-99, -100, -99),
    (23, 6, 23),
    (11, -11, 11)
]
)
def test_es_mayor_params(input_n1, input_n2, expected):
    assert es_mayor(input_n1, input_n2) == expected