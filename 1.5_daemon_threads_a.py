# DO NOT RUN THIS FILE

# daemon threads are background threads, execute tasks in the background

from threading import Thread
import time

# non-daemon function
def show_timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f"Has been waiting for {count} second(s)...")

t = Thread(target=show_timer)
t.start()

answer = input("Do you want to exit?\n")
# IMPORTANT: if you run this program, you must kill the terminal to close it