import pytest
from src.ej05_def2 import calcula_precio

def test_calcula_precio():
    assert calcula_precio(100, 21) == "El precio final del artículo con IVA (21.00) es 121.00€."
    assert calcula_precio(100, 10) == "El precio final del artículo con IVA (10.00) es 110.00€."
    assert calcula_precio(100, 0) == "El precio final del artículo con IVA (0.00) es 100.00€."
    assert calcula_precio(100, -10) == "El precio final del artículo con IVA (21.00) es 121.00€."

@pytest.mark.parametrize(
    "input_importe, input_iva, expected",
    [
        (100, 21, "El precio final del artículo con IVA (21.00) es 121.00€."),
        (100, 10, "El precio final del artículo con IVA (10.00) es 110.00€."),
        (100, 0, "El precio final del artículo con IVA (0.00) es 100.00€."),
        (100, -10, "El precio final del artículo con IVA (21.00) es 121.00€."),
    ]
)
def test_calcula_precio_params(input_importe, input_iva, expected):
    assert calcula_precio(input_importe, input_iva) == expected