#!/bin/env python3
import argparse
import time
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
    fibonachi = fibonachi_generator()
    for i, f in enumerate(fibonachi):
        if i > args.N:
            break
        time_s = time.perf_counter()
        print(f"{i}: {f}")
        time_e = time.perf_counter()
        print(f'Calc time = {time_e - time_s}')

