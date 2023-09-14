


def main():
   try:
        print("Enter first Number")
        No1=int(input())

        print("Enter Second Number")
        No2=int(input())

        Ans=No1/No2
        print("Division is :",Ans)
    
   except ZeroDivisionError:
        print("inside zero division eroor")
    
   except ValueError:
        print("Inside value error")
    
   except Exception:
        print("Inside last exept error")
    
   finally:
        print("inside finally block")

    



if __name__ == "__main__":
    main()