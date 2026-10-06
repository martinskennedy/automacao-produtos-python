import pandas as pd

def ler_produtos(caminho):
    produtos = pd.read_excel(caminho)

    return produtos