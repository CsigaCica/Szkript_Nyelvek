def is_numeric(text):
    return text.isnumeric()

def is_supported_operator(text):
        return text in ["+", "-", "*", "/"]

def calculate(op1, operator, op2):
        result = 0

        if operator == "+":
            result = op1 + op2

        elif operator == "-":
            result = op1 - op2

        elif operator == "*":
            result = op1 * op2

        if operator == "/":
            result = op1 / op2

        return result