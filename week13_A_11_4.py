# week13_A_11_4.py
# id:202444001
# name:yu seungwon

import datetime as dt
import os
from week13_A_room import Room2 as Room
from week13_A_room import TimeStamp
import random

timeformat = "%Y-%m-%d %H:%M:%S"
mypath = "c:\\room2_2400001"

# A1_10~ A1_99 일반호실1층_방번호
# S2_10~ S2_99
def gen_room_number():
    room_type = ['A','S']
    room_level = f'{random.randint(1,8)}' #1-8사이의 인트값 출력
    room_num = f'{random.randrange(10,100)}' # 10부터 99까지 출력 (10,100,2) = 2step마다
    room_choice_type = random.choice(room_type) # random.choice(순번을가진그시기) 중에서 하나 꼽음
    return f'{room_choice_type}{room_level}_{room_num}'

def gen_intime():
    return dt.datetime.now() - dt.timedelta(hours=random.randint(0,8),minutes=random.randint(0,60)) # day, week, hours, minutes, seconds 따로 알아보기

def gen_outtime():
    return dt.datetime.now() + dt.timedelta(hours=random.randint(1,48),minutes=random.randint(0,60))

if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    rooms = []

    members = os.listdir(mypath) # mypath의 모든 파일,폴더명을 가져옴
    for member in members:
        member_fullname = os.path.join(mypath, member)
        if os.path.isFile(member_fullname):
            file_ext = os.path.splitext(member) #확장자 명으로 나눔 111.ex.txt = [111.ex, .txt]
            if len(file_ext) == 2 and file_ext[-1] == ".txt":
                number =file_ext[0].strip()
                room = Room(number)
                #rooms[number] =[]
                rooms.append(room)
                with open(member_fullname, 'r', encoding="utf-8") as f:
                    for line in f:
                        split_data = line.strip().split("|")
                        if len(split_data) == 2:
                            intime = dt.strptime(split_data[0].strip(), timeformat)
                            if split_data[1].strip():
                                outtime = dt.strptime(split_data[1].strip(), timeformat)
                            else:
                                outtime = None
                            room.add_timestamp(intime,outtime) # ? 리스트에 추가한 인스턴스를 수정할수 있나?
            

    while True:
        room = input("강의실 호수:").strip()
        if not room:
            break
        search_room = [room_info for room_info in rooms if room_info.number == room ]

        if not search_room:
            room_info = Room(room)
            rooms.append(room_info)
        else:
            room_info = search_room[0]
            for timestamp in rooms_info.history:
                if timestamp.is_rent():
                    #반납 코드
                    print("대여중")
                    continue

        while True:
            try:
                starttime = input("시작시간:").strip()
                if starttime:
                    starttime = dt.datetime.strptime(starttime, timeformat)
                    break
                else:
                    starttime = gen_intime()
            except:
                starttime = gen_intime()
                break

        while True:
            try:
                stoptime = input("종료시간:").strip()
                if not stoptime:
                    stoptime = None
                else:
                    stoptime = dt.datetime.strptime(stoptime, timeformat)
                break
            except:
                pass

        #rent_info = {"in" : starttime, "out": stoptime}
        #rooms[room].append(rent_info)
        room_info.add_timestamp(starttime,stoptime)

        fullfile = os.path.join(mypath, room + ".txt")

        with open(fullfile, 'a', encoding = "utf-8") as f:
            intime = dt.strftime(starttime, timeformat)
            if stoptime != None:
                outtime = dt.strftime(stoptime, timeformat)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|") # 만약 반납을 구현한다면 |뒤에 바로 어펜드 할수 있도로 줄바꿈 하지 않음
            
    for room_info in rooms:
        print(room_info.number)
        for timestamp in room_info.history:
            print(timestamp.intime, timestamp.outtime)
            print(timestapm.diff_seconds())

   
