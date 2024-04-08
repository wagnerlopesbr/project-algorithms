def find_duplicate(nums):  # type: ignore
    s_nums = sorted(nums)  # type: ignore

    return next((s_nums[i] for i in range(1, len(s_nums))  # type: ignore
                if s_nums[i] == s_nums[i-1]  # type: ignore
                and s_nums[i] > 0), False)  # type: ignore
