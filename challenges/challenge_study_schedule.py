def study_schedule(permanence_period, target_time):  # type: ignore
    if target_time is None:
        return None

    if not permanence_period or any(
        len(period) != 2  # type: ignore
        or not all(isinstance(t, int) for t in period)  # type: ignore
        for period in permanence_period  # type: ignore
    ):  # type: ignore
        return None

    students_present = 0

    for start, end in permanence_period:  # type: ignore
        if start <= target_time <= end:
            students_present += 1

    return students_present
