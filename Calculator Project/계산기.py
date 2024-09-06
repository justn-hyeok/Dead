import math

# 메인 메뉴
def main_menu():
    print("""
=======================
메인 메뉴
-----------------------
1 | 계산기
2 | 삼각함수
0 | 프로그램 종료하기
=======================
사용할 기능을 선택해주세요: """, end="")

def calculator_menu():
    print("""
=======================
계산기 메뉴
-----------------------
1 | 사칙 연산
2 | 여러가지 나눗셈
3 | 제곱과 제곱근
b | 뒤로 가기
=======================
사용할 기능을 선택해주세요: """, end="")

def sachickyeonsan_menu():
    print("""
=======================
사칙 연산 메뉴
-----------------------
1 | +
2 | -
3 | *
4 | /
b | 뒤로 가기
=======================
사용할 기능을 선택해주세요: """, end="")

def many_divide_menu():
    print("""
=======================
여러가지 나눗셈 메뉴
-----------------------
1 | 몫
2 | 나머지
b | 뒤로 가기
=======================
사용할 기능을 선택해주세요: """, end="")

def jegob_menu():
    print("""
=======================
제곱과 제곱근 메뉴
-----------------------
1 | 제곱
2 | 제곱근
b | 뒤로 가기
=======================
사용할 기능을 선택해주세요: """, end="")

# 삼각함수 메뉴
def trig_menu():
    print("""
=======================
삼각함수 메뉴
-----------------------
1 | sin
2 | cos
3 | tan
b | 뒤로 가기
=======================
사용할 기능을 선택해주세요: """, end="")

# 기본 연산
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0 으로 나눌 수 없습니다.")
    return a / b

# 여러가지 나눗셈
def quotient(a, b):  # 몫
    if b == 0:
        raise ValueError("0 으로 나눌 수 없습니다.")
    return a // b

def remainder(a, b):  # 나머지
    if b == 0:
        raise ValueError("0 으로 나눌 수 없습니다.")
    return a % b

# 제곱과 제곱근
def power(base, exp):
    return base ** exp

def root(a):
    if a < 0:
        raise ValueError("음수의 제곱근은 허용되지 않습니다.")
    return math.sqrt(a)

# 삼각함수 계산
def trig_sin(angle):
    return math.sin(math.radians(angle))

def trig_cos(angle):
    return math.cos(math.radians(angle))

def trig_tan(angle):
    return math.tan(math.radians(angle))

# 계산기 기능
def calculator():
    while True:
        calculator_menu()
        menu_choice = input().strip().lower()
        
        if menu_choice == '1':
            while True:
                sachickyeonsan_menu()
                op = input().strip()
                
                if op == '1':
                    a = float(input("첫 번째 숫자를 입력하세요: "))
                    b = float(input("두 번째 숫자를 입력하세요: "))
                    print(f"결과: {add(a, b)}")
                elif op == '2':
                    a = float(input("첫 번째 숫자를 입력하세요: "))
                    b = float(input("두 번째 숫자를 입력하세요: "))
                    print(f"결과: {subtract(a, b)}")
                elif op == '3':
                    a = float(input("첫 번째 숫자를 입력하세요: "))
                    b = float(input("두 번째 숫자를 입력하세요: "))
                    print(f"결과: {multiply(a, b)}")
                elif op == '4':
                    a = float(input("첫 번째 숫자를 입력하세요: "))
                    b = float(input("두 번째 숫자를 입력하세요: "))
                    try:
                        print(f"결과: {divide(a, b)}")
                    except ValueError as e:
                        print(e)
                elif op == 'b':
                    break
                else:
                    print("잘못된 선택입니다. 다시 시도해주세요.")
        
        elif menu_choice == '2':
            while True:
                many_divide_menu()
                op = input().strip()
                
                if op == '1':
                    a = int(input("첫 번째 숫자를 입력하세요: "))
                    b = int(input("두 번째 숫자를 입력하세요: "))
                    try:
                        print(f"결과: {quotient(a, b)}")
                    except ValueError as e:
                        print(e)
                elif op == '2':
                    a = int(input("첫 번째 숫자를 입력하세요: "))
                    b = int(input("두 번째 숫자를 입력하세요: "))
                    try:
                        print(f"결과: {remainder(a, b)}")
                    except ValueError as e:
                        print(e)
                elif op == 'b':
                    break
                else:
                    print("잘못된 선택입니다. 다시 시도해주세요.")

        elif menu_choice == '3':
            while True:
                jegob_menu()
                op = input().strip()
                
                if op == '1':
                    base = float(input("밑을 입력하세요: "))
                    exp = float(input("지수를 입력하세요: "))
                    print(f"결과: {power(base, exp)}")
                elif op == '2':
                    a = float(input("숫자를 입력하세요: "))
                    try:
                        print(f"결과: {root(a)}")
                    except ValueError as e:
                        print(e)
                elif op == 'b':
                    break
                else:
                    print("잘못된 선택입니다. 다시 시도해주세요.")

        elif menu_choice == 'b':
            break
        
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

# 삼각함수 기능 추가
def trigonometry():
    while True:
        trig_menu()
        trig_choice = input().strip().lower()

        if trig_choice == '1':
            angle = float(input("각도를 입력하세요(도 단위): "))
            print(f"sin({angle}) = {trig_sin(angle)}")
        elif trig_choice == '2':
            angle = float(input("각도를 입력하세요(도 단위): "))
            print(f"cos({angle}) = {trig_cos(angle)}")
        elif trig_choice == '3':
            angle = float(input("각도를 입력하세요(도 단위): "))
            print(f"tan({angle}) = {trig_tan(angle)}")
        elif trig_choice == 'b':
            break
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

def main():
    while True:
        main_menu()
        menu_choice = input().strip()
        
        if menu_choice == '1':
            calculator()
        elif menu_choice == '2':
            trigonometry()  # 삼각함수 기능 추가
        elif menu_choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
