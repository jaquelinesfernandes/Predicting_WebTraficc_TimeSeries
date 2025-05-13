# %%
# Imports
import pandas as pd
import numpy as np

# %%
# Parâmetros para gerar dados de exemplo
np.random.seed(42)
data_size = 1000

# %%
# Cria um DataFrame de exemplo com dados de tráfego de web site de e-commerce
df = pd.DataFrame({
    'dia_semana': np.random.choice(range(7), size = data_size),              # Dia da semana (0=domingo, 6=sábado)
    'eh_feriado': np.random.choice([0, 1], size = data_size),                # Feriado ou não
    'campanha_marketing_ativa': np.random.choice([0, 1], size = data_size),  # Campanha de marketing ativa ou não
    'taxa_media_conversao': np.random.uniform(0, 50, size = data_size),      # Taxa média de conversão em %
    'num_visitas_dia_anterior': np.random.poisson(100, size = data_size),    # Visitas no dia anterior
    'num_visitas': np.random.poisson(120, size = data_size)                  # Número de visitas (variável dependente)
})

# Salvar o dataset para análise
df.to_csv('./dataset/dataset_webtraffic.csv', index = False)
# %%

