import sqlite3
import pandas as pd

print("--- INICIANDO GERAÇÃO DO RELATORIO ---")

conexao = sqlite3.connect("carros.db")

query_sql = """
SELECT
    comb.nome AS tipo_combustivel,
    COUNT(f.id) AS quantidade_carros,
    ROUND(AVG(f.preco_brl), 2) AS preco_medio_brl
FROM fato_versoes f
JOIN dim_combustiveis comb ON f.combustivel_id = comb.id
GROUP BY comb.nome;
"""
print("Buscando dados...")
df_resultado = pd.read_sql_query(query_sql, conexao)

print("Exportando dados para o Excel...")
df_resultado.to_excel("relatorio_precos_combustivel.xlsx", index=False)

conexao.close()

print("\n--- PROCESSO CONCLUIDO ---")
print("O arquivo 'relatorio_precos_combustivel.xlsx' foi gerado!")