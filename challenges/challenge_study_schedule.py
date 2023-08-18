def study_schedule(permanence_period, target_time):

    if not permanence_period or target_time is None:
        return None

    count = 0

    for period in permanence_period:
        if not isinstance(period, tuple) or len(period) != 2 or period[0] > period[1]:
            return None

        if period[0] <= target_time <= period[1]:
            count += 1

    return count


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_times = [5, 4, 3, 2, 1]

max_count = 0
best_time = None

for time in target_times:
    count = study_schedule(permanence_period, time)
    if count is None:
        print("Permanence period or target time is invalid.")
        break

    if count > max_count:
        max_count = count
        best_time = time

if best_time is not None:
    print(f"O melhor horário é {best_time}, com {max_count} estudantes presentes.")