class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            new_body = [newInterval] + intervals
        elif intervals[-1][1] < newInterval[0]:
            new_body = intervals + [newInterval]
        else:
            new_body = list()
            body = iter(intervals)
            for interval in body:
                if interval[1] < newInterval[0]:
                    new_body.append(interval)
                elif newInterval[1] < interval[0] and new_body[-1][1] < newInterval[0]:
                    new_body += [newInterval, interval]
                elif interval[0] <= newInterval[1]:
                    newInterval[0] = min(newInterval[0], interval[0])
                    newInterval[1] = max(newInterval[1], interval[1])
                    interval = next(body, None)
                    if interval:
                        while newInterval[1] >= interval[0]:
                            newInterval[1] = max(newInterval[1], interval[1])
                            interval = next(body, None)
                            if not interval:
                                break
                    new_body += [newInterval, interval]
                else:
                    new_body.append(interval)
        new_body = [item for item in new_body if item is not None]
        return new_body



if __name__ == '__main__':
    # intervals = [[1, 5], [6, 9]]
    # newInterval = [2, 5]
    # intervals = [[2, 3], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [17, 18]
    #intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]     # Вводные данные
    #newInterval = [4, 8]
    intervals = [[3,5],[12,15]]
    newInterval = [6,6]
    sol = Solution()
    print(sol.insert(intervals, newInterval))          # Функция возвращает лист => при желании результат можно записать в intervals
