from Functions.vultr import first_step
import sys

def main(argv):
    for opt in argv:
        if "--help" in opt:
            print('\n')
            print('#' * 45)
            print('--help - Imprime os argumentos na tela')
            print('--print - Imprime resultados na tela')
            print('--save_csv - Salva dados em arquivo csv')
            print('--save_json - Salva dados em arquivo json')
            print('#' * 45)

        elif "--print" in opt:
            rows = first_step()
            for row in rows:
                print(row)
        elif "--save_csv" in opt:
            pass

        elif "--save_json" in opt:
            pass

        else:
            print('\n')
            print('#' * 45)
            print('--help - Imprime os argumentos na tela')
            print('--print - Imprime resultados na tela')
            print('--save_csv - Salva dados em arquivo csv')
            print('--save_json - Salva dados em arquivo json')
            print('#' * 45)


if __name__ == '__main__':
    main(sys.argv[1:])

