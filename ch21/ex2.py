import threading
students = {'population': 0}
counter = 1

# Lock for synchronization
lock = threading.Lock()

# Function to increment the population
def admit_student():
    global students
    global counter
    lock.acquire()
    print(f'Admitting student{counter}')
    students['population'] += 1
    print(f'Admitted student{counter}')
    #print separator lines
    print('-'*20)
    counter +=1
    lock.release()

# Creating multiple threads to admit students
threads = []
for _ in range(5):
    thread = threading.Thread(target=admit_student)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Printing the updated population of students
print("Total number of students admitted:", 
students['population'])
