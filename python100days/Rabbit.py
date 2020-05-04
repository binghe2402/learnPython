"""一对兔子，从出生后第3个月起每个月都生一对兔子。
小兔子长到第3个月后每个月又生一对兔子。
假如兔子都不死，请问第1个月出生的一对兔子，
至少需要繁衍到第几个月时兔子总数才可以达到N对？"""
from typing import List


class Rabbit:
    age = 0

    def __init__(self):
        self.age = 1

    def __call__(self, all_rabbits: List):
        if self.age >= 3:
            new_rabbit = Rabbit()
            all_rabbits.append(new_rabbit)
        self.age += 1


i = 0
N = int(input())
new_rabbit = Rabbit()
all_rabbits = [new_rabbit]

while len(all_rabbits) < N:
    for rab in all_rabbits:
        rab(all_rabbits)
    i += 1


print(len(all_rabbits))
print(i)
