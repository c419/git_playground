#!/bin/env python3
"""Prints fibonachi sequence of given length and show computation time
"""
import argparse
import time
import functools
import itertools

class bcolors:
    COLOR_RED   = "\033[1;31m"  
    COLOR_BLUE  = "\033[1;34m"
    COLOR_CYAN  = "\033[1;36m"
    COLOR_GREEN = "\033[0;32m"
    ENDC = '\033[0m'


def next_color(color_cls=bcolors):
	colors = [attr for attr in dir(color_cls) if attr.startswith('COLOR')]
	for color in itertools.cycle(colors):
		yield getattr(color_cls, color)

def reset_color(colors_cls=bcolors):
	return colors_cls.ENDC

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_s = time.perf_counter()
        ret = func(*args, **kwargs)
        time_e = time.perf_counter()
        print(f'Calc time of {func.__name__} = {time_e - time_s}')
        return ret
    return wrapper

@timer_decorator
def fibonachi_sequence(n):
    """print n fibonachi numbers"""
    fibonachi = fibonachi_generator()
    fibonachi_sequence = []
    for i, f in enumerate(fibonachi):
        if i > args.N:
            break
        fibonachi_sequence.append(f)
    return fibonachi_sequence
    

def fibonachi_generator():
    """Generator for fibonachi sequence
    """
    f1, f2 = 0, 1
    yield f1
    yield f2
    while True:
        f1, f2 = f2, f1 + f2
        yield f2



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prints given amount of fibonachi sequence")
    parser.add_argument('N', nargs='?', default='10', type=int, help="Number of fibonachi numbers to display, default is 10")
    args = parser.parse_args()
    f_seq = fibonachi_sequence(args.N)
    color = next_color()
    [print(f'{i}: {next(color)}{f}{reset_color()}') for i, f in enumerate(f_seq)]
