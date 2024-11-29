import os
from test_class import Member

member_list = []

dir_path = "./202444001" # 맥 경로 / 과제 요구 경로 = c:/학번

def return_paths(): # fixit 회원 정보가 없으면 경로 반환 안됨
    path_list = []
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for file in os.listdir(dir_path):
        file_ext = os.path.splitext(file)
        if len(file_ext) == 2 and file_ext[-1] == ".txt":
            path_list.append(os.path.join(dir_path, file))
    return path_list

def make_path(file_name):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    if not os.path.isfile(os.path.join(dir_path, file_name)):
        with open(os.path.join(dir_path, file_name), "w", encoding="utf-8") as f:
            pass
    return os.path.join(dir_path, file_name)

def read_file():
    paths = return_paths()
    invalid_count = 0
    height_list = []
    weight_list = []
    if len(paths) == 0:
        print("\n복원할 회원 정보가 없습니다.\n")
        return
    if len(member_list) > 0:
        print("\n기존 회원 정보가 있어 복원하지 않습니다.\n")
        return
    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                data = line.split(",")
                if len(data) != 2:
                    invalid_count += 1
                    continue
                height, weight = data
                id = os.path.splitext(path)[0].split("/")[-1].split("_")[0]
                id = id.strip().upper()
                sex = os.path.splitext(path)[0].split("/")[-1].split("_")[1]
                sex = sex.strip().upper()
                if sex != "M" and sex != "F":
                    invalid_count += 1
                    continue
                try:
                    height_list.append(float(height))
                    weight_list.append(float(weight))
                except Exception:
                    invalid_count += 1
                    continue
                if height_list[-1] <= 0 or weight_list[-1] <= 0:
                    invalid_count += 1
                    continue
            member = Member(id, sex, height_list, weight_list)
            member_list.append(member)
            height_list = []
            weight_list = []
    print(f"\n{len(member_list)}명의 회원 정보를 복원하였습니다.\n")
    print(f"유효하지 않은 회원 정보는 {invalid_count}건입니다.\n")
    return

def save_file():
    if len(member_list) == 0:
        print("\n저장할 회원 정보가 없습니다.\n")
        return
    for member in member_list:
        path = make_path(f"{member.id}_{member.sex}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(member.return_value())
    print(f"\n{len(member_list)}명의 회원 정보를 저장하였습니다.\n")
    
def select_menu():
    print('#' * 20)
    print('A. 기존자료복원')
    print('B. 회원 등록')
    print('C. 정보수정')
    print('D. 전체 조회')
    print('Q. 종료 및 회원 정보 저장')
    print('#' * 20)

    menu = input('메뉴를 선택하세요: ').strip().upper()
    if menu not in ['A', 'B', 'C', 'D', 'Q']:
        print("\n잘못된 메뉴를 선택하였습니다.\n")
        return
    return menu

def init_member():
    print("\n[회원 정보 등록]")
    id = input("아이디: ").strip().upper()
    if id == "":
        print("\n아이디는 필수 입력 사항입니다.\n")
        return
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
        if height <= 0:
            print("\n신장은 0보다 커야 합니다.\n")
            return
    except Exception:
        print("\n신장은 숫자만 입력 가능합니다.\n")
        return
    weight = input("체중(kg): ").strip()
    try:
        weight = float(weight)
        if weight <= 0:
            print("\n체중은 0보다 커야 합니다.\n")
            return
    except Exception:
        print("\n체중은 숫자만 입력 가능합니다.\n")
        return
    height_list = [height]
    weight_list = [weight]
    
    return Member(id, sex, height_list, weight_list)

def edit_member():
    if len(member_list) == 0:
        print("\n등록된 회원이 없습니다.\n")
        return
    else:
        print("\n[회원 정보 수정]")
        id = input("아이디: ").strip().upper()
        found = False
        for member in member_list:
            if member.id == id:
                found = True
                print(f"현재 신장 : {member.height[-1]:.1f}m")
                edit_height = input("수정 신장(m): ")
                if edit_height == "" or edit_height == None:
                    pass
                else:
                    try:
                        member.height.append(float(edit_height))
                    except Exception:
                        print("\n신장은 숫자만 입력 가능합니다.\n")
                        return
                print(f"현재 체중 : {member.weight[-1]:.1f}kg")
                edit_weight = input("수정 체중(kg): ")
                if edit_weight == "" or edit_weight == None:
                    pass
                else:
                    try:
                        member.weight.append(float(edit_weight))
                    except Exception:
                        print("\n체중은 숫자만 입력 가능합니다.\n")
                        return
                print(f"BMI : {member.calc_bmi():.2f}")
                return
        if not found:
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
                print(f"[{i+1}] 아이디:{member.id} 신장:{member.height[-1]:.2f} 체중:{member.weight[-1]:.2f} BMI:{member.calc_bmi():.2f}")
                print(f"도표: {'*' * int(member.calc_bmi())}")
                
        if len(female_members) > 0:
            print("[여성]") 
            for i, member in enumerate(female_members):
                print(f"[{i+1}] 아이디:{member.id} 신장:{member.height[-1]:.2f} 체중:{member.weight[-1]:.2f} BMI:{member.calc_bmi():.2f}")
                print(f"도표: {'*' * int(member.calc_bmi())}")
        
        print("=" * 20)
        print(f"총 {len(member_list)}명의 정보입니다.")
        
while True:
    select = select_menu()
    if select == 'A':
        read_file()
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
        save_file()
        break
    
print("프로그램을 종료합니다")
