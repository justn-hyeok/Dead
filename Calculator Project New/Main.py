from calculator import calculator
# from trigonometry import trigonometry

# 메인 메뉴 출력 함수
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

def main():
    while True:
        main_menu()
        menu_choice = input().strip()
        
        if menu_choice == '1':
            calculator()
        elif menu_choice == '2':
            # trigonometry()
            print("곧 추가 예정")
        elif menu_choice == '0':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")

main()

# 접을래 그냥 ㅜㅜ