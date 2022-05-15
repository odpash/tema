import matplotlib.pyplot as plt  # pip install matplotlib
import math


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
                continue
            res.append(f[i])
        except Exception as error:
            print(f"В файле {file} содержится неккоректная строка под номером {i + 1}!\nПодробное описание ошибки: {error}")
    return res


def to_write(filename, value, mode='a'):
    with open(filename, mode, encoding='UTF-8') as f:
        if mode == 'w':
            f.close()
            return
        f.write(str(value))
        f.write('\n')
    f.close()


def build_triple_graphic(data):
    line_x, line_y, line_z = [], [], []
    indx = 0
    for d in data['data']:
        indx += 0.1
        line_x.append((d[0] - data['data'][0][0]) / indx)
        line_y.append((d[1] - data['data'][0][1]) / indx)
        line_z.append((d[2] - data['data'][0][2]) / indx)
    figure = plt.figure()
    s4 = figure.add_subplot(projection='3d')
    s4.plot(line_x, line_y, line_z)
    plt.title(f"Акселерометр")
    plt.show()


def build_solo_graphic(data, coordinate):
    if coordinate == 'X':
        index = 0
    elif coordinate == 'Y':
        index = 1
    else:
        index = 2
    to_write(data['filename'].replace('.txt', '-x.txt'), '', 'w')
    to_write(data['filename'].replace('.txt', '-y.txt'), '', 'w')
    to_write(data['filename'].replace('.txt', '-z.txt'), '', 'w')
    to_write(data['filename'].replace('.txt', '-xyz.txt'), '', 'w')
    figure = plt.figure()
    s4 = figure.add_subplot()

    arr_x, arr_y = [], []
    x_arr, y_arr, z_arr = [], [], []
    i = 0
    for d in data['data']:
        i += 0.1
        if '.0' in str(i):  # analyze every one second
            to_write(data['filename'].replace('.txt', '-x.txt'), d[0])
            to_write(data['filename'].replace('.txt', '-y.txt'), d[1])
            to_write(data['filename'].replace('.txt', '-z.txt'), d[2])
            to_write(data['filename'].replace('.txt', '-xyz.txt'), math.sqrt(d[0] ** 2 + d[1] ** 2 + d[2] ** 2))
        x_arr.append(d[0])
        y_arr.append(d[1])
        z_arr.append(d[2])
        arr_x.append(i)
        arr_y.append(d[index])
    s4.plot(arr_x, arr_y)
    plt.title(f"{coordinate}, Summary SKO: X-{srqrt_otkl(x_arr)}, Y-{srqrt_otkl(y_arr)}, Z-{srqrt_otkl(z_arr)}")
    plt.show()


def srqrt_otkl(sp):
    res = 0
    for ii in sp:
        res += (ii - (sum(sp) / len(sp))) ** 2
    res /= len(sp)
    return math.sqrt(res)


def simple_read_file(filename: str):
    return open(filename, mode='r', encoding="UTF-8").read().split('\n')[:-1]


def linear_deviation(arr: list, file_to_check: str):
    array_to_check = simple_read_file(file_to_check.replace('.txt', '-xyz.txt'))
    result_arr = []
    for i in range(len(arr) - 1):
        to_write(arr[i]['filename'].replace('.txt', '-ld.txt'), '', 'w')
        array_to_minus = simple_read_file(arr[i]['filename'].replace('.txt', '-xyz.txt'))
        result = 0
        for j in range(len(array_to_check)):
            try:
                to_write(arr[i]['filename'].replace('.txt', '-ld.txt'), float(array_to_check[j]) - float(array_to_minus[j]), 'a')
                result += float(array_to_check[j]) - float(array_to_minus[j])
            except:
                pass
        result_arr.append([result, arr[i]['filename'].replace('.txt', '-ld.txt')])
    print(result_arr)
    result_arr.sort()  # reverse=True
    print(result_arr[0][1])

def main():
    file_to_check = '/Users/olegpash/PycharmProjects/tema/tests/16_52_0-Daniil_levaya-Sit.txt'
    case_filenames = [
        '/Users/olegpash/PycharmProjects/tema/tests/14,45,56-Даниил, левая-workPC.txt',
        '/Users/olegpash/PycharmProjects/tema/tests/14,48,33-Даниил, левая-Sport.txt',
        file_to_check]
    cases_data = []
    for filename in case_filenames:
        cases_data.append({'data': read_file(filename), 'filename': filename})
    for case in cases_data:
        build_triple_graphic(case)
        build_solo_graphic(case, 'X')
        build_solo_graphic(case, 'Y')
        build_solo_graphic(case, 'Z')
    linear_deviation(cases_data, file_to_check)




if __name__ == "__main__":
    main()