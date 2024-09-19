# 딕셔너리 활용 프로젝트
# 일상 생활 속 다양한 데이터를 딕셔너리를 이용해 처리하는 프로그램을 작성해 봅시다.
# 예) Todo list, 전화번호 프로그램, 단어장 프로그램 등

# 8/28 (수) 
# 파이썬 미니 프로젝트

# 상품 재고 관리 시스템
# 가게의 상품 재고를 관리하는 프로그램입니다. 상품명을 키로, 재고 수량을 값으로 저장합니다.
# GPT로 코드 이쁘게 바꿨스빈다 ㅎㅎ

inventory = {
    "지식" : 0,
    "코딩실력" : 0,
    "asdf" : 1,
    "황준혁" : 1,
    "바나나" : 5,
    "사과" : 10,
    "재고" : 100
}

# 상품 추가 함수
def add_item(item, quantity):
    inventory[item] = inventory.get(item, 0) + quantity
    print(f"{item}이(가) {quantity}개 추가되었습니다.")

# 상품 수정 함수
def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
        print(f"{item}의 재고가 {quantity}개로 수정되었습니다.")
    else:
        print("상품이 존재하지 않습니다.")

# 재고 확인 함수
def check_stock(item):
    return inventory.get(item, "상품이 없습니다.")

# 재고가 없는 상품 목록 함수
def out_of_stock_items():
    return [item for item, quantity in inventory.items() if quantity == 0]

# 사용자 메뉴
def display_menu():
    print("\n==== 재고 관리 시스템 ====")
    print("1. 상품 추가")
    print("2. 상품 수정")
    print("3. 재고 확인")
    print("4. 재고가 없는 상품 확인")
    print("5. 종료")
    print("========================")

# 프로그램 실행
try:
    while True:
        display_menu()
        choice = input("원하는 작업을 선택하세요: ")

        if choice == "1":
            item = input("추가할 상품명을 입력하세요: ")
            quantity = int(input("추가할 수량을 입력하세요: "))
            add_item(item, quantity)

        elif choice == "2":
            item = input("수정할 상품명을 입력하세요: ")
            quantity = int(input("수정할 수량을 입력하세요: "))
            update_item(item, quantity)

        elif choice == "3":
            item = input("확인할 상품명을 입력하세요: ")
            print(f"{item}의 재고: {check_stock(item)}")

        elif choice == "4":
            out_of_stock = out_of_stock_items()
            if out_of_stock:
                print("재고가 없는 상품들:", ", ".join(out_of_stock))
            else:
                print("재고가 없는 상품이 없습니다.")

        elif choice == "5":
            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 번호를 선택하세요.")
except KeyboardInterrupt:
    print("\n프로그램이 사용자에 의해 중단되었습니다.")