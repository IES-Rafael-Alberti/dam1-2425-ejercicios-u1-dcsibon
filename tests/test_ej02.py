import pytest
from EjerciciosU1.ej02_def import calculo_salario

def test_calculo_salario():
    assert calculo_salario(10, 10) == 100
    assert calculo_salario(0, 50) == 0
    assert calculo_salario(40, 15.5) == 620.0
    assert calculo_salario(35, 20) == 700
    assert calculo_salario(25, 0) == 0

@pytest.mark.parametrize(
    "input_horas, input_coste_hora, expected",
    [
        (10, 10, 100),
        (0, 50, 0),
        (40, 15.5, 620.0),
        (35, 20, 700),
        (25, 0, 0),
    ]
)
def test_calculo_salario_params(input_horas, input_coste_hora, expected):
    assert calculo_salario(input_horas, input_coste_hora) == expected