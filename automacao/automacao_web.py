def cadastrar_produto(pagina, codigo, nome, preco, quantidade):

    pagina.locator("#codigo").fill(codigo)

    pagina.locator("#nome").fill(nome)

    pagina.locator("#preco").fill(str(preco))

    pagina.locator("#quantidade").fill(str(quantidade))

    pagina.locator("#btn-salvar").click()