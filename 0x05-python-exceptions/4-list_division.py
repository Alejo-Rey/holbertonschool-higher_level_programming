#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for x , y in zip(my_list_1, my_list_2):
            new_list.append(x / y)
    except (TypeError, ValueError):
        print("wrong type")
        new_list.append(0)
        pass
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("division by 0")
    finally:
        return (new_list)
