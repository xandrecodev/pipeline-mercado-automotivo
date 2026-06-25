# Pipeline de Dados: Inteligência de Mercado Automotivo

Desenvolvi este projeto para replicar uma necessidade real do mercado: a integração de relatórios brutos que costumam ser exportados de sistemas corporativos como o SAP. O meu objetivo principal foi criar uma solução que eliminasse o trabalho manual de limpeza, tratamento e consolidação dessas informações.

O projeto executa um processo de ETL (Extração, Transformação e Carga) completo. O script lê os arquivos originais, calcula novas métricas de negócio e carrega tudo estruturado em um banco de dados relacional. Por fim, uma rotina automatizada gera um relatório final em Excel pronto para uso.

---

## Como o projeto funciona

O fluxo dos dados foi dividido em três etapas claras:

1. Extração e Tratamento: O arquivo `pipeline_dados.py` lê as tabelas fato e dimensão em CSV utilizando Pandas, aplicando limpezas e calculando o consumo médio dos veículos.
2. Armazenamento: Os dados tratados são carregados de forma estruturada dentro do arquivo `mercado_automotivo.db` (SQLite).
3. Automação: O arquivo `gerar_relatorio.py` executa consultas analíticas diretamente no banco SQL e exporta um arquivo Excel consolidado de forma automática.

---

## Ferramentas utilizadas

- Python: Construção da lógica e automação do processo.
- Pandas: Limpeza, manipulação e transformação dos dados.
- SQLite e SQL: Modelagem relacional, armazenamento e consultas com agregadores.
- Openpyxl: Geração automática das planilhas Excel.

---

## Insights obtidos através do SQL

Ao analisar o banco de dados que estruturei, utilizei consultas com Joins e Group By para extrair alguns pontos estratégicos sobre o negócio:

- Os motores do tipo Flex representam o maior volume de versões disponíveis no mercado atual da base de dados.
- Os veículos Híbridos registram a maior média de preço do ecossistema, destacando a valorização comercial da tecnologia embarcada.

---

## Como rodar o projeto

1. Clone o repositório:
```bash
git clone [https://github.com/xandrecodev/pipeline-mercado-automotivo.git](https://github.com/xandrecodev/pipeline-mercado-automotivo.git)
```

2. Instale as dependências necessárias:
```bash
pip install pandas openpyxl
```

3. Execute o pipeline de ETL para criar e popular o banco de dados:
```bash
python pipeline_dados.py
```

4. Gere o relatório automatizado em Excel:
```bash
python gerar_relatorio.py
```
