import schedule
import time
import datetime
import sys


def Task_Minute():
    print("Task based on minutes schedule at : ",datetime.datetime.now())


def Task_Hour():
    print("Task based on Hour schedule at : ",datetime.datetime.now())

def Task_Day():
    print("Task based on Day schedule at : ",datetime.datetime.now())


def script_Terminator():
    sys.exit()



def main():
    print("inside Task scheduler")
    print("Current Time Is:",datetime.datetime.now())


    schedule.every(1).minutes.do(Task_Minute)
    schedule.every(3).minutes.do(script_Terminator)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().saturday.at("18:00").do(Task_Day)
    schedule.every().day.at("20:37").do(Task_Day)


    while(True):
        schedule.run_pending()
        time.sleep(1)





if __name__ =="__main__":
    main()