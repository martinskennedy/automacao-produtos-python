def validar_produto(preco, quantidade):

    if preco <= 0:
        return False, "Preço inválido"

    if quantidade < 0:
        return False, "Quantidade inválida"

    return True, ""