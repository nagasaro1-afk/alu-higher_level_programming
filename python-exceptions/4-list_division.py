#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        divided = 0
        try:
            divided = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            divided = 0
            print("division by 0")
        except TypeError:
            divided = 0
            print("wrong type")
        except IndexError:
            divided = 0
            print("out of range")
        finally:
            new_list.append(divided)
    return new_list
