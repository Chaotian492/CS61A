def move_disk(disk_number, from_peg, to_peg):
    """
    使用print函数代表移动汉诺塔块的过程。
    """
    print(
        "Move disk "
        + str(disk_number)
        + " from peg "
        + str(from_peg)
        + " to peg "
        + str(to_peg)
        + "."
    )


steps = 0


def solve_hanoi(n, start_peg, end_peg):
    """
    使用递归解决汉诺塔问题。
    n -- 汉诺塔块的数量。
    start_peg -- 开始移动前处于的柱子。
    end_peg -- 目标所在的柱子。
    return value-- 移动次数

    >>> steps=solve_hanoi(3,1,2)
    Move disk 1 from peg 1 to peg 2.
    Move disk 2 from peg 1 to peg 3.
    Move disk 1 from peg 2 to peg 3.
    Move disk 3 from peg 1 to peg 2.
    Move disk 1 from peg 3 to peg 1.
    Move disk 2 from peg 3 to peg 2.
    Move disk 1 from peg 1 to peg 2.
    >>> steps
    7
    """
    global steps

    # base line
    if n == 1:
        move_disk(n, start_peg, end_peg)
        steps += 1
    else:
        # 获取备用柱子
        spare_peg = 6 - start_peg - end_peg
        # 将n-1的汉诺塔从开始柱子移动到备用柱子
        solve_hanoi(n - 1, start_peg, spare_peg)
        # 移动第n块积木到目标柱子
        move_disk(n, start_peg, end_peg)
        steps += 1
        # 将n-1的汉诺塔从备用柱子移动到目标柱子
        solve_hanoi(n - 1, spare_peg, end_peg)
    return steps


# step = solve_hanoi(10, 1, 2)
# print(step)
# move_disk(3, 2, 1)
