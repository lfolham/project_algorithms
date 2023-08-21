def merge(left, right):
    result = []
    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1

    result.extend(left[left_i:])
    result.extend(right[right_i:])
    return result


def merge_sort(letters):
    if len(letters) <= 1:
        return letters

    middle = len(letters) // 2
    left_half = letters[:middle]
    right_half = letters[middle:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def is_anagram(first_string, second_string):
    first_lowered = first_string.lower()
    second_lowered = second_string.lower()
    first_ordered = merge_sort(list(first_lowered))
    second_ordered = merge_sort(list(second_lowered))
    first_result = ''.join(first_ordered)
    second_result = ''.join(second_ordered)

    if len(first_string) == 0 or len(second_string) == 0:
        return first_result, second_result, False

    return first_result, second_result, first_result == second_result
