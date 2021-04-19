import sys, json, csv
from spiders.extractor_vultr import spider_extractor_vultr
from constants.extractor_vultr import VultrItemsEnum

"""
    Função Responsável por decidir a saída das spiders
    de acordo com os argumentos informados pelo usuário
"""


def main(argv):
    if argv:
        rows = spider_extractor_vultr()
        for opt in argv:
            if "--help" in opt:
                show_help()

            elif "--print" in opt:

                for row in rows:
                    print(row)

            elif "--save_csv" in opt:
                with open('outputs/csv_output.csv', 'w', newline='') as csv_file:
                    csv_file = csv.writer(csv_file, delimiter=',')

                    csv_file.writerow([
                        VultrItemsEnum.CPU,
                        VultrItemsEnum.MEMORY,
                        VultrItemsEnum.STORAGE,
                        VultrItemsEnum.BANDWIDTH,
                        VultrItemsEnum.PRICE
                    ])

                    for row in rows:
                        csv_file.writerow([
                            row[VultrItemsEnum.CPU],
                            row[VultrItemsEnum.MEMORY],
                            row[VultrItemsEnum.STORAGE],
                            row[VultrItemsEnum.BANDWIDTH],
                            row[VultrItemsEnum.PRICE]
                        ])

            elif "--save_json" in opt:
                with open('outputs/json_output.json', 'w') as json_file:
                    json.dump(rows, json_file)

            else:
                show_help()
    else:
        show_help()


def show_help():
    print('\n')
    print('#' * 45)
    print('--help - Imprime os argumentos na tela')
    print('--print - Imprime resultados na tela')
    print('--save_csv - Salva dados em arquivo csv')
    print('--save_json - Salva dados em arquivo json')
    print('#' * 45)


if __name__ == '__main__':
    main(sys.argv[1:])
