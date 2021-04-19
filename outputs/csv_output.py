from constants.items import ItemsEnum, OutputsEnum
import csv


"""
    Função responsável por salvar os resultados em digital_ocean
    do sistema vultr

"""


def save_vultr_results_in_csv(rows):
    with open(OutputsEnum.VULTR_CSV_FILE, 'w', newline='') as csv_file:
        csv_file = csv.writer(csv_file, delimiter=',')

        csv_file.writerow([
            ItemsEnum.CPU,
            ItemsEnum.MEMORY,
            ItemsEnum.STORAGE,
            ItemsEnum.BANDWIDTH,
            ItemsEnum.PRICE
        ])

        for row in rows:
            csv_file.writerow([
                row[ItemsEnum.CPU],
                row[ItemsEnum.MEMORY],
                row[ItemsEnum.STORAGE],
                row[ItemsEnum.BANDWIDTH],
                row[ItemsEnum.PRICE]
            ])


"""
    Função responsável por salvar os resultados em digital_ocean
    do sistema digital ocean

"""


def save_digital_ocean_results_in_csv(rows):
    with open(OutputsEnum.DIGITAL_OCEAN_CSV_FILE, 'w', newline='') as csv_file:
        csv_file = csv.writer(csv_file, delimiter=',')

        csv_file.writerow([
            ItemsEnum.CPU,
            ItemsEnum.MEMORY,
            ItemsEnum.SSD_DISK,
            ItemsEnum.TRANSFER,
            ItemsEnum.PRICE
        ])

        for row in rows:
            csv_file.writerow([
                row[ItemsEnum.CPU],
                row[ItemsEnum.MEMORY],
                row[ItemsEnum.SSD_DISK],
                row[ItemsEnum.TRANSFER],
                row[ItemsEnum.PRICE]
            ])
