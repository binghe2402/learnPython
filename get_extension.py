def get_extension(filename):

    index = filename.index(".")
    return filename[index+1:]


def main():
    filename = input("请输入文件名：")
    try:
        extension = get_extension(filename)
    except ValueError:
        print("输入的文件名不合法")
    else:
        print(extension)


if __name__ == '__main__':
    main()
