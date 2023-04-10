from datetime import datetime
from calendar import Calendar

d = datetime(2020,11,4,14,53,0)
print(d.strftime("%Y/%m/%d %H:%M:%S"))
print(d.strftime("%y/%B/%d %H:%M:%S %p"))
print(d.strftime("%a, %Y %b %d"))
print(d.strftime("%A, %Y %B %d"))
print(d.strftime("Weekday: %w"))
print(d.strftime("Day of the year: %j"))
print(d.strftime("Week number of the year: %W"))



class MyCalendar(Calendar):

    
    def count_weekday_in_year(self, year, weekday):
        count = 0
        
        for month in range(1, 13):
            lst = self.monthdays2calendar(year, month)
            for week in lst:
                tpl = week[weekday]
                if tpl[0] != 0:
                    count += 1 

        return count


c = MyCalendar()
print(c.count_weekday_in_year(2019,0))
print(c.count_weekday_in_year(2000,6))


for i in range(1, 4, 2):
    print("*", end="**")
print("***")
