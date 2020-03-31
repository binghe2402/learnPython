def get_max_and_second(num_seq):
    a = max(num_seq)
    num_seq.remove(a)
    b = max(num_seq)
    return a, b


def main():
    num_seq = input("请输入数字，用空格隔开").split()
    num_seq = [int(x) for x in num_seq]
    print("%d,%d" % get_max_and_second(num_seq))


if (__name__ == '__main__'):
    main()
