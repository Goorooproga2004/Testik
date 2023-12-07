if __name__ == '__main__':
    summa = 1
    a = 3
    n = 2
    N = 1001
    for i in range((N - 1) // 2):
        summa += a * 4 + n * 6
        a += n * 4 + 2
        n += 2
    print(summa)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
