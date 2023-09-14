import schedule
import time
import datetime

def Fun():
    print("Inside fun")

def main():
    print("inside Task scheduler")
    
    schedule.every(1).minutes.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(20)


if __name__ =="__main__":
    main()