def linecount(filename):
    with open(filename) as fin:
        lines = fin.readlines()
        line_count = len(lines)
    return line_count


if __name__ == '__main__':
    print(linecount("output_v1.txt"))
    print(linecount("wc.py"))

