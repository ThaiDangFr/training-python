from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        counter = 0
        for m in range(1,13):
            for weeks in self.monthdays2calendar(year, m):
                print(weeks)
                r = list(filter(lambda x: x[0]>0 and x[1]==weekday, weeks))
                counter += len(r)
                    
        return counter


c = MyCalendar()
print(c.count_weekday_in_year(2019,0)) # 52 lundi en 2019
print(c.count_weekday_in_year(2000,6)) # 53 dimanche en 2000
