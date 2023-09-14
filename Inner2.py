

def Demo():
    print("inside demo")

def Fun():
    print("Inside fun")

def Hello(FPTR):
    print("inside hello")
    FPTR()
 
Hello(Demo)
Hello(Fun)

