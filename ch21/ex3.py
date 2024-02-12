#daemon threads
import threading
import time

# Function executed by a daemon thread
def task():
    while True:
        print("Daemon thread is running")
        time.sleep(1)

# Create a daemon thread
thread = threading.Thread(target=task)
thread.daemon = True

# Start the daemon thread
thread.start()

# Main program continues executing
print("Main program is running")

# Sleep for some time to allow the daemon thread to run
time.sleep(5)

# The program exits without waiting for the daemon thread to complete
print("Exiting the program")
