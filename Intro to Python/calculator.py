class Calculator:
    def __init__(self):
        self.operations = {
            1: self.addition,
            2: self.subtraction,
            3: self.multiplication,
            4: self.division
        }

    def addition(self, x, y):
        return x + y
    
    def subtraction(self, x, y):
        return x - y
    
    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def main(self):
        while True:    
            print("""Operations:
                (1)Addition
                (2)Subtraction
                (3)Multiplication
                (4)Division
                (5)Quit""")
            operators = getint("Enter operation (1/2/3/4/5): ")
            if operators not in (1,2,3,4,5):
                print("Invalid input.")
                continue
            if operators == 5:
                print("Bye!")
                break
            num1 = getint("Enter first number: ")
            num2 = getint("Enter second number: ")
            while operators == 4 and num2 == 0:
                print("Zero is not a valid divisor.")
                num2 = getint("Please enter a valid second number: ")
            result = self.operations[operators](num1, num2)
            print(f"Answer: {result}")
def getint(x):
    while True:
        try:
            user_input = int(input(x))
        except ValueError:
            print("Invalid input.")
        else:
            return user_input
        
calculator = Calculator()
if __name__ == '__main__':
    calculator.main()