import schedule
import time
import datetime


def Fun():
    print("Inside fun at the time:",datetime.datetime.now())

def main():
    print("inside Task scheduler")
    print("Current Time Is:",datetime.datetime.now())

    
    schedule.every(1).minutes.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)




if __name__ =="__main__":
    main()