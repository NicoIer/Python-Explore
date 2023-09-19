import dataclasses
from typing import List


@dataclasses.dataclass
class Record:
    pos: int
    id: int
    rank: int

    def __init__(self, pos, id, rank):
        self.id = id
        self.pos = pos
        self.rank = rank

def get_rank(records:dict):
    """
    计算排名
    :param records:
    :return:
    """
    # 计算排名

    pos_records = sorted(records.values(), key=lambda x: x.pos)
    cur = 0
    last_pos = pos_records[0].pos
    records[pos_records[0].id].rank = 0
    for i in range(1, len(pos_records)):
        # 如果当前位置和上一个位置相同，则排名相同
        if pos_records[i].pos == last_pos:
            records[pos_records[i].id].rank = cur
        else:
            records[pos_records[i].id].rank = i
            cur = i
            last_pos = pos_records[i].pos



if __name__ == "__main__":
    n, t = map(int, input().split())
    # 初始排名
    pos_list = list(map(int, input().split()))
    velocity_list = list(map(int, input().split()))
    begin_records = dict()
    for i in range(n):
        begin_records[i] = Record(pos_list[i], i, 0)
    get_rank(begin_records)
    # 计算每个人的最终位置
    end_records = dict()
    for i in range(n):
        end_records[i] = Record(pos_list[i] + velocity_list[i] * t, i, 0)

    get_rank(end_records)
    # 比较是否有人的排名进步
    cnt = 0
    for i in range(n):
        if end_records[i].rank > begin_records[i].rank:
            cnt += 1
    print(cnt)



