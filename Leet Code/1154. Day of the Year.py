class Solution:
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Solution.is_leap_year(year):
            days_in_month[2] = 29

        day_number = sum(days_in_month[i] for i in range(1, month)) + day
        return day_number