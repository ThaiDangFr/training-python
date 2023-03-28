from datetime import datetime

d = datetime(2020,11,4,14,53,0)

print(d.strftime("%Y/%m/%d %H:%M:%S")) # 2020/11/04 14:53:00
print(d.strftime("%y/%B/%d %H:%M:%S %p")) # 20/November/04 14:53:00 PM
print(d.strftime("%a, %Y %b %d")) # Wed, 2020 Nov 04
print(d.strftime("%A, %Y %B %d")) # Wednesday, 2020 November 04
print(d.strftime("Weekday: %w")) # Weekday: 3
print(d.strftime("Day of the year: %j")) # Day of the year: 309
print(d.strftime("Week number of the year: %W")) # Week number of the year: 44
