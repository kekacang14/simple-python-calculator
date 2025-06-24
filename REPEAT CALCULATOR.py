#set data input from user as variables
import math
print("hello, please enter your name")
name = input("name: ")
print("hello " +name)

#calculation function
def nombor():
    print("please enter your number ")
    num1 = float(input("your first number : "))
    num2 = float(input("your second number : "))

    while True:
        print("which operation do you want?")
        operation = input (" add, subs, time, divide : ").lower()
        if operation == "add":
            print("= ",(num1 + num2))
            break
        elif operation == "subs":
            print("= ",(num1 - num2))
            break
        elif operation == "time":
            print("= ",(num1 * num2))
            break
        elif operation == "divide":
            if num2 != 0:
                print("= ",(num1 / num2))
            else : print(" number cannot be divided by 0, please try again ")
            return
        else :print(" option is not available, please try again ")
        return

#user choose the operation
choice = input("want to do some calculation? yes or no? ").lower()

if choice == "yes":
#allows user to repeat the operation once finished
    while True:
      nombor()
      repeat = input("repeat? yes or no? " ).lower()
      if repeat == "no":
        print("ok, see yaa")
        break

      elif repeat != "yes" :
        print("Invalid input. Exiting...")
        break

elif choice == "no":
    print("ok, see yaa")

else : print("please try again ")


