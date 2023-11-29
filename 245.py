import datetime

day = "2023-11-29"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))
