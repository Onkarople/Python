#implementaing the python automation pratice and command line arguments


from sys import *

def pattern(No):
    for i in range(0,No):
        for j in range(0,No):
            print("*",end=" ")
        
        print()



def main():
    

    if(len(argv)!=2):
        print("invalid ")
        print("use --U")
        exit()

    if(len(argv)==2):
        if(argv[1] == "--U"):
            print("use python Name_of_app argument")
            exit()


    
        pattern(int(argv[1]))



    print("thank you for using app")
    print("By onkar ople")

    


if __name__ == "__main__":
    main()