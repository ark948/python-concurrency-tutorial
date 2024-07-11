from time import sleep, perf_counter

def task():
    # a function that takes one second to complete
    print("Starting a task...")
    sleep(1)
    print("done")


start_timne = perf_counter()

task()
task()

end_time = perf_counter()

print(f'It took {end_time - start_timne: 0.2f} second(s) to complete.')