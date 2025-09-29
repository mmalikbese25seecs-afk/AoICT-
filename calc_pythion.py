
print("Pythonn Calculator")
print("Choose specifeid no. for mats operation")
print("1. Addition, 2.Subtraction, 3. multiplication, 4. Division,5.check even odd,6, percentage,7. exit")


num = input("Enter your choice (1-6):") 
while num!='7':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if num in ['1', '2','3','4','5','6','7']:
    

    if num == '1':
        print("Add=", num1 + num2) 
    elif num == '2':
        print("Subtraction=", num1 - num2)
    elif num == '3': 
     print("Multiply=:", num1 * num2)
    elif num == '4':
     print("Division=", num1 / num2)
    elif num =='5':    
         eodd = int(input("Enter yournumber: "))
         if eodd % 2 == 0:
            print("The number is Even")
         else:
            print("The number is Odd")
    elif num=='6':
        
        a = float(input("Enter the part value: "))
        tot = float(input("Enter the total value: "))
        
        print("Result:", (a/ tot) * 100, "%")
    
        

             