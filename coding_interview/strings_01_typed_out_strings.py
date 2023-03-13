def clear_backspaces(s):
    s_list = []
    for item in s:
        if item != '#':
            s_list.append(item)
        else:
            if s_list:
                s_list.pop()
    return ''.join(s_list)


def compare_strings(s, t):
    return clear_backspaces(s) == clear_backspaces(t)


def compare_strings(s, t):
    p0 = len(s)
    p1 = len(t)

    while (p0 > 0) and (p1 > 0):
        remove_from_s =

    return
