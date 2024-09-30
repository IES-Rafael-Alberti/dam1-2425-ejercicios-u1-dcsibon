import pytest
from EjerciciosU1.ej01_def import saludo

def test_saludo():
    assert saludo("Juan") == "Hola, Juan."
    assert saludo(" maria ") == "Hola, Maria."
    assert saludo("MARIA") == "Hola, Maria."
    assert saludo("") == "No has introducido un nombre."
    assert saludo(" ANA ") == "Hola, Ana."

@pytest.mark.parametrize(
    "input_nombre, expected",
    [
        ("Juan", "Hola, Juan."),
        (" maria ", "Hola, Maria."),
        ("MARIA", "Hola, Maria."),
        ("", "No has introducido un nombre."),
        (" ANA ", "Hola, Ana."),
    ]
)
def test_saludo_params(input_nombre, expected):
    assert saludo(input_nombre) == expected