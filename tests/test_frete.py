"""Exemplos e fronteiras rastreáveis à especificação EARS."""

import pytest

from frete import calcular_frete, calcular_total


@pytest.mark.parametrize("subtotal", [0, 50, 150, 199.99])
def test_req01_frete_padrao_abaixo_limite(subtotal):
    """REQ-01: tarifa padrão abaixo do limite de isenção."""
    assert calcular_frete(subtotal) == 15.00


@pytest.mark.parametrize("subtotal", [200, 200.01, 250, 300])
def test_req02_frete_gratis_a_partir_limite(subtotal):
    """REQ-02: inclui o próprio limite, não apenas valores acima."""
    assert calcular_frete(subtotal) == 0.00


@pytest.mark.parametrize(
    "subtotal,total", [(0, 15), (150, 165), (199.99, 214.99), (200, 200), (300, 300)]
)
def test_req01_req02_total_do_pedido(subtotal, total):
    """REQ-01 + REQ-02: soma com tarifa padrão ou isenta."""
    assert calcular_total(subtotal) == pytest.approx(total)
