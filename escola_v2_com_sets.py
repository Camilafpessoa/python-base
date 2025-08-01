#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
sala1 = ["Camila", "Braian", "Lila", "Boo", "Gamba", "Gabriel"]
sala2 = ["Bia", "Celda", "Savio", "Paula", "Akira"]

aula_ingles = ["Camila", "Braian", "Gabriel", "Savio", "Celda"]
aula_musica = ["Camila", "Savio", "Paula"]
aula_danca = ["Lila", "Gamba", "Gabriel", "Celda"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca)
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)
