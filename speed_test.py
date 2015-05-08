#! /usr/bin/env python3

import timeit

def a():
    d = {str(i): i for i in range(1000)}
    for i in range(1000):
        del d[str(i)]

    return

def a():
    d = {str(i): i for i in range(1000)}
    for i in range(1000):
        d.pop(str(i))

    return

if __name__ == '__main__':
    print(min(timeit.repeat(b, number=100)))
    print(min(timeit.repeat(a, number=100)))
