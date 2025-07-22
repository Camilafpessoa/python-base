#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
salas = {
    "Sala 1": ["Camila", "Braian", "Lila", "Boo", "Gamba", "Gabriel"],
    "Sala 2": ["Bia", "Celda", "Savio", "Paula", "Akira"],
}

atividades = {
    "Inglês": ["Camila", "Braian", "Gabriel", "Savio", "Celda"],
    "Música": ["Camila", "Savio", "Paula"],
    "Dança": ["Lila", "Gamba", "Gabriel", "Celda"]
}

# Listar alunos em cada atividade por sala

for nome_atividade, alunos_atividade in atividades.items():

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    for nome_sala, alunos_sala in salas.items():
        alunos_na_atividade = set (alunos_sala) & set(alunos_atividade)
        print(f"{nome_sala}: {alunos_na_atividade}")

        print()
        print("#" * 40)
