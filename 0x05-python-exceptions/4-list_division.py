#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for item_1, item_2 in zip(my_list_1, my_list_2):
        try:
            result = item_1 / item_2
        except (IndexError, TypeError):
            print("Error: Unable to perform division.")
            result = 0
        except ZeroDivisionError:
            print("Error: Division by zero.")
            result = 0
        finally:
            new_list.append(result)

    return new_list
