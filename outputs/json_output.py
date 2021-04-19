import json

"""
    Função responsável por salvar os resultados em json
    independente do sistema
"""


def save_results_in_json(file, rows):
    with open(file, 'w') as json_file:
        json.dump(rows, json_file)
