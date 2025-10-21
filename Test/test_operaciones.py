import pytest
import operaciones

def test_sumar():
    assert operaciones.sumar(3, 5) == 8

def test_division_por_cero():
    with pytest.raises(ValueError):
        operaciones.dividir(10, 0)

@pytest.mark.parametrize("a,b,esperado",[
    (2,5,7), #numeros positivos
    (-4, -6, -10), #numeros negativos
    (0,0,0), #ceros
    (-2, 3, 1) #negativo y positivo
])
def test_sumar_varios(a,b,esperado):
    assert operaciones.sumar(a,b) == esperado


def test_restar_con_fixture(numeros):
    a,b = numeros
    assert operaciones.restar(a, b) == 0

def test_sumar_con_fixture(numeros):
    a,b = numeros
    assert operaciones.sumar(a, b) == 10


@pytest.mark.listo
def test_sumar_listo():
    assert operaciones.sumar(10, 15) == 25

def test_estructuta_dicc():
    data = {"nombre":"Juan", "edad":34}

    assert "nombre" in data
    assert "edad" in data
#verificamos que los datos dentro del diccionario sean del tipo correcto
    assert isinstance(data["nombre"], str)
    assert isinstance(data["edad"], int)

def test_estructura_lista():
    items = [{"id":1, "id":2}]
    
    assert all("id" in item for item in items)
