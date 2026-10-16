# Auditoria de drift e revisão multidimensional — exercício 6.2

## Método e decisão

Comparação da especificação EARS com src/frete.py e tests/test_frete.py. Revisão assistida por Codex, disponível para conferência humana; não se declara uma revisão humana independente.

O experimento da tag `exercicio-6.2-drift` adicionou cupom sem requisito. Os 13 testes originais passaram: cobertura dos requisitos existentes não prova ausência de funcionalidades indevidas. A revisão da API e das linhas de código identificou a extensão. **Decisão: rejeitar e remover parâmetro, condição e cálculo do cupom**, sem criar requisito retroativo para justificar código.

## Matriz de rastreabilidade

| Cláusula EARS | Status após correção | Teste coberto | Implementação |
|---|---|---|---|
| REQ-01: frete padrão R$15 e composição do total | Conforme | tests/test_frete.py:9 e :24 | src/frete.py:4 e :9 |
| REQ-02: gratuidade a partir do limite da spec | Conforme | tests/test_frete.py:15 e :24 | src/frete.py:6 |
| CUPOM: não existe cláusula EARS | DRIFT no candidato; removido da versão corrigida | Sem teste de requisito: regra inexistente | Candidato: src/frete.py:9–14; ausente após correção |

As linhas do candidato pertencem à tag do experimento. As demais referências apontam para o arquivo corrigido. Na etapa 6.2 o limite é R$200; na etapa 6.3 passa a R$250 com atualização conjunta de spec e testes.

## Revisão multidimensional

| Dimensão | Evidência e conclusão |
|---|---|
| Arquitetura | Duas funções puras; sem classe artificial, framework, dependência de execução ou persistência. Respeita a constituição. |
| Segurança | Não coleta dados pessoais, não imprime entradas, não acessa arquivos/rede nem executa comandos. O domínio de entrada é precondição explícita da spec; validação de entradas externas deverá ser especificada antes de uma futura interface pública. |
| Performance | Uma comparação e uma soma: tempo e espaço O(1), sem laços, chamadas externas ou armazenamento. |
| Observabilidade | Nomes, docstrings e IDs EARS permitem rastrear a regra; pytest informa caso e valor divergentes. Nenhum print de depuração ou dado sensível. Telemetria de serviço não se aplica a estas funções puras. |

## Evidências e conclusão

- `evidencias/6.2_experimento.md`: prompt e interpretação indevida.
- `evidencias/6.2_DRIFT_testes.txt`: testes verdes com drift, mostrando o limite da suíte.
- `evidencias/6.2_CORRIGIDO.txt`: nova execução após remoção.
- Tag `exercicio-6.2`: versão corrigida para inspeção.

Não restam comportamentos de cupom na implementação final. A documentação histórica conserva o caso rejeitado apenas como evidência. A verificação de ausência de drift foi por inspeção, sem alegar prova formal ou medição de cobertura de linhas.
