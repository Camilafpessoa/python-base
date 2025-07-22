#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

produto_nome = "Blusa"
produto_cor1 = "azul"
produto_cor2 = "preto"
produto_preco = 45.12
produto_dimensao_altura = 12.1
produto_dimensao_largura = 0.8
produto_em_estoque = True
produto_codigo = 34334
produto_codebar = None


compra = ("Braian", produto_nome, 3)

print(
    f"O cliente {compra[0]} comprou {compra[1]}"
    f" e pagou o total de {compra[2] * produto_preco}"
)
