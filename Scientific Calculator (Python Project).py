import math
print("\nWELCOME :)\n")
print("Type 'a' for addition")
print("Type 's' for subtraction")
print("Type 'm' for multiply")
print("Type 'd' for divide")
print("Type 'sqrt' for Square Root")
print("Type 'exp' for Exponent(Power(a,b))")
print("Type 'sin' for Sine Function")
print("Type 'cos' for Cosine Function")
print("Type 'tan' for Tangent Function")
print("Type 'rad' to Change from Radian to Degree")
print("Type 'deg' to Change from Degree to Radian")
print("Type 'exit' to take Exit From Program")

while True:

    choice = str(input("\nYour Choice: "))
    if choice=='a':
        n=int(input("How many Numbers you want to add: "))
        s=0
        for i in range(1,n+1):
            add=eval(input("Number: "))
            s+=add
        print("Sum is: ",s)
    elif choice=='s':
        n = int(input("How many Numbers you want to subtract: "))
        a = eval(input("Number: "))
        for i in range(1,n):
            sub=eval(input("Number: "))
            a-=sub
        print("Subtraction of the numbers is: ",a)
    elif choice=='m':
        m=int(input("How many Numbers You Want to Multiply: "))
        s=1
        for i in range(1,m+1):
            mul=eval(input("Number: "))
            s*=mul
        print("Multiplication of Entered Number is: ",s)
    elif choice=='d':
        d = int(input("How many numbers you want to division: "))
        a = eval(input("Number: "))
        for i in range(1,d):
            div = eval(input("Number: "))
            a/=div
        print("Division of entered numbers is: ",a)
    elif choice=='sqrt':
        num=eval(input("Enter Number of which you want to find Square Root: "))
        print("Square root is: ",math.sqrt(num))
    elif choice=='exp':
        d = int(input("How many numbers you want: "))
        exp = eval(input("Exponent Number: "))
        for i in range(1, d):
            pow = eval(input("Power Number: "))
            exp **= pow
        print("evaluted answer: ", exp)
    elif choice=='sin':
        val=eval(input("Value(Sin_): "))
        a= math.radians(val)
        print("Result ", math.sin(a))
    elif choice=='cos':
        val=eval(input("Value(Cos_): "))
        a = math.radians(val)
        print("result: ",math.cos(a))
    elif choice=='tan':
        val=eval(input("Value(Tan_): "))
        a = math.radians(val)
        print("Result ", math.tan(a))
    elif choice=='rad':
        val=eval(input("Radian: "))
        print("Degree", math.degrees(val))
    elif choice=='deg':
        val=eval(input("Degree: "))
        print("Radian", math.radians(val))
    elif choice=='exit':
        break
    else:
        print("\nInvalid Input!")
print("\nThank You :)")