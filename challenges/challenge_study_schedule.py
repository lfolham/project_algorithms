def study_schedule(permanence_period, target_time):
    if target_time is None or not all(
        len(period) == 2 and isinstance(period[0], int) and
        isinstance(period[1], int) and period[0] <= period[1]
        for period in permanence_period
    ):
        return None

    count = sum(
        period[0] <= target_time <= period[1]
        for period in permanence_period
    )
    return count
