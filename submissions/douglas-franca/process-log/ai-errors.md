# Onde a IA errou

Registrado no momento em que o erro aconteceu.

| Data | Gate | O que a IA fez | Como detectei | Correção | Commit |
|---|---|---|---|---|---|
| 2026-09-16 | G1 | Claude Code escreveu no script o veredito "nenhuma célula passa de ~1,1x" **antes** de rodar a conta | A execução mostrou teto de 1,02x | Veredito passou a ser gerado a partir do valor calculado (`f"teto real {max:.2f}x"`) | g1 |
| 2026-09-16 | G1 | Claude Code deixou vereditos "conferir" em afirmações que o próprio output já confirmava | Leitura da tabela de saída | Vereditos corrigidos para VERDADEIRO com os valores observados | g1 |
| 2026-09-16 | G2 | Claude Code reportou "52.214 × 29 colunas" contando duas colunas que ele mesmo criou | O número não batia com as 27 colunas vistas no G1 | Contagem feita antes das colunas derivadas | g2 |
| 2026-09-16 | G2 | Claude Code afirmou que "dados reais têm var/média na casa de milhares", sem fonte | Revisão do texto antes do commit | Reescrito como "sobredispersão (var/média >> 1)", afirmação qualitativa e sustentável | g2 |
| 2026-09-16 | G2 | Claude Code resumiu "8 falhas em 7 etapas" sem que a contagem de etapas fechasse | Revisão do texto antes do commit | Removido o número de etapas | g2 |
| 2026-09-16 | G2 | Claude Code rotulou como [evidência] que o patrocínio "não é aleatorizado" | Os próprios números do G1 mostram balanceamento perfeito (seguidores 499.924 vs 499.855; Cramér's V 0,013) | Linha reescrita: a evidência é a ausência do campo de critério; o balanceamento é mais um sinal de sorteio | g2 |
| 2026-09-16 | G3 | Claude Code contou "154 comparações" no resumo, esquecendo audiência, plataformas e hashtags | Soma das famílias na conferência do relatório contra `inf-summary.json` | Corrigido para 335 | g3 |
| 2026-09-16 | G3 | Primeira versão da análise de hashtags só testava pares; nenhum par tem n ≥ 100 (máx. 5), então a família saía vazia | Leitura do resumo (`pares_com_n_min: 0`) | Adicionada a análise por hashtag individual (16 com n ≥ 100) | g3 |
| 2026-09-16 | G3 | Gráfico com faixas de seguidores em ordem alfabética e rótulo sobreposto à linha do zero | Inspeção visual dos PNGs | Ordem fixa das faixas + fundo no rótulo | g3 |
| 2026-09-16 | G1 | Baseline: Gemini inventou o dataset e os achados; Grok vendeu um artefato 1/x como insight; Claude errou o período; DeepSeek leu 37% do CSV | Checagem numérica `src/audit/verify_baseline_claims.py` | Documentado em `process-log/baseline/README.md` e na rubrica D3 | g1 |
