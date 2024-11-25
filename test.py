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
    print("\n[회원 정보 등록]")
    id = input("아이디: ").strip().upper()
    for member in member_list:
        if member.id == id:
            print("\n이미 존재하는 아이디입니다.\n")
            return
    sex = input("성별(M/F): ").strip().upper()
    if sex != "M" and sex != "F":
        print("\n성별은 M 또는 F만 가능합니다.\n")
        return
    height = input("신장(m): ").strip()
    try:
        height = float(height)
    except Exception:
        print("\n신장은 숫자만 입력 가능합니다.\n")
        return
    weight = input("체중(kg): ").strip()
    try:
        weight = float(weight)
    except Exception:
        print("\n체중은 숫자만 입력 가능합니다.\n")
        return
    
    return Member(id, sex, height, weight)

def edit_member():
    if len(member_list) == 0:
        print("\n등록된 회원이 없습니다.\n")
        return
    else:
        print("\n[회원 정보 수정]")
        id = input("아이디: ").strip().upper()
        for member in member_list:
            if member.id == id:
                print(f"현재 신장 : {member.height:.1f}m")
                edit_height = input("수정 신장(m): ")
                if edit_height == "" or edit_height == None:
                    pass
                else:
                    try:
                        member.height = float(edit_height)
                    except Exception:
                        print("\n신장은 숫자만 입력 가능합니다.\n")
                        return
                print(f"현재 체중 : {member.weight:.1f}kg")
                edit_weight = input("수정 체중(kg): ")
                if edit_weight == "" or edit_weight == None:
                    pass
                else:
                    try:
                        member.weight = float(edit_weight)
                    except Exception:
                        print("\n체중은 숫자만 입력 가능합니다.\n")
                        return
                print(f"BMI : {member.calc_bmi()}")
                return
            else:
                print("\n존재하지 않는 아이디입니다.\n")
                return
    
def print_member():
    if len(member_list) == 0:
        print("\n등록된 회원이 없습니다.\n")
        return
    else:
        print("[전체 상태 조회]")
        print("=" * 20)
        male_members = [m for m in member_list if m.sex == "M"]
        female_members = [m for m in member_list if m.sex == "F"]
        
        if len(male_members) > 0:
            print("[남성]")
            for i, member in enumerate(male_members):
                print(f"[{i}] 아이디:{member.id} 신장:{member.height:.2f} 체중:{member.weight:.2f} BMI:{member.calc_bmi():.2f}")
                print(f"도표: {'*' * int(member.calc_bmi())}")
                
        if len(female_members) > 0:
            print("[여성]") 
            for i, member in enumerate(female_members):
                print(f"[{i+1}] 아이디:{member.id} 신장:{member.height:.2f} 체중:{member.weight:.2f} BMI:{member.calc_bmi():.2f}")
                print(f"도표: {'*' * int(member.calc_bmi())}")
        
        print("=" * 20)
        print(f"총 {len(member_list)}명의 정보입니다.")
        
while True:
    select = select_menu()
    if select == 'A':
        pass
    elif select == 'B':
        member = init_member()
        if member:
            member_list.append(member)
            print(f"BMI : {member.calc_bmi():.2f}")
        
    elif select == 'C':
        edit_member()
    elif select == 'D':
        print_member()
    elif select == 'Q':
        pass
        break
    
    for member in member_list: # 테스트 코드 (필요한것 아님)
        print(member)
    
print("프로그램을 종료합니다")
