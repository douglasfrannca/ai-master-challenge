# G8: crítica adversarial, síntese

A entrega passou por crítica **antes** do PR, com dois tipos de revisor:

| Rodada | Revisor | Como foi feita | Veredito |
|---|---|---|---|
| 1 | Agente `g4-reviewer` (Claude Code), calibrado nos reviews públicos do repositório | Checkout limpo da branch, `uv sync`, rodou os 4 scripts e os testes, comparou os CSVs regerados com os versionados, conferiu mais de 30 números contra os dados | **9/10, sem bloqueadores** · [`../../reports/review-verdict-round1.md`](../../reports/review-verdict-round1.md) |
| 2 | ChatGPT e Gemini, operados pelo Douglas | Submissão colada com o pedido de apontar as fraquezas | _pendente_ |

## Rodada 1: o que foi apontado e o que fiz

| # | Apontamento | Decisão | Status | Verificação |
|---|---|---|---|---|
| 1 | Process log incompleto: `chat-exports/` e `critique/` vazias; linha do tempo por gate só com o G0 | Preencher | Linha do tempo G0–G8 e esta síntese: **feito**. Transcript da sessão: _pendente_ | `process-log/README.md` |
| 2 | `app/assets/posts.parquet` tinha as 52.214 linhas do dataset (o PR #96 foi reprovado em higiene por isso) | **Douglas:** "Baixar ao abrir" | **Feito**: o app carrega os dados por `src/app_data.py` (local ou Kaggle na 1ª abertura, 4,8 s a frio); conteúdo idêntico ao anterior | `git ls-files \| grep parquet` → vazio; commit `c976a8e` |
| 3 | Único número sem tabela: "≤ 0,012 p.p." (real: 0,0126) | Corrigir e gerar a tabela | **Feito** | `outputs/tables/dq-segment-amplitude.csv`; commit `8cd775c` |
| 4 | Data do PR em branco no README | Preencher no dia do PR | _no G9_ | `README.md` |
| 5 | `curl` sem cookie entra em loop de redirecionamento no domínio `streamlit.app` | Documentar; é o login do próprio Streamlit Cloud | `/healthz` responde `200 {"status":"ok"}` com cookie; o app abre no navegador | `curl -c ck -b ck -L https://decision-social-doug.streamlit.app/healthz` |

### O risco que não se resolve editando arquivo
> "A silhueta é a do #91; as 8 diferenças vivem dentro das camadas."

O revisor mostrou que, por fora, a entrega se parece com o PR #91 (mesmo arquivo, mesma conclusão, mesmo tipo de app), e que o resumo executivo abria justamente pelo achado estatístico, onde as duas empatam. **Decisão do Douglas:** o README passa a abrir pelo processo; a estatística vira o motivo, não a manchete.

## Rodada 2: ChatGPT e Gemini
_Pendente. Quando chegar: resposta literal em `chatgpt.md` e `gemini.md` nesta pasta, e uma linha por apontamento na tabela acima._
