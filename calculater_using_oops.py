class calculator:
    def add(self,a,b):
        return a+b
    def Subtract(self,a,b):
        return a-b   

    def Multiply(self,a,b):
        return a*b

    def Divide(self,a,b):
        return a/b        

my_cal = calculator()        
print("***** Welcome to the IQCALCULAToR ******")
while True:
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
       
    try:
        ch = int(input("Select opraction :"))
    except:
        print("Plz Enter Integer Number ")
        continue    

    if ch in (1,2,3,4,5):
        if(ch==5):
            print("****Thanks for using our IQ CALCULAToR****")
            break
        
        try:
            a = float(input("Enter first Number: "))
            b = float(input("Enter Second Number: "))
        except:
            print(" **Plz enter integer value** ")
            continue                 
        if (ch==1):
            print(f"{a} + {b} = {my_cal.add(a,b)}")
        if (ch==2):
            print(f"{a} - {b} = {my_cal.Subtract(a,b)}")    
        if (ch==3):
            print(f"{a} * {b} = {my_cal.Multiply(a,b)}") 
        if (ch==4):
            print(f"{a} / {b} = {my_cal.Divide(a,b)}")
        
    else:
        print("****Plz Enter valid Input****\n")