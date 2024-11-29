def sum_of_intervals(intervals):
    result = 0
    intervals = sorted(intervals)
    index = 0
    while True:
        try:
            if intervals[index+1][0] <= intervals[index][1]:
                intervals[index] = [
                    min(intervals[index][0], intervals[index+1][0]), max(intervals[index+1][1], intervals[index][1])
                ]
                del intervals[index+1]
            else:
                index += 1
        except IndexError:
            break
    for a, b in intervals:
        result += b-a
    return result