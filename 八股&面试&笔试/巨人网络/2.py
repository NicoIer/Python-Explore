from dataclasses import dataclass
from typing import List


@dataclass
class Record:
    def __init__(self, start, end, num):
        self.start = start
        self.end = end
        self.num = num


if __name__ == "__main__":
    # 车站数量 和 座位数量
    num_station, num_set, num_operation = 5, 5, 10  # = map(int, input().split())

    operation_queue = [
        ["Q", 0, 4],
        ["B", 0, 2, 3],
        ["B", 3, 4, 2],
        ["Q", 2, 3],
        ["B", 1, 4, 3],
        ["B", 1, 4, 2],
        ["Q", 0, 4],
        ["R", 0, 3, 1],
        ["R", 1, 4, 5],
        ["Q", 2, 4]
    ]

    # []
    # for _ in range(num_operation):
    #     line = list(map(str, input().split()))
    #     operation_queue.append(line)
    #

    # Q 输出余票
    # B 如果有余票则 输出OK 否则 Fail
    # R 如果可以退票 则输出OK 否则 Fail

    # [start,end,num]
    cur_state: List[Record] = []  # 当前购票状态


    def query_left(start, end) -> int:
        """
        查询从[start:end]的余票数量
        :param start: 起始站
        :param end: 终点站
        :return: 余票数量
        """
        sold = 0  # 计算这段路程中已经卖出的票数
        for record in cur_state:
            # 只要有教交叉就要减去
            if record.start <= start < record.end or record.start < end < record.end:
                sold += record.num
        return num_set - sold


    def buy(start, end, num) -> bool:
        """
        从[start:end]购买num张票
        :param start: 起始站
        :param end: 终点站
        :param num: 购买数量
        :return: 是否购买成功
        """
        if query_left(start, end) < num:
            return False
        else:
            cur_state.append(Record(start, end, num))
            return True


    def refund(start, end, num) -> bool:
        """
        从退票num张票
        :param start: 起始站
        :param end: 终点站
        :param num: 退票数量
        :return: None
        """
        remove_list = []
        for record in cur_state:
            # 只要有教交叉就要减去
            if record.start == start and record.end == end:
                if record.num < num:
                    num -= record.num
                    remove_list.append(record)
                else:
                    record.num -= num
                    return True
        for record in remove_list:
            cur_state.remove(record)

        return True


    for operation in operation_queue:
        if operation[0] == "Q":
            start = int(operation[1])
            end = int(operation[2])
            print(query_left(start, end))
        if operation[0] == "B":
            start = int(operation[1])
            end = int(operation[2])
            num = int(operation[3])
            if buy(start, end, num):
                print("OK!")
            else:
                print("Fail!")
        if operation[0] == "R":
            start = int(operation[1])
            end = int(operation[2])
            num = int(operation[3])
            if refund(start, end, num):
                print("OK!")
            else:
                print("Fail!")
