import datetime


class Date:
    WEEK = 7
    ONE_DAY = datetime.timedelta(days=1)

    def __init__(self):
        self.today = datetime.date.today()

    @staticmethod
    def init_date(date):
        "вернуть день, месяц и год"
        pass

    def date_to_str(self, date):
        "перевести дату в строку в формате dd.mm.yy"
        pass

    def one_week(self):
        last_day = self.today
        week = [self.date_to_str(last_day)]

        "заполнить список week датами с текущего и семью следующими"

        return week




