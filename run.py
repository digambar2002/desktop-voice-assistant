# Run two proccess from foreground Jarvis and background hot word detection

# Library use to run two process
import multiprocessing


# Define functions to be run as separate processes

# To run Jarvis
def process1():
    # Code for process 1
    print("Process 1 is running.")
    from main import start
    start()
 
# To run hotword
def process2():
    # Code for process 2
    print("Process 2 is running.")
    from hotword import hotword
    hotword()

# Start both processes
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
