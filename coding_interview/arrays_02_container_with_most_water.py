def largest_area_slower(height):
    max_area = 0
    number_of_lines = len(height)

    for idx_a in range(number_of_lines):
        for idx_b in range(idx_a+1, number_of_lines):
            area = min(height[idx_a], height[idx_b]) * (idx_b - idx_a)
            max_area = max(max_area, area)

    return max_area


def largest_area(heights):
    left_idx = 0
    right_idx = len(heights)-1
    max_area = 0

    while left_idx < right_idx:
        left = heights[left_idx]
        right = heights[right_idx]
        height = min(left, right)
        width = right_idx - left_idx
        area = height*width
        max_area = max(max_area, area)

        if left < right:
            left_idx += 1
        else:
            right_idx -= 1

    return max_area
