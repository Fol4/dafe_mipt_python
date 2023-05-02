import json
import pathlib
import datetime


class Note:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.time = None

        self.filename = (f'{"0" if self.day < 10 else ""}{self.day}.'
                         f'{"0" if self.month < 10 else ""}{self.month}.'
                         f'{self.year % 100}.json')

    @staticmethod
    def int_to_time(time):
        return [datetime.time(time[0][0], time[0][1]), datetime.time(time[1][0], time[1][1])]

    @staticmethod
    def time_to_str(time):
        "перевести время в строку в формате hh:mm-hh:mm"
        pass

    def add_time(self, time):
        self.time = time

    def create_note(self, text):
        data = {}
        path = "путь до файла при помощи pathlib"

        if path.exists():
            with open(str(path), "r") as read_file:
                data = json.load(read_file)
                times = [self.int_to_time(time) for time in data.key()]
                if not self.valid_time(times):
                    return -1
        else:
            path.touch()

        "добавить заметку"

        with open(str(path), "w") as write_file:
            json.dump(data, write_file)

    def valid_time(self, times):
        "проверка возможна ли запись на данное время"
        pass