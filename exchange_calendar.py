import holidays as hday
from datetime import date, datetime, timedelta

class ExchangeCalendar:

    _WEEKDAYS = [0, 1, 2, 3, 4]
    _WEEKENDS = [5, 6]

    def __init__(self, country_code):
        self.holidays = hday.CountryHoliday(country_code)

    def is_holiday(self, day: str) -> bool:
        return day in self.holidays

    def find_next_working_day(self, day: str):
        d = datetime.strptime(day, "%Y-%m-%d").date()
        next_date = d + timedelta(days=1)
        while next_date.weekday() in self._WEEKENDS or next_date in self.holidays:
            next_date = next_date + timedelta(days = 1)
        return next_date

    def find_prev_working_day(self, day: str):
        d = datetime.strptime(day, "%Y-%m-%d").date()
        prev_date = d + timedelta(days=-1)
        while prev_date.weekday() in self._WEEKENDS or prev_date in self.holidays:
            prev_date = prev_date + timedelta(days=-1)
        return prev_date

