import time
from time import sleep
from datetime import datetime


def ft_progress(listy):

    rng = len(listy)
    start = time.time()
    rest = " " * 21

    for x in range(rng):
        perc = 100 * (x + 1) / rng
        iter_time = time.time()
        et = iter_time - start
        eta = (rng * et / (x + 1)) - et
        progress = perc // 5
        bar = "=" * int(progress) + ">"
        rest = " " * (20 - len(bar))
        print(f'ETA: {eta:.2f} | [{bar} {rest}] | [{perc}%] | {x + 1}/{rng} | elapsed time: {et:.2f}', end='\r')

        yield x


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
