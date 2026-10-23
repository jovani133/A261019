### Importação das bibliotecas, 
# instalação no terminal, 
# ambiente virual venv, 
# criação e 
# vinculação com GitHub ###

import pandas as pd
import os

PASTA = os.path.dirname(os.path.abspath(__file__))
CAMINHO_CSV_ORIGINAL = os.path.join(PASTA, "Base_Varejo_Novo.csv")  
CAMINHO_CSV = os.path.join(PASTA, "Base_Varejo.csv")

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV_ORIGINAL,sep=';')
    return df

if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())