#!/bin/env python3

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
    fibonachi = fibonachi_generator()
    for f in fibonachi:
        print(f)
