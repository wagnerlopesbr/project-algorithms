def merge(left, right):  # type: ignore
    result = []
    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):  # type: ignore
        if left[left_i] < right[right_i]:
            result.append(left[left_i])  # type: ignore
            left_i += 1
        else:
            result.append(right[right_i])  # type: ignore
            right_i += 1

    result.extend(left[left_i:])  # type: ignore
    result.extend(right[right_i:])  # type: ignore

    return result  # type: ignore


def merge_sort(entry):  # type: ignore
    if len(entry) <= 1:  # type: ignore
        return entry  # type: ignore

    middle = len(entry) // 2  # type: ignore
    left = entry[:middle]  # type: ignore
    right = entry[middle:]  # type: ignore

    left = merge_sort(left)  # type: ignore
    right = merge_sort(right)  # type: ignore

    return merge(left, right)  # type: ignore


def is_anagram(first_string, second_string):  # type: ignore
    if first_string == "" and second_string == "":
        return "", "", False

    sorted_str1 = ''.join(merge_sort(first_string.lower()))  # type: ignore
    sorted_str2 = ''.join(merge_sort(second_string.lower()))  # type: ignore

    return sorted_str1, sorted_str2, sorted_str1 == sorted_str2
