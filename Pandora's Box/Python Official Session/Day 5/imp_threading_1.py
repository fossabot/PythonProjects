import threading
import datetime
import time

print('-' * 70)

def write_file(trdname, fname, msg, delay):
    print('{} Started'.format(trdname))

    with open(fname, 'w') as fhandle:
        for n in range(1, 6):
            tstamp = datetime.datetime.now().strftime('%c')
            fhandle.write('{} -> {}\n'.format(tstamp, msg))
            time.sleep(delay)

    print('{} Completed'.format(trdname))

# Create the Threaded Objects
trd1 = threading.Thread(target=write_file,
                        args=('T1', 't1_out.txt', 'Into T1', 3))
trd2 = threading.Thread(target=write_file,
                        args=('T2', 't2_out.txt', 'Into T2', 1))

# Start the threads
trd1.start()
time.sleep(2)
trd1.join()
trd2.start()
trd2.join()

# Make the main program to wait until
# all the threads completed its execution
# trd1.join()
# trd2.join()

print('End of Main Program Execution')

print('-' * 70)
