import logging

from playwright.sync_api import sync_playwright

from leitor_excel import ler_produtos
from validacao import validar_produto
from automacao_web import cadastrar_produto
from relatorio import gerar_relatorio

logging.basicConfig(
    filename="logs/automacao.log",
    level=logging.INFO,
    encoding="utf-8",
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)

produtos = ler_produtos("dados/produtos.xlsx")
#print(produtos)

resultados = []

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)

    pagina = navegador.new_page()

    pagina.goto("http://localhost:5000")

    for indice, produto in produtos.iterrows():
        codigo = str(produto["codigo"])
        nome = str(produto["nome"])

        try:
            preco = float(produto["preco"])
            quantidade = int(produto["quantidade"])

            valido, mensagem = validar_produto(preco, quantidade)

            if not valido:
                print(f"Produto {nome}: {mensagem}")

                logging.warning(f"Produto {nome}: {mensagem}")

                resultados.append({
                    "codigo": codigo,
                    "nome": nome,
                    "status": "Erro",
                    "mensagem": "Preço inválido"
                })

                continue

            cadastrar_produto(pagina, codigo, nome, preco, quantidade)    

            print(f"Produto {nome}: cadastrado com sucesso.")

            logging.info(f"Produto {nome}: cadastrado com sucesso.")

            resultados.append({
                "codigo": codigo,
                "nome": nome,
                "status": "Sucesso",
                "mensagem": "Produto cadastrado"
            })

        except Exception as erro:
            print(f"{nome}: erro no cadastro.")

            logging.error(f"Erro ao cadastrar {nome}: {erro}")

            pagina.screenshot(path=f"screenshots/erro_{codigo}.png")

            resultados.append({
                "codigo": codigo,
                "nome": nome,
                "status": "Erro",
                "mensagem": str(erro)
            })

    input("Pressione ENTER para fechar...")

    navegador.close()

gerar_relatorio(resultados, "resultados/resultado.xlsx")

print("Relatório gerado com sucesso.")