def trap(height):
    volume = 0
    current_max = 0
    current_diffs = list()

    for column in height:
        if column >= current_max:
            current_max = column
            volume += sum(current_diffs)
            current_diffs = list()
        