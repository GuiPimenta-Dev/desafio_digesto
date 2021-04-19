"""
    Função responsável por printar os resultados na tela
    independente do sistema
"""


def print_results_on_screen(system, rows):
    print(f'\n Resultado da extração no sistema {system}: \n')
    for row in rows:
        print(row)

