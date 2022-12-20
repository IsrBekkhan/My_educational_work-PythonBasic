class Date:
    """
    Класс дата, возвращающий строку со значение даты.

    Args:
        day (int): день
        month (int): месяц
        year (int): год
    """
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return 'День: {}\tМесяц: {}\tГод: {}'.format(
            self.day, self.month, self.year
        )

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        """
        Метод, проверяющий корректность даты.

        Args:
            date (str): дата

        :return: bool
        """
        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 3000

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        """
        Метод, возвращающий из строки класс 'Дата'.

        Args:
            date (str): дата

        :return class: Date
        """
        day, month, year = map(int, date.split('-'))
        return cls(day, month, year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

