def merge_sorted_arrays_simple(a, b):
    a.extend(b)
    return sorted(a)


def merge_sorted_arrays(a, b):
    output = list()

    first_a = a.pop(0)
    first_b = b.pop(0)

    while first_a or first_b:
        if first_a <= first_b:
            output.append(first_a)
            first_a = a.pop(0)
        else:
            output.append(first_b)
            first_b = b.pop(0)

    return output


merge_sorted_arrays([0, 3, 4, 31], [4, 6, 8, 30])
