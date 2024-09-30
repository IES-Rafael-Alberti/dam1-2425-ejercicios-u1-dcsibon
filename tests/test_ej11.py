import pytest
from EjerciciosU1.ej11_def import suma_numeros

def test_suma_numeros():
    assert suma_numeros(5) == "La suma de los números del 1 al 5 es 15."
    assert suma_numeros(10) == "La suma de los números del 1 al 10 es 55."
    assert suma_numeros(1) == "La suma de los números del 1 al 1 es 1."
    assert suma_numeros(100) == "La suma de los números del 1 al 100 es 5050."

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (5, "La suma de los números del 1 al 5 es 15."),
        (10, "La suma de los números del 1 al 10 es 55."),
        (1, "La suma de los números del 1 al 1 es 1."),
        (100, "La suma de los números del 1 al 100 es 5050."),
    ]
)
def test_suma_numeros_params(input_num, expected):
    assert suma_numeros(input_num) == expected