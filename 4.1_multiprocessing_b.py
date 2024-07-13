# using multiprocessing, took about 3 seconds
import time
import multiprocessing

def task() -> int:
    result = 0
    for _ in range(10**8):
        result += 1
    return result

if __name__ == "__main__":
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f"It took {finish - start: .2f} second(s) to finish.")