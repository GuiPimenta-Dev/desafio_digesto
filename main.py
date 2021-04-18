import sys, json, csv
from Functions.vultr import vultr


def main(argv):
    if argv:
        rows = vultr()
        for opt in argv:
            if "--help" in opt:
                show_help()

            elif "--print" in opt:
                for row in rows:
                    print(row)

            elif "--save_csv" in opt:
                pass

            elif "--save_json" in opt:
                with open('json_output.json', 'w') as json_file:
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
