import pandas as pd

def gerar_relatorio(resultados, caminho):

    df_resultados = pd.DataFrame(resultados)

    df_resultados.to_excel(caminho, index=False)