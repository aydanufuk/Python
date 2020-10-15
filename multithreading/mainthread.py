import threading

print("current thread : ",threading.currentThread().getName())

if threading.currentThread() == threading.main_thread():
    print("main thread...")
else:
    print("other thread")