import random

class Hcode:
    def __init__(self):
        self.hcode_result = None
    def Hidecode(self, number):

        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 100)

        if operation == '+':
            self.hcode_result = number + operand
        elif operation == '-':
            self.hcode_result = number - operand
        elif operation == '*':
            self.hcode_result = number * operand
        elif operation == '/':
            self.hcode_result = number / operand

    def hcode_number(self):
        self.Hidecode(number)

    def get_hcode_result(self):
        return self.hcode_result

hcoder = Hcode()
number = random.randint(1, 50)
hcoder.hcode_number()

hcode_result = hcoder.get_hcode_result()
print('Result:', hcode_result)


