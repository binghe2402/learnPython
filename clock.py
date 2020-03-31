import time


class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def __call__(self, para="noon"):
        if para == "noon":
            self._hour = 12
            self._minute = 0
            self._second = 0
        elif para == "midnight":
            self._hour, self._minute, self._second = 0, 0, 0

    def display(self):
        print(f"{self._hour:02}:{self._minute}:{self._second}")
        print("%02d:%02d:%02d" % (self._hour, self._minute, self._second))

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 60:
                    self._hour = 0

    def running_clock(self):
        while True:
            self.display()
            time.sleep(1)
            self.run()


clock = Clock(10, 2, 3)
clock.display()

clock("midnight")
clock.running_clock()
