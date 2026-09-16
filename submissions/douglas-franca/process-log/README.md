# Process Log: índice de evidências

Evidências de como a IA foi usada, organizadas por gate. Tudo em texto (Markdown) ou PNG.

| Pasta/arquivo | Conteúdo |
|---|---|
| `decisions.md` | Decisões humanas por gate (fonte da seção "O que eu adicionei") |
| `ai-errors.md` | Onde a IA errou, como foi detectado e como foi corrigido |
| `baseline/` | Respostas literais de IAs ao brief colado sem contexto (G1) |
| `critique/` | Críticas adversariais multi-modelo + síntese (G8) |
| `chat-exports/` | Transcripts das sessões em Markdown |
| `screenshots/` | Prints nomeados `gN-descricao.png` |

## Sessão 0: calibração da barra (2026-09-14 a 2026-09-16)
Antes de construir, estudei o repositório público do challenge: os 122 PRs e os 181 reviews publicados pelo avaliador. O objetivo era entender o critério real de qualidade e o que já tinha sido entregue no Challenge 004, para não repetir o que já existe. Nenhum conteúdo de outras submissões foi copiado.
Transcript: `chat-exports/g0-calibracao-e-plano.md` (a exportar).

## Linha do tempo por gate
| Gate | Data | Commits | Evidências |
|---|---|---|---|
| G0 Setup | 2026-09-16 | `g0: scaffold` | estrutura, agentes, regras de permissão |
