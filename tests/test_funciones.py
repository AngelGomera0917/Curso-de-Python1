
from Python_Basic.Functions09 import (
    sum_two_values_with_return,
    verificar,
    resta,
    recomendacion_planta
)

def test_sum_two_values_with_return():
    assert sum_two_values_with_return(3, 4) == 7
    assert sum_two_values_with_return(-1, 1) == 0
    assert sum_two_values_with_return(0, 0) == 0
    

def test_verificar_positivo():
    assert verificar (8) == 8
    assert verificar (6) == 6
    assert verificar (0) == 0

    
def test_verificar_negativo():
    assert verificar (-5) is None
    assert verificar (-10) is None
    assert verificar (-1) is None
    assert verificar (-100) is None


def test_resta():
    assert resta(8, 3) == 5
    assert resta(0, 0) == 0
    assert resta(-5, -3) == -2
    
def test_recomendacion_planta():
    assert recomendacion_planta("bajo") == "Cactus"
    assert recomendacion_planta("alto") == "Orquídea"
    assert recomendacion_planta("medio") == "Suculenta"
    assert recomendacion_planta("Full") == "No se encontró ninguna planta"

