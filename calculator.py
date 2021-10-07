import secret_logic


def ask():
    print("CALCULATOR APP")

    print("1. operand: ")
    text = input()

    while not secret_logic.is_numeric(text):
        print("try again")
        text = input()

    op1 = int(text)

    print("operator (+,-,*,/):")
    text = input()

    while not secret_logic.is_supported_operator(text):
        print("try again")
        text = input()

    operator = text

    print("2. operand: ")
    text = input()

    while not secret_logic.is_numeric(text):
        print("try again")
        text = input()

    op2 = int(text)

    return op1, operator, op2


result = secret_logic.calculate(*ask())
print("result: {}".format(result))
