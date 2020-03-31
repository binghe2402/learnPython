import random

def generate(len=4):
    string = '01234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    return random.choices(string,k=len)
 


def main():
    len = int(input('请输入长度：'))
    code = generate(len)
    print("".join(code))    


if __name__ == '__main__':
    main()