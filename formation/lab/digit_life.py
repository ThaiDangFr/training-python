def digit_life(birthday):
    date = birthday
    while len(date) > 1:
        sum = 0
        for s in date:
            i = int(s)
            sum += i
        date = str(sum)
    return date

birthday = input("Birthday: ")

if len(birthday) != 8 or not birthday.isdigit():
    print("invalid format")
else:
    print("Digit life", digit_life(birthday))
