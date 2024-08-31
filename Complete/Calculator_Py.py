def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "나누기 0은 쓰면 안되요.."

def perform_operation(x, y, operation):
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return subtract(x, y)
    elif operation == '*':
        return multiply(x, y)
    elif operation == '/':
        return divide(x, y)
    else:
        return "유효하지 않은 연산 기호입니다. +, -, *, / 중 하나를 입력해 주세요."

def print_menu():
    print("\n====================")
    print("      계산기 메뉴      ")
    print("====================")
    print("1. 사칙연산")
    print("2. 종료")
    print("====================")

def print_operations_menu():
    print("\n====================")
    print("   사칙연산 메뉴   ")
    print("====================")
    print("1. 덧셈 (+)")
    print("2. 뺄셈 (-)")
    print("3. 곱셈 (*)")
    print("4. 나눗셈 (/)")
    print("뒤로 가려면 'back'을 입력하세요")
    print("====================")

def calculator():
    while True:
        print_menu()
        choice = input("메뉴를 선택하세요 (1/2): ").strip().lower()

        if choice == '2':
            print("\n계산기를 종료합니다. 감사합니다!")
            break
        elif choice == '1':
            while True:
                print_operations_menu()
                operation_choice = input("원하는 연산을 선택하세요 (1/2/3/4) 또는 뒤로 가려면 'back': ").strip().lower()

                if operation_choice == 'back':
                    break

                if operation_choice in ('1', '2', '3', '4'):
                    operation_dict = {'1': '+', '2': '-', '3': '*', '4': '/'}
                    operation = operation_dict[operation_choice]

                    try:
                        num1 = float(input("첫 번째 숫자를 입력하세요: "))
                        num2 = float(input("두 번째 숫자를 입력하세요: "))
                    except ValueError:
                        print("유효한 숫자를 입력해 주세요.")
                        continue

                    result = perform_operation(num1, num2, operation)
                    print("결과:", result)
                else:
                    print("유효하지 않은 선택입니다. 1, 2, 3, 4 중 하나를 입력해 주세요.")
        else:
            print("유효하지 않은 선택입니다. 1 또는 2 중 하나를 입력해 주세요.")

calculator()
