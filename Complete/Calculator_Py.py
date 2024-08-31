import sys

# 계산기 메뉴 출력 함수
def display_menu():
    print("\n========= 계산기 메뉴 ===========")
    print("1. 사칙연산 (+, -, *, /)")
    print("2. 거듭제곱")
    print("3. 제곱근")
    print("4. 루트")
    print("5. 소수 <-> 분수 변환기")
    print("6. 로그")
    print("7. 팩토리얼")
    print("8. 프로그램 종료")
    print("==============================")

# 사칙연산 메뉴 출력 함수
def arithmetic_operations_display():
    print("\n==== 사칙 연산 계산기 메뉴 ====")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 계산기 메뉴로 돌아가기")
    print("6. 프로그램 종료")
    print("==============================")

# 사칙 연산 수행 함수
def perform_arithmetic_operations():
    while True:
        arithmetic_operations_display()
        choice = input("사용할 연산을 선택하세요: ")

        if choice == '5':
            return  # 메뉴로 돌아가기 위해 함수 종료
        elif choice == '6':
            print("계산기를 종료합니다. 뿌슝!")
            sys.exit()  # 프로그램 종료
        elif choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("첫번째 숫자를 입력하시오: "))
                num2 = float(input("두번째 숫자를 입력하시오: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"{num1} / {num2} = {num1 / num2}")
                    else:
                        print("오류! 0으로 나눌 수 없습니다.")
            except ValueError:
                print("유효하지 않은 입력입니다. 숫자를 입력해 주세요.")
        else:
            print("입력 에러! 다시 입력해주세요!")

# 프로그램 실행
def main():
    while True:
        display_menu()
        menu_choice = input("메뉴를 선택하세요: ")

        if menu_choice == '1':
            perform_arithmetic_operations()
        elif menu_choice == '8':
            print("프로그램을 종료합니다. 안녕히 가세요!")
            sys.exit()  # 프로그램 종료
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

# 예시 실행
if __name__ == "__main__":
    main()
