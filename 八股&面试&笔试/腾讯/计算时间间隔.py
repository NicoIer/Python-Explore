class TimeStamp:
    def __init__(self, time_stamp: str):
        _ = time_stamp.split("-")
        self.year = int(_[0])
        self.month = int(_[1])
        self.day = int(_[2])

    def cast_to(self) -> int:
        """
        以0000-00-00为基准，转换成天数
        :return:
        """
        # 闰年
        leap_year = lambda x: x % 4 == 0 and x % 100 != 0 or x % 400 == 0
        ans = 0
        for i in range(1, self.year):
            if leap_year(i):
                ans += 366
            else:
                ans += 365
        for i in range(1, self.month):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                ans += 31
            elif i in [4, 6, 9, 11]:
                ans += 30
            else:
                if leap_year(self.year):
                    ans += 29
                else:
                    ans += 28
        ans += self.day
        return ans


def solution(start_time_stamp: TimeStamp, end_time_stamp: TimeStamp) -> int:
    """
    :param start_time_stamp: 开始时间
    :param end_time_stamp: 结束时间
    :return: 时间间隔
    """
    return abs(start_time_stamp.cast_to() - end_time_stamp.cast_to())


if __name__ == "__main__":
    start_time_stamp = TimeStamp(input())
    end_time_stamp = TimeStamp(input())
    print(solution(start_time_stamp, end_time_stamp))
