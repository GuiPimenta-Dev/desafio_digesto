import sys

from constants.items import OutputsEnum, SystemsEnum

from outputs.csv_output import save_digital_ocean_results_in_csv, save_vultr_results_in_csv
from outputs.screen_output import print_results_on_screen
from outputs.json_output import save_results_in_json

from spiders.extractor_digital_ocean import spider_extractor_digital_ocean
from spiders.extractor_vultr import spider_extractor_vultr

"""
    Função Responsável por decidir a saída das spiders
    de acordo com os argumentos informados pelo usuário
"""

def main(argv):
    if argv:
        rows_vultr = spider_extractor_vultr()
        rows_digital_ocean = spider_extractor_digital_ocean()

        for opt in argv:
            if "--help" in opt:
                show_help()

            elif "--print" in opt:
                print_results_on_screen(SystemsEnum.VULTR, rows_vultr)
                print_results_on_screen(SystemsEnum.DIGITAL_OCEAN, rows_digital_ocean)

            elif "--save_csv" in opt:
                save_vultr_results_in_csv(rows_vultr)
                save_digital_ocean_results_in_csv(rows_digital_ocean)

            elif "--save_json" in opt:
                save_results_in_json(OutputsEnum.VULTR_JSON_FILE, rows_vultr)
                save_results_in_json(OutputsEnum.DIGITAL_OCEAN_JSON_FILE, rows_digital_ocean)

            else:
                show_help()
    else:
        show_help()


def show_help():
    print('\n')
    print('#' * 45)
    print('--help - Instruções')
    print('--print - Imprime resultados na tela')
    print('--save_csv - Salva dados em arquivo digital_ocean')
    print('--save_json - Salva dados em arquivo json')
    print('#' * 45)


if __name__ == '__main__':
    main(sys.argv[1:])
