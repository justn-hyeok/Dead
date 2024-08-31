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

def calculator():
    print("사용 가능한 연산: +, -, *, /")
    
    # 사용자 입력 받기
    operation = input("연산 기호를 입력하세요: ")
    
    if operation in ('+', '-', '*', '/'):
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
        except ValueError:
            print("유효한 숫자를 입력해 주세요.")
            return

        if operation == '+':
            print("결과:", add(num1, num2))
        elif operation == '-':
            print("결과:", subtract(num1, num2))
        elif operation == '*':
            print("결과:", multiply(num1, num2))
        elif operation == '/':
            print("결과:", divide(num1, num2))
    else:
        print("유효하지 않은 연산 기호입니다. +, -, *, / 중 하나를 입력해 주세요.")

calculator()

# 빡쳐서 아ㅣ것만 만들어써