# Import threading

import threading

def task1():
    print('Task 1')

def task2():
    print('Task 2')

#creating threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# start
#start the threads
thread1.start()
thread2.start()

#wait for the threads to complete
thread1.join()
thread2.join()
print("All tasks completed")

# Create a lock object
lock = threading.Lock()
lock.release()


