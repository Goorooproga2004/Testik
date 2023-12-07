import time

if __name__ == '__main__':
    start = time.time()
    print(
        f"Total sum is: {sum([i for i in range(0, int(1e6)) if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1]])}")
    print(time.time() - start)


