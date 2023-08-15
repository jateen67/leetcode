class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def can_attend_meetings(intervals):
    intervals.sort(key=lambda i: i.start)

    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False

    return True


print(can_attend_meetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))


# time complexity: o(nlog(n))
# space complexity: o(1)
