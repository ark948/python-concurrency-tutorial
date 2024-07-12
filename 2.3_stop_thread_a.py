from threading import Thread, Event
from time import sleep

def task(event: Event) -> None:
    for i in range(6):
        print(f'Running #{i+1}')
        sleep(1)
        if event.is_set():
            print('The thread was stopped prematurely.')
            break
    else:
        print('The thread was stopped maturely.')

def main() -> None:

    event = Event()
    thread = Thread(target=task, args=(event,))
    
    # start the thread
    thread.start()

    # suspend  the thread after 3 seconds
    sleep(3)

    # stop the child thread
    event.set()    
   

if __name__ == '__main__':
    main()