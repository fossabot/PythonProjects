print('-' * 70)

import threading
import datetime
import time

class ImplementThread(threading.Thread):
    all_trds = []

    def __init__(self, trd_name, fname, msg, delay):
        super(ImplementThread, self).__init__()
        self.trd_name = trd_name
        self.fname = fname
        self.msg = msg
        self.delay = delay

        # Add the thread
        ImplementThread.all_trds.append(self)

    def run(self):
        print(self.trd_name, '->', self.is_alive())

        # Acquire the Lock
        trdLock.acquire()

        print('{} Started'.format(self.trd_name))

        with open(self.fname, 'w') as fhandle:
            for n in range(1, 6):
                tstamp = datetime.datetime.now().strftime('%c')
                fhandle.write('{} -> {}\n'.format(tstamp, self.msg))
                time.sleep(self.delay)

        print('{} Completed'.format(self.trd_name))

        # Release the Lock
        trdLock.release()

# Create the thread lock object
trdLock = threading.Lock()

# Create the threaded objects
trd1 = ImplementThread('T1', 't1_out.txt', 'Into T1', 3)
trd2 = ImplementThread('T2', 't2_out.txt', 'Into T2', 1)

# Start the threads
for trd in ImplementThread.all_trds:
    trd.start()
    time.sleep(2)

# Make the program to wait
for trd in ImplementThread.all_trds:
    trd.join()

print('-' * 70)
