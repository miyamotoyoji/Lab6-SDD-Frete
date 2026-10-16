# Laboratório 6 — SDD e revisão multidimensional

Exercícios **6.1, 6.2 e 6.3**: checkout com frete padrão de R$15 e gratuidade por subtotal. Versão final: **frete grátis a partir de R$250**.

## Entregas

Conforme os slides, envie o **mesmo link deste repositório nas três atividades**:

https://github.com/miyamotoyoji/Lab6-SDD-Frete

| Exercício | Relatório | Versão identificada |
|---|---|---|
| 6.1 — execução dirigida por agente | [TDD e requisitos](docs/6.1_Execucao.md) | [exercicio-6.1](https://github.com/miyamotoyoji/Lab6-SDD-Frete/tree/exercicio-6.1) |
| 6.2 — auditoria e revisão | [Auditoria](audit_report.md) | [exercicio-6.2](https://github.com/miyamotoyoji/Lab6-SDD-Frete/tree/exercicio-6.2) |
| 6.3 — spec viva e alteração sincronizada | [Evolução da regra](docs/6.3_Spec_Viva.md) | [exercicio-6.3](https://github.com/miyamotoyoji/Lab6-SDD-Frete/tree/exercicio-6.3) |

## Executar

Com Python **3.14+**, na raiz do projeto:

```console
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements-dev.txt
.venv\Scripts\python -m pytest -q
```

No PyCharm, abra esta pasta, selecione um interpretador Python 3.14+ com pytest e execute `tests/test_frete.py` como pytest. O pyproject.toml configura a descoberta de src.

## Estrutura

- `constitution.md`: regras de desenvolvimento.
- `specs/checkout_frete.md`: fonte de verdade em EARS.
- `tasks/TASK-01.md`: tarefa inicial delimitada.
- `src/frete.py`: implementação mínima.
- `tests/test_frete.py`: casos normais e fronteiras.
- `audit_report.md`: matriz e revisão multidimensional.
- `evidencias/`: saídas reais das execuções e experimento de drift.

## Ferramentas e transparência

Trabalho realizado com assistência de **Codex**, Python 3.14, pytest e Git. O roteiro metodológico SDD/TDD foi executado; não se afirma uso de Google Antigravity, de conexão MCP com PyCharm ou de GitHub Desktop. O experimento de cupom é uma injeção controlada para auditoria, documentada como tal. Esses pontos diferem da ferramenta sugerida nos slides e podem exigir validação do professor. Não há alegação de revisão humana independente.

O exemplo regional dos slides não foi incorporado por conflitar com a tarefa explícita: as decisões de escopo estão na especificação. Este projeto é de frete e é separado do laboratório 7 bancário.
