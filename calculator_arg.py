import sys
import secret_logic


def print_usage_and_exit():
    print("Usage: <OPERAND> <OPERATOR> <OPERAND>")
    exit(-1)


def get_input():
    if len(sys.argv) != 4:
        print_usage_and_exit()

    if not secret_logic.is_numeric(sys.argv[1]):
        print_usage_and_exit()
    op1 = int(sys.argv[1])

    if not secret_logic.is_supported_operator(sys.argv[2]):
        print_usage_and_exit()
    l_operator = sys.argv[2]

    if not secret_logic.is_numeric(sys.argv[3]):
        print_usage_and_exit()
    op2 = int(sys.argv[3])

    return op1, l_operator, op2

op1, l_operator, op2 = get_input()
result = secret_logic.calculate(op1, l_operator, op2)
print(f"result: {result}")
exit(0)