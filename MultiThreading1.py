import time
import threading

def DispalyEven(No):
    for i in range(1,No+1):
        if(i%2==0):
            print("Even Number:",i)
    

def DisplayOdd(No):
    for i in range(1,No+1):
        if(i%2!=0):
            print("Odd Number:",i)
    

def main():
    print("demonstration of parallel programming using multiple threads")
    Number=2000

    p1=threading.Thread(target = DispalyEven,args=(Number,))

    p2=threading.Thread(target = DisplayOdd,args=(Number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")



if __name__ == "__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Excution Time is:",end_time-start_time)