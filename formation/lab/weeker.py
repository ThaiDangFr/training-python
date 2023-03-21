class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    
    def __init__(self, day):
        if day not in Weeker.__days:
            raise WeekDayError
        else:
            self.__day = day
            self.__index = Weeker.__days.index(day)

    def __str__(self):
        return self.__day

    def add_days(self, n):
        index = self.__index + n
        if index > 6:
            index = index % 7
        self.__day = Weeker.__days[index]
        self.__index = index

    def subtract_days(self, n):
        index = self.__index - n
        if index > 6:
            index = index % 7
        elif index < -7:
            index = index % -7
        self.__day = Weeker.__days[index]
        self.__index = index   

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
    
