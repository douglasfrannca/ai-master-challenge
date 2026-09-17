# Screenshots

| Arquivo | O que mostra | Tirado por |
|---|---|---|
| `g1-chatgpt-00a-brief-colado.png` | Baseline: o brief do challenge colado sem nenhum contexto no ChatGPT | Douglas |
| `g1-chatgpt-00b-inicio-resposta.png` | Início da resposta: frase de abertura e pesquisa em 5 sites | Douglas |
| `g1-chatgpt-01.png` a `g1-chatgpt-06.png` | Baseline: resposta do ChatGPT ao brief colado sem contexto ("Pensou por 1m 48s"). Texto literal em `../baseline/chatgpt.md` | Douglas |
| `g1-deepseek-01` a `09` | Baseline DeepSeek, na ordem da conversa: README enviado como arquivo, raciocínio interno exposto, pedido do dataset, upload do CSV com o aviso **"Length limit reached. DeepSeek can only read the first 37%"** e o diagnóstico errado de **7.109 linhas** | Douglas |
| `g1-grok-01` a `06` | Baseline Grok: brief colado, resposta após 6 min, tabela "Nano 51,7%" (artefato engajamento ÷ seguidores) e estratégia P0–P2. **Barra lateral recortada** para não expor nome e foto da conta pessoal | Douglas (recorte: Claude Code) |
| `g1-claude-01` a `16` | Baseline Claude.ai (Opus 5): brief colado, pedido do CSV, execução, resposta final, o artifact "Painel de Decisão" e as 10 páginas do .docx (a p. 3 traz o período errado 01/01–09/09/2024). **Barra lateral recortada** | Douglas (recorte: Claude Code) |
| `g7-github-historico-commits.png` | Histórico da branch `submission/douglas-franca`: um commit por gate, coassinados por Douglas e Claude | Claude Code (Playwright) |
| `g7-github-pasta-submissao.png` | Estrutura da pasta da submissão no fork | Claude Code (Playwright) |

Prints do app: `../../outputs/figures/app/`.
