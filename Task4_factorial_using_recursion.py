#program to find teh factorial of enterd number using recursion
def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

def main():
    while True:
        number=int(input("Enter a number:"))
        if number<0:
            print("Enter a valid positive number ") 
        else:
            result=factorial(number)
            print(f"Factorial of number:{result}")
            break

#call the main funtion
main()
