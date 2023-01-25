def sequencer(temp_max=None, max_count=0):
    """
    This function receives a sequence of numbers that ends with 0, and returns the max element and the amount of
    times it appeared in sequence.
    """

    x = int(input())
    if x == 0:
        return temp_max, max_count

    elif temp_max is None:
        temp_max = x

    elif x > temp_max:
        temp_max = x
        max_count = 1

    elif x == temp_max:
        max_count += 1

    return sequencer(temp_max, max_count)


if __name__ == '__main__':
    print(sequencer())
