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

    menu = input('메뉴를 선택하세요: ').strip().upper()
    return menu

def init_member():
    print("[회원 정보 등록]")
    id = input("아이디: ").strip().upper()
    for member in member_list:
        if member.id == id:
            print("이미 존재하는 아이디입니다.")
            return
    sex = input("성별(M/F): ").strip().upper()
    if sex != "M" and sex != "F":
        print("성별은 M 또는 F만 가능합니다.")
        return
    height = input("신장(m): ").strip()
    try:
        height = float(height)
    except Exception:
        print("신장은 숫자만 입력 가능합니다.")
        return
    weight = input("체중(kg): ").strip()
    try:
        weight = float(weight)
    except Exception:
        print("체중은 숫자만 입력 가능합니다.")
        return
    
    return Member(id, sex, weight, height)

while True:
    select = select_menu()
    if select == 'A':
        pass
    elif select == 'B':
        member = init_member()
        if member:
            member_list.append(member)
    elif select == 'C':
        pass
    elif select == 'D':
        pass
    elif select == 'Q':
        pass
        break
    
print("프로그램을 종료합니다")
