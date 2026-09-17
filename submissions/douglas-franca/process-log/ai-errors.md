# Onde a IA errou

Registrado no momento em que o erro aconteceu.

| Data | Gate | O que a IA fez | Como detectei | Correção | Commit |
|---|---|---|---|---|---|
| 2026-09-16 | G1 | Claude Code escreveu no script o veredito "nenhuma célula passa de ~1,1x" **antes** de rodar a conta | A execução mostrou teto de 1,02x | Veredito passou a ser gerado a partir do valor calculado (`f"teto real {max:.2f}x"`) | g1 |
| 2026-09-16 | G1 | Claude Code deixou vereditos "conferir" em afirmações que o próprio output já confirmava | Leitura da tabela de saída | Vereditos corrigidos para VERDADEIRO com os valores observados | g1 |
| 2026-09-16 | G1 | Baseline: Gemini inventou o dataset e os achados; Grok vendeu um artefato 1/x como insight; Claude errou o período; DeepSeek leu 37% do CSV | Checagem numérica `src/audit/verify_baseline_claims.py` | Documentado em `process-log/baseline/README.md` e na rubrica D3 | g1 |
