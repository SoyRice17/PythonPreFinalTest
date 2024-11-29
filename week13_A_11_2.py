# week13_A_11_2.py
# id:202444001
# name:yu seungwon
# room2가 아닌 TimeStamp로만 코드를 적용해볼것
import datetime as dt
import os
from week13_A_room import Room2 as room
from week13_A_room import TimeStamp

timeformat = "%Y-%m-%d %H:%M:%S"

mypath = "c:\\room2_2400001"

def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.datetime.now()
    return (outtime - intime).total_seconds()


if __name__ == "__main__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)

    rooms = {}

    # rooms = {'roomNo' : [{intime: , outtime:}, {...}], 'roomNo2' : [{}] }
    # 파일이 있으면 읽어서 rooms에 복구한다.
    members = os.listdir(mypath) # mypath의 모든 파일,폴더명을 가져옴
    for member = members:
        member_fullname = os.path.join(mypath, member)
        if os.path.isFile(member_fullname):
            file_ext = os.path.splitext(member) #확장자 명으로 나눔 111.ex.txt = [111.ex, .txt]
            if len(file_ext) == 2 and file_ext[-1] == ".txt":
                number =file_ext[0].strip()
                rooms[number] =[]
                with open(member_fullname, 'r', encoding="utf-8") as f:
                    for line in f:
                        split_data = line.strip().split("|")
                        if len(split_data) == 2:
                            intime = dt.strptime(split_data[0].strip(), timeformat)
                            if split_data[1].strip():
                                outtime = dt.strptime(split_data[1].strip(), timeformat)
                            else:
                                outtime = None
                            rooms[number].append({"in": intime, "out": outtime})
            

    while True:
        room = input("강의실 호수:").strip()
        if not room:
            break
        if not room in rooms.keys():
            rooms[room] = []
        else:
            for history in rooms[room]:
                if history['out'] == None:
                    #반납 코드
                    print("대여중")
                    continue

        while True:
            try:
                starttime = input("시작시간:").strip()
                if starttime:
                    starttime = dt.datetime.strptime(starttime, timeformat)
                    break
            except:
                pass

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

        #room_info = {"num": room, "in": starttime, "out": stoptime}
        #rooms.append(room_info)
        rent_info = {"in" : starttime, "out": stoptime}
        rooms[room].append(rent_info)

        fullfile = os.path.join(mypath, room + ".txt")

        with open(fullfile, 'a', encoding = "utf-8") as f:
            intime = dt.strftime(starttime, timeformat)
            if stoptime != None:
                outtime = dt.strftime(stoptime, timeformat)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|") # 만약 반납을 구현한다면 |뒤에 바로 어펜드 할수 있도로 줄바꿈 하지 않음
            
    for room, history in rooms.items():
        print(room)
        for info in history:
            print(info["in"],info["out"])
            print(diff_seconds(info["in"], info["out"]))

   
