'''print(f'NameError - {type(NameError)}- {issubclass(NameError,BaseException)}')'''
'''try:
    print('Start code')
    print(error)
    print('No errors')

except:
    print('We have an error')

print('Code after capsule')'''
'''try:
    print(error)
except NameError:
    print('U have NameError')

try:
    print(10 / 0)
except ZeroDivisionError:
    print('ZeroDivisionError')'''
#ValueError
#ZeroDivisionError
'''try:
    a=int(input('1st number'))
    b=int(input('2nd number'))
    c = a / b
    print(c)
except ValueError:
    print('Not correct Value')
except ZeroDivisionError:
    print('You can`t divide by zero')
'''
def calculator():
    while True:
        try:
            num1 = float(input("1st number: "))
            num2 = float(input("2nd number: "))
            operator = input("Enter operator (+, -, *, /): ")

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                print("Wrong operator! Enter +, -, *, or /.")
                continue

            print("Result: ", result)
            break

        except ValueError:
            print("Incorrect input! Enter numbers.")
        except ZeroDivisionError:
            print('You can`t divide by zero')

calculator()