# no multiprocessing, took about 7 seconds
import time

def task():
    result = 0
    for _ in range(10**8):
        result += 1
    return result

if __name__ == "__main__":
    start = time.perf_counter()
    task()
    task()
    finish = time.perf_counter()

    print(f"It took {finish - start:.2f} second(s) to finish.")