import time

duration = time.time()
# Я знаю что сдесь должно быть число, а не импорт билиотеки time,
# надеюсь это шалость простительна

my_time = (24 * 60 ** 2, 60 ** 2, 60, 365 * 24 * 60 ** 2)

years = duration // my_time[3]
duration = duration % my_time[3]

days = duration // my_time[0]
hours = duration % my_time[0] // my_time[1]
minutes = duration % my_time[0] % my_time[1] // my_time[2]
second = duration % my_time[0] % my_time[1] % my_time[2]

print("years: {} days: {} hours: {} minutes: {} seconds: {} ".format(int(years), int(days), \
                                                                     int(hours), int(minutes), round(second, 2)))
