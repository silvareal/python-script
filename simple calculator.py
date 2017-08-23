print("SIMPLE CALCULATOR")
while True:
    name=str(input("what is your name bruh :"))
    if len(name) > 2:
        print("bravo!",name,"what can i do for you? \n ")
        break
    if len(name) < 2 or name !=str(name):
        print('invalid syntax ')
        continue
    print("HINT:1.name should be in words \n 2.name should be greater than 2 alphabet")

#creating  functions for signs
def add(x,y):
    '''number -> number
    it print add what ever the number in parameter x and y

    >>>add(3+2)
    5'''
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y
def square(x,y):
    return x**y


def calculator():
    
    #input what you want to do
    print ("\nfor addition;press 1 \n for subtraction:press 2 \n for multiplication:press3 \n for division:press4 \n for exponent;press5")       
    cal =input ("input operation:1  ,2  ,3   ,4   ,5  :")   
    number1=int(float((input("input x:"))))
    number2=int(float(input("input y:")))
        
    if cal=='1':
         print(name,",",number1,"+",number2,"=",add(number1,number2))
    elif cal=='2':
        print(name,",",number1,'-',number2,"=",subtract(number1,number2))
    elif cal=='3':
         print(name,",",number1,"*",number2,"=",multiply(number1,number2))
    elif cal=='4':
        print(name,",",number1,"/",number2,"=",divide(number1,number2))
    elif cal=='5':
        print(name,",",number1,"**",number2,"=",square(number1,number2))
    elif cal !="1" or cal !="2" or cal !="3" or cal !="4" or cal !=5:
        print(name,",input operations correct")
    else:
        print('invalid syntax',name,",",calculator())
calculator()


def again():
    while True:
        repeat=input("do you want to keep calculating: \n yes/no: ")
        if  repeat=="yes" or repeat=="y" or repeat=="YES" or repeat=="Y":
            print("yhp",calculator(),"bring it on  bruh")
            continue
        if  repeat=="no" or repeat=="NO" or repeat=="n" or repeat=="N":
          print(name,",","feel my accuracy,am always here to help")
          break
        else:
            print("bravo",again())
again()

            

