from test_class import Member

member_list = []

def select_menu():
    print('#' * 20)
    print('A. 기존자료복원')
    print('B. 회원 등록')
    print('C. 정보수정')
    print('D. 전체 조회')
    print('Q. 종료 및 회원 정보 저장')
    print('#' * 20)

    menu = int(input('메뉴를 선택하세요: '))
    return menu

while True:
    select = select_menu()
    if select == 'A':
        pass
    elif select == 'B':
        pass
    elif select == 'C':
        pass
    elif select == 'D':
        pass
    elif select == 'Q':
        pass
        break
    
print("프로그램을 종료합니다")
