def two_digits(st):
    if len(st) < 2:
        return "0" + st
    else:
        return st

class Timer:
    def __init__(self, hour=0, mi=0, sec=0):
        self.__hour = hour
        self.__min = mi
        self.__sec = sec

    def __str__(self):
        hour = two_digits(str(self.__hour))
        minu = two_digits(str(self.__min))
        sec = two_digits(str(self.__sec))
            
        return  hour + ":" + minu + ":" + sec

    def next_second(self):
        self.__sec += 1
        if self.__sec >= 60:
            self.__min += 1
            self.__sec = 0
        if self.__min >= 60:
            self.__min = 0
            self.__hour += 1
        if self.__hour >= 24:
            self.__hour = 0

            

    def prev_second(self):
        self.__sec -= 1
        if self.__sec < 0:
            self.__sec = 59
            self.__min -= 1
        if self.__min < 0:
            self.__min = 59
            self.__hour -= 1
        if self.__hour < 0:
            self.__hour = 23

            
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    
