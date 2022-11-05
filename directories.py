import os

cwd = os.getcwd()
# print(cwd)
path_abs = os.path.abspath('output_v1.txt')
# print(path_abs)

dir_cont = os.listdir(cwd)
# print(dir_cont)


def walk(dirname):
    for name in os.listdir(dirname):
        print(name)
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


walk(cwd)
