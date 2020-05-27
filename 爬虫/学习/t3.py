import requests
from bs4 import BeautifulSoup
import time

init_URL = ''


def get_web(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup


def main():

    filt = ['贴主', '评分完成：', '【未完待续】']
    with open(r'txt', 'w', encoding='utf-8') as f:
        soup = get_web(init_URL)
        for line in soup.pre.strings:
            if not any((word in line for word in filt)):
                f.write(line if '.com' not in line else '\n')

        all_link = []
        for line in soup.pre.find_all('a'):
            all_link.append(line['href'])

        print(all_link)
        for link in reversed(all_link):
            time.sleep(2)
            print(link)
            soup = get_web(link)
            print(soup.title.string)
            for line in soup.pre.strings:
                if not any((word in line for word in filt)):
                    f.write(line if '.com' not in line else '\n')


if __name__ == '__main__':
    main()
