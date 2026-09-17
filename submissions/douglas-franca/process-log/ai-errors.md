# Onde a IA errou

Registrado no momento em que o erro aconteceu.

| Data | Gate | O que a IA fez | Como detectei | Correção | Commit |
|---|---|---|---|---|---|
| 2026-09-16 | G1 | Claude Code escreveu no script o veredito "nenhuma célula passa de ~1,1x" **antes** de rodar a conta | A execução mostrou teto de 1,02x | Veredito passou a ser gerado a partir do valor calculado (`f"teto real {max:.2f}x"`) | g1 |
| 2026-09-16 | G1 | Claude Code deixou vereditos "conferir" em afirmações que o próprio output já confirmava | Leitura da tabela de saída | Vereditos corrigidos para VERDADEIRO com os valores observados | g1 |
| 2026-09-16 | G1 | Baseline: Gemini inventou o dataset e os achados; Grok vendeu um artefato 1/x como insight; Claude errou o período; DeepSeek leu 37% do CSV | Checagem numérica `src/audit/verify_baseline_claims.py` | Documentado em `process-log/baseline/README.md` e na rubrica D3 | g1 |
| 2026-09-16 | G2 | Claude Code reportou "52.214 × 29 colunas" contando duas colunas que ele mesmo criou | O número não batia com as 27 colunas vistas no G1 | Contagem feita antes das colunas derivadas | g2 |
| 2026-09-16 | G2 | Claude Code afirmou que "dados reais têm var/média na casa de milhares", sem fonte | Revisão do texto antes do commit | Reescrito como "sobredispersão (var/média >> 1)", afirmação qualitativa e sustentável | g2 |
| 2026-09-16 | G2 | Claude Code resumiu "8 falhas em 7 etapas" sem que a contagem de etapas fechasse | Revisão do texto antes do commit | Removido o número de etapas | g2 |
| 2026-09-16 | G2 | Claude Code rotulou como [evidência] que o patrocínio "não é aleatorizado" | Os próprios números do G1 mostram balanceamento perfeito (seguidores 499.924 vs 499.855; Cramér's V 0,013) | Linha reescrita: a evidência é a ausência do campo de critério; o balanceamento é mais um sinal de sorteio | g2 |
| 2026-09-16 | G3 | Claude Code contou "154 comparações" no resumo, esquecendo audiência, plataformas e hashtags | Soma das famílias na conferência do relatório contra `inf-summary.json` | Corrigido para 335 | g3 |
| 2026-09-16 | G3 | Primeira versão da análise de hashtags só testava pares; nenhum par tem n ≥ 100 (máx. 5), então a família saía vazia | Leitura do resumo (`pares_com_n_min: 0`) | Adicionada a análise por hashtag individual (16 com n ≥ 100) | g3 |
| 2026-09-16 | G3 | Gráfico com faixas de seguidores em ordem alfabética e rótulo sobreposto à linha do zero | Inspeção visual dos PNGs | Ordem fixa das faixas + fundo no rótulo | g3 |
| 2026-09-16 | G5 | Claude Code citou na estratégia amplitudes de plataforma (0,008) e formato (0,012) calculadas com as 5 redes, embora a estratégia seja para os 3 canais | Conferência contra `inf-factors.csv` antes do commit | Substituídas pelas amplitudes no escopo: 0,007 e 0,014 p.p. | g5 |
| 2026-09-16 | G5 | Primeira versão da regra de ciclo classificava um efeito negativo com margem larga como "Replicar: promissor" | Revisão da lógica ao escrever os testes | Nova regra: se o IC não alcança +1 p.p., Parar; teste `test_wide_negative_interval_is_not_promising` | g5 |
| 2026-09-17 | G6 | Regras do health check devolviam `numpy.bool_`; o teste por identidade (`is False`) não encontrava H10 e H11 | Teste `test_challenge_like_file_is_rejected_for_the_right_reasons` falhou | `Check.__post_init__` converte para `bool` | g6 |
| 2026-09-17 | G6 | A exceção `!app/assets/*.parquet` do `.gitignore` não vale para o `stage.sh` (`git ls-files -X`); a base do app ficaria fora do commit e o app publicado abriria vazio | Conferência da lista de arquivos no stage | Removida a regra genérica `*.parquet`; dados brutos seguem bloqueados por `data/` | g6 |
| 2026-09-17 | G6 | Motivo de "Escalar" dizia "retorno acima do break-even" num teste sem custo | Inspeção visual da aba 4 | Mensagem condicional + teste `test_scale_reason_does_not_mention_money_when_test_has_no_cost` | g6 |
| 2026-09-17 | G6 | Rótulo da faixa irrelevante sobre o primeiro ponto do gráfico; placeholder do select em inglês; tabela de regras cortando a última linha | Inspeção visual no navegador e nos prints | Anotação acima do gráfico; `placeholder="Selecione"`; altura da tabela calculada | g6 |
| 2026-09-17 | G7 | Claude Code repetiu "21 afirmações conferidas" (G1, também na mensagem do commit f94b3ec) e "17 entradas" neste log | Conferência dos números do README contra os arquivos | A tabela tem 19 afirmações das IAs + 4 checagens próprias; README corrigido; o commit antigo fica como está | g7 |
