# using multithreading and thread pools and map function instead of submit
from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    return f'Done with task {id}'

start = perf_counter()

with ThreadPoolExecutor() as executor:
    results = executor.map(task, [1, 2])
    for result in results:
        print(result)

finish = perf_counter()

print(f"It took {finish-start} second(s) to finish.")