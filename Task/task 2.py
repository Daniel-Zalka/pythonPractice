my_list = [5, 12, 30, 60, 120, 240, 600, 900, 360, 6000]

def dev_number(my_list):
    """A function that checks which index divides all the numbers that follow it and is divided by all the numbers before that index,"
    the function returns at the end of the run the index number that satisfies the two conditions."""

    index = 0
    dev = 0
    my_list1 = []
    count = 0

    for number in my_list:
        count = 0
        dev = dev + 1
        for next_num in range(my_list.index(number), len(my_list)):
            if my_list[next_num] % number != 0:
                break
            if my_list[next_num] % number == 0:
                count = count + 1
                if count == len(my_list) - dev:
                    my_list1.append(number)

    for g in my_list1:
        correct_num = 0
        dev = dev +1
        for i in range(0, my_list1.index(g)):
            if g % my_list1[i] != 0:
                break
            if g % my_list1[i] == 0:
                correct_num = my_list.index(g)
                return correct_num

print("index number", dev_number(my_list))








