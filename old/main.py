import matplotlib.pyplot as plt
# pip install matplotlib
# or
# pip install -r requirements.txt


def read_file(filename):
    f = open(filename).read().split('\n')
    for i in range(len(f)):
        try:
            f[i] = list(map(int, f[i].split(',')))
        except:
            f.pop(i)

    arr_x, arr_y, arr_z = [], [], []
    for i in f:
        arr_x.append(i[0])
        arr_y.append(i[1])
        arr_z.append(i[2])
    return f, arr_x, arr_y, arr_z


def build_graphic(x, y, z, name):
    fig = plt.figure()
    s4 = fig.add_subplot()#projection='3d') #
    s4.plot(arr_x, arr_y)
    s4.plot(x, y)
    plt.title(name)
    plt.show()


def sport_mode(arr):
    confirmed = 0
    graphic_x = []
    graphic_y = []
    for i in arr:
        if -1000 < i[0] < 2000 and -1000 < i[1] < 2000:
            confirmed += 1
            graphic_x.append(i[0])
            graphic_y.append(i[1])
    return [confirmed, graphic_x, graphic_y, f"sport - {confirmed / len(arr)}"]


def chill_mode(arr):
    confirmed = 0
    graphic_x = []
    graphic_y = []
    for i in arr:
        if -500 < i[0] < 1000 and -800 < i[1] < 1800:
            confirmed += 1
            graphic_x.append(i[0])
            graphic_y.append(i[1])
    return [confirmed, graphic_x, graphic_y, f"chill - {confirmed / len(arr)}"]


def drive_mode(arr):
    confirmed = 0
    graphic_x = []
    graphic_y = []
    for i in arr:
        if -1000 < i[0] < 3000 and -3000 < i[1] < 3000:
            confirmed += 1
            graphic_x.append(i[0])
            graphic_y.append(i[1])
    return [confirmed, graphic_x, graphic_y, f"drive - {confirmed / len(arr)}"]


arr, arr_x, arr_y, arr_z = read_file('../tests/14,48,33-Даниил, левая-Sport.txt')
res = [sport_mode(arr), chill_mode(arr), drive_mode(arr)]

res.sort(reverse=True)
build_graphic(res[0][1], res[0][2], [], res[0][3])