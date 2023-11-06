class ClockIterator:
    def __init__(self):
        self.hours = 0
        self.minutes = 0

    def __iter__(self):
        return self

    def __next__(self):
        time_format = f"{self.hours:02d}:{self.minutes:02d}"
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours = 0 if self.hours == 23 else self.hours + 1
        return time_format

if __name__ == "__main__":
    clock = ClockIterator()
    for _ in range(1440):  # Because who really wants an infinite loop?
        print(next(clock))
