#! /usr/bin/env python3

def a(ref, insert_item):
    ref.append(insert_item)

def b():
    ref = []
    insert_items = list(range(10))

    for i in insert_items:
        a(ref, i)

    print(ref)


if __name__ == '__main__':
    b()
