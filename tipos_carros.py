import sqlite3
import pandas as pd

print("--- CARREGANDO DADOS... ---")
#carregando todas as tabelas
df_cambios = pd.read_csv("dim_cambios.csv")
df_combustiveis = pd.read_csv("dim_combustiveis.csv")
df_marcas = pd.read_csv("dim_marcas.csv")
df_modelos = pd.read_csv("dim_modelos.csv")
df_paises = pd.read_csv("dim_paises.csv")
df_segmentos = pd.read_csv("dim_segmentos.csv")

#carregando a tabela principal
df_versoes = pd.read_csv("fato_versoes.csv")
print(f"Concluido: {len(df_versoes)} versões carregadas.")

print("Criando coluna para saber o consumo médio...")

df_versoes["consumo_medio_kml"] = (df_versoes["consumo_cidade_kml"] + df_versoes["consumo_estrada_kml"])/2

#arredondando para apenas duas casas decimais
df_versoes["consumo_medio_kml"] = df_versoes["consumo_medio_kml"].round(1)

print("A criação foi feita com sucesso!")

print(df_versoes[["nome_versao", "consumo_cidade_kml", "consumo_estrada_kml", "consumo_medio_kml"]].head())

print("\n--- INSERINDO DADOS (SQLITE) ---")

conexao = sqlite3.connect("carros.db")

df_cambios.to_sql("dim_cambios", conexao, if_exists="replace", index=False)
df_combustiveis.to_sql("dim_combustiveis", conexao, if_exists="replace", index=False)
df_marcas.to_sql("dim_marcas", conexao, if_exists="replace", index=False)
df_modelos.to_sql("dim_modelos", conexao, if_exists="replace", index=False)
df_paises.to_sql("dim_paises", conexao, if_exists="replace", index=False)
df_segmentos.to_sql("dim_segmentos", conexao, if_exists="replace", index=False)
df_versoes.to_sql("fato_versoes", conexao, if_exists="replace", index=False)

conexao.close()

print("--- PIPELINE DE ETL FOI EXECUTADO COM SUCESSO ---")
print("O arquivo 'carros.db' foi criado com todas as tabelas.")