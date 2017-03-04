# -*- coding: utf8 -*-

import random

total = 100000  # 总共选多少次
switch = 0      # 换门次数
stay = 0        # 保持次数
switch_win = 0  # 换门赢的次数
stay_win = 0    # 保持赢的次数

for i in range(total):
    my_choice = random.randint(0, 2)
    car = random.randint(0, 2)
    # 是否换门
    change = random.choice([True, False])
    if change:
        switch += 1
        if my_choice != car:  # 一开始没选对，换了就赢了
           switch_win += 1
    else:
        stay += 1
        if my_choice == car:  # 一开始就选对，不换就赢了
            stay_win += 1

print '换门', switch
print '换门赢%d次，%.2f%%' % (switch_win, 100.0 * switch_win / switch)
print '不换门', stay
print '不换门赢%d次，%.2f%%' % (stay_win, 100.0 * stay_win / stay)
