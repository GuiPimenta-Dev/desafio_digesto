import sys
import json, csv
from Functions.vultr import vultr

def choose_output(argv):
    if argv:
        rows = vultr()
        for opt in argv:
            if "--help" in opt:
                show_help()

            elif "--print" in opt:
                for row in rows:
                    print(row)

            elif "--save_csv" in opt:
                with open('csv_output.csv', 'w', newline='') as csv_file:
                    csv_file = csv.writer(csv_file, delimiter=',')
                    csv_file.writerow(["cpu", "memory", "storage", "bandwidth", "price"])

                    for row in rows:
                        csv_file.writerow([row["cpu"],
                                           row["memory"],
                                           row["storage"],
                                           row["bandwidth"],
                                           row["price"]])

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
    choose_output(sys.argv[1:])

