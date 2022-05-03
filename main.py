import matplotlib.pyplot as plt  # pip install matplotlib


def read_file(file: str):
    try:
        f = open(file).read().strip().split('\n')
    except IOError as error:
        print(f"Критическая ошибка чтения файла {file}!\nПодробное описание ошибки: {error}."
              f"\nПожайлуйста, укажите верные файлы!")
        exit(1)
    res = []
    for i in range(len(f)):
        try:
            f[i] = list(map(int, f[i].split(',')))
            if len(f[i]) != 3:
                exit(0)
            res.append(f[i])
        except Exception as error:
            print(f"В файле {file} содержится неккоректная строка под номером {i + 1}!\nПодробное описание ошибки: {error}")
    return res


def build_solo_graphic(data, coordinate):
    if coordinate == 'X':
        index = 0
    elif coordinate == 'Y':
        index = 1
    else:
        index = 2

    figure = plt.figure()
    s4 = figure.add_subplot()

    arr_x, arr_y = [], []
    i = 0
    for d in data['data']:
        i += 0.1
        arr_x.append(i)
        arr_y.append(d[index])
    s4.plot(arr_x, arr_y)
    plt.title(f"График функции {data['filename']} координаты {coordinate} по времени.")
    plt.show()


def main():
    case_filenames = ['/Users/olegpash/PycharmProjects/tema/tests/14,45,56-Даниил, левая-workPC.txt',
                      '/Users/olegpash/PycharmProjects/tema/tests/14,48,33-Даниил, левая-Sport.txt']
    cases_data = []
    for filename in case_filenames:
        cases_data.append({'data': read_file(filename), 'filename': filename})
    for case in cases_data:
        build_solo_graphic(case, 'X')
        build_solo_graphic(case, 'Y')
        build_solo_graphic(case, 'Z')


if __name__ == "__main__":
    main()

