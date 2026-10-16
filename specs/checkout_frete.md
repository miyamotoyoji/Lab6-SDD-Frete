# Checkout: cálculo de frete — versão 1

## Requisitos EARS

- **REQ-01 (ubíquo):** O sistema deve calcular o total do pedido somando o frete padrão de R$15,00 ao subtotal do carrinho, respeitando a isenção prevista em REQ-02.
- **REQ-02 (condicional):** Se o subtotal do carrinho for maior ou igual a R$200,00, então o sistema deve aplicar frete grátis (R$0,00).

## Contrato e escopo

Entradas: subtotal numérico não negativo, finito, em reais, com até duas casas decimais. O chamador é responsável por fornecer valores dentro desse domínio; validações de entrada não fazem parte desta tarefa.

`calcular_frete(subtotal)` devolve 15.00 ou 0.00; `calcular_total(subtotal)` devolve subtotal + frete. O carrinho de valor zero pertence ao domínio e tem frete padrão. Testes usam comparação aproximada para números decimais em ponto flutuante.

Sem cupons, regiões, interface, banco de dados ou rede. Os trechos ilustrativos dos slides com tarifa de R$20, regiões e outros identificadores não são adotados: conflitam com REQ-01 e extrapolam a tarefa delimitada. Prevalecem as regras explícitas do exercício 1.
