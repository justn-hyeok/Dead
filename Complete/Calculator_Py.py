import sys
import ast
import operator

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

# 사칙연산 계산기 함수
def calculate_expression(expression):
    # 연산자 정의
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    
    # 표현식 파싱
    def eval_node(node):
        if isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            return operators[type(node.op).__name__](left, right)
        elif isinstance(node, ast.Num):
            return node.n
        else:
            raise TypeError(node)

    # 표현식의 AST 생성
    try:
        tree = ast.parse(expression, mode='eval')
        return eval_node(tree.body)
    except ZeroDivisionError:
        return "오류! 0으로 나눌 수 없습니다."
    except Exception as e:
        return f"오류: {e}"

# 사칙연산을 수행하는 함수
def arithmetic_operations():
    expr = input("계산할 수식을 입력하세요 (예: 1 + 2 * 3 / 4): ")
    try:
        result = eval(expr)  # 수식을 계산
        print(f"결과: {result}")
    except Exception as e:
        print(f"오류 발생: {e}")

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

if __name__ == "__main__":
    main()
