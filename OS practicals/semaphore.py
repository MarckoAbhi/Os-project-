import threading

# Initialization
semaphore = threading.Semaphore(1)  # Binary semaphore (initial value 1)

# Shared variable
shared_variable = 0

# Process 1
def process_1():
    global shared_variable
    semaphore.acquire()
    # Critical Section
    shared_variable += 1
    print("Process 1: Shared Variable =", shared_variable)
    semaphore.release()

# Process 2
def process_2():
    global shared_variable
    semaphore.acquire()
    # Critical Section
    shared_variable += 2
    print("Process 2: Shared Variable =", shared_variable)
    semaphore.release()

# Create threads
thread1 = threading.Thread(target=process_1)
thread2 = threading.Thread(target=process_2)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()
