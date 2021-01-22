import holidays as hday
import calendar
import typing
import enum
from dataclasses import dataclass
from datetime import date, datetime, timedelta

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)

@dataclass
class Days:
    MON = 0
    TUE = 1

class CountryCode(enum.Enum):
    KR = "KR"
    US = "US"
    JP = "JP"
    HK = "HK"


class ExchangeCalendar:

    _WEEKDAYS = [MON, TUE, WED, THU, FRI]
    _WEEKENDS = [SAT, SUN]

    def __init__(self, country_code: CountryCode):
        self.holidays = hday.CountryHoliday(country_code.value)

    def get_holidays(self):
        return self.holidays

    def add_custom_holiday(self, holiday_date: str, name: str):
        self.holidays.append({holiday_date: name})

    def is_holiday(self, date_string: str) -> bool:
        return date_string in self.holidays

    def next_working_day(self, date_string: str) -> date:
        d = date.fromisoformat(date_string)
        next_date = d + timedelta(days=1)
        while next_date.weekday() in self._WEEKENDS or next_date in self.holidays:
            next_date = next_date + timedelta(days = 1)
        return next_date

    def prev_working_day(self, date_string: str) -> date:
        d = date.fromisoformat(date_string)
        prev_date = d + timedelta(days=-1)
        while prev_date.weekday() in self._WEEKENDS or prev_date in self.holidays:
            prev_date = prev_date + timedelta(days=-1)
        return prev_date

    @staticmethod
    def find_nth_day_in_month(year: int, month: int, day: int, nth: int) -> date:
        """
        nth = 1 -> returns first
        eg) find_nth_day_in_month(2021,1,THU,2)
        """
        c = calendar.Calendar(firstweekday=calendar.SUNDAY)
        month_calendar = c.monthdatescalendar(year, month)
        all_days = [
            d for week in month_calendar for d in week if d.weekday() == day and d.month == month
        ]
        return all_days[nth - 1]

    @staticmethod
    def last_day_in_month(year: int, month: int) -> date:
        c = calendar.Calendar(firstweekday=calendar.SUNDAY)
        month_calendar = c.monthdatescalendar(year, month)
        return month_calendar[-1][-1]
