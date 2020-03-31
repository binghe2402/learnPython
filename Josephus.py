def circle(man):
    index = 0
    setp = 9-1
    while len(man) > 15:
        index += setp

        if index > len(man):
            index -= len(man)
        man.pop(index)

    return man


def main():
    man = list(range(1, 31))
    print(circle(man))


if __name__ == "__main__":
    main()
