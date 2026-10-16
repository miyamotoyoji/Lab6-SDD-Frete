"""Cálculo mínimo de frete conforme specs/checkout_frete.md."""


def calcular_frete(subtotal: float) -> float:
    """REQ-01 e REQ-02: tarifa padrão com isenção por subtotal."""
    return 0.00 if subtotal >= 200.00 else 15.00


def calcular_total(subtotal: float) -> float:
    """REQ-01: total é a soma do subtotal com o frete aplicável."""
    return subtotal + calcular_frete(subtotal)
