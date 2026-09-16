import threading
import time

def square(num):
    print(f"Square: {num*num}")
    time.sleep(1)

def cube(num):
    print(f"Cube: {num*num*num}")
    time.sleep(1)

t1 = threading.Thread(target=square, args=(4,))
t2 = threading.Thread(target=cube, args=(4,))

t1.start()
t2.start()
t1.join()
t2.join()

print("Done!")



# import threading
# import time

# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print(f"{threadName}: {time.ctime(time.time())}")
#         counter -= 1

# class MyThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter

#     def run(self):
#         print(f"Starting {self.name}")
#         threadLock.acquire()      # get exclusive access
#         print_time(self.name, self.counter, 3)
#         threadLock.release()      # release for the next thread

# threadLock = threading.Lock()
# threads = []

# thread1 = MyThread(1, "Thread-1", 1)
# thread2 = MyThread(2, "Thread-2", 2)

# thread1.start()
# thread2.start()
# threads.extend([thread1, thread2])

# for t in threads:
#     t.join()

# print("Exiting Main Thread")