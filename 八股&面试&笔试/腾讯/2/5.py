import dataclasses


@dataclasses.dataclass
class Point:
    pos: int
    color: int


if __name__ == "__main__":
    # n个点 第i个点的位置为xi 颜色为ci
    # ci=0表示红点 ci=1表示蓝点
    # 每次可以
    # 1.选一个红点 把它移动到 x+1 或者 x-1
    # 2.选择一个蓝点，把它变成红点
    # 最多做k次2
    # 求至少做多少次1才能让任意两个红点间不存在蓝点
    _, k = map(int, input().split())
    pos_list = list(map(int, input().split()))
    color_list = list(map(int, input().split()))
    points = [Point(pos_list[i], color_list[i] for i in range(len(pos_list))]
