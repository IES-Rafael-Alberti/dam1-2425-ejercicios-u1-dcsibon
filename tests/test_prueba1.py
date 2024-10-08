import pytest

from otros.prueba1 import  es_mayor, introduce_entero


#
# Pruebas unitarias de la función es_mayor()
#

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


#
# Pruebas unitarias de la función introduce_entero()
#

import pytest

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('  10', 10),     # Número positivo válido
        ('-5', -5),     # Número negativo válido
        ('0', 0),       # Número cero
    ]
)
def test_introduce_entero_valid(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert introduce_entero("Introduce un entero: ") == expected


@pytest.mark.parametrize(
    "mock_inputs, error_msg",
    [
        (['abc'], "**ERROR** 'abc' no es un número entero válido!\n"),  # Entrada inválida sin valor válido posterior
        (['123abc'], "**ERROR** '123abc' no es un número entero válido!\n"),  # Entrada con mezcla de caracteres
        (['-123a'], "**ERROR** '-123a' no es un número entero válido!\n"),  # Entrada con número negativo y caracteres inválidos
    ]
)
def test_introduce_entero_invalid_only(mock_inputs, error_msg, monkeypatch, capfd):
    input_iterator = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Usamos pytest.raises para manejar el agotamiento del iterador
    with pytest.raises(StopIteration):
        introduce_entero("Introduce un entero: ")  # Esto seguirá esperando una entrada válida

    # Capturamos el mensaje de salida y verificamos si se imprimió el mensaje de error
    captured = capfd.readouterr()
    assert error_msg in captured.out