

def counting_sort(my_list, max_value):
    counts = [0]*(max_value+1)
    for item in my_list:
        counts[item] += 1

    