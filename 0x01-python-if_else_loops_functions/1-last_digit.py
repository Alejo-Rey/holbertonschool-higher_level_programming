#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    str_num = str(number)[-1:]
    str_num = int(str_num)
else:
    str_num = str(number)[-1:]
    str_num = -int(str_num)
if str_num > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, str_num))
elif str_num == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, str_num))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, str_num)) 
