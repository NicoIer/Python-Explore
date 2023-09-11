# 题目说明
# 大家知道12306的卖票系统是个非常复杂的东西，这里考虑简单的情况
# 假设火车从A到B，有M个站点，一共N个座位
# 写程序模拟车票分配情况，有座就卖
# 输入 有三个整数M（代表车站数目，M<10), N(代表座位数目,N<1000) K(代表操作数目)
# 5 5 10
# Q 0 4
# B 0 2 3
# B 3 4 2
# Q 2 3
# B 1 4 3
# B 1 4 2
# Q 0 4
# R 0 3 1
# R 1 4 5
# Q 2 4
# 输出
# 5
# OK!
# OK!
# 5
# Fail!
# OK!
# 0
# Fail!
# Fail!
# 1
import dataclasses

if __name__ == "__main__":
    num_station, num_set, num_operation = map(int, input().split())

    operation_queue = []
    for _ in range(num_operation):
        line = list(map(str, input().split()))
        operation_queue.append(line)
    # operation_queue = [["Q", 0, 4],
    #                    ["B", 0, 2, 3],
    #                    ["B", 3, 4, 2],
    #                    ["Q", 2, 3],
    #                    ["B", 1, 4, 3],
    #                    ["B", 1, 4, 2],
    #                    ["Q", 0, 4],
    #                    ["R", 0, 3, 1],
    #                    ["R", 1, 4, 5],
    #                    ["Q", 2, 4]]


    @dataclasses.dataclass
    class Record:
        def __init__(self, start, end, num):
            self.start = start
            self.end = end
            self.num = num

        def __repr__(self):
            return f"(start={self.start}, end={self.end}, num={self.num})"


    sold_record = []  # 当前购票状态


    def query_sold(start, end) -> int:
        sold = 0  # 计算这段路程中已经卖出的票数
        for record in sold_record:
            # 只要有交叉就要减去
            if record.start <= start < record.end or record.start < end < record.end:
                sold += record.num
        return sold


    def query_left(start, end) -> int:
        """
        查询从[start:end]的余票数量
        :param start: 起始站
        :param end: 终点站
        :return: 余票数量
        """
        return min(num_set - query_sold(start, end) -2,num_set- query_sold(start, end))


    def buy(start, end, num) -> bool:
        """
        购票
        :param start: 起始站
        :param end: 终点站
        :param num: 购票数量
        :return: 是否购票成功
        """
        # 如果有余票
        if query_left(start, end) >= num:
            sold_record.append(Record(start, end, num))
            return True
        else:
            return False


    def refund(start, end, num) -> bool:
        """
        退票
        :param start: 起始站
        :param end: 终点站
        :param num: 退票数量
        :return: 是否退票成功
        """
        # 如果有余票
        if query_left(start, end) < num:
            return False
        else:
            # 先把所有的都退了
            remove_list = []
            for record in sold_record:
                if record.start == start and record.end == end:
                    if record.num < num:
                        num -= record.num
                        remove_list.append(record)
                    else:
                        record.num -= num
                        return True
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
        # print("OP", operation)
        # print("sold_record:", sold_record)
