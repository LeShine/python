print("hello world")
a = [1, 2, 3, 4]
for i in a:
    print(i)


def get_num():
    yield 0
    yield 1
    yield 2


gg = get_num()
print(gg)
print(gg.__next__())
print(gg.__next__())
print(gg.__next__())


def yh():
    l = [1]
    while True:
        yield l
        l = [1] + [x+y for x, y in zip(l[1:], l[:-1])] + [1]
        print()


def test_yh():
    n = 0
    results = []
    for t in yh():
        print(t)
        results.append(t)
        n = n + 1
        if n == 10:
            break
    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!')


test_yh()


