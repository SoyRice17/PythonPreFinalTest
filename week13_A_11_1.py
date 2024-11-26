# week13_A_11_1.py
# id:202444001
# name: 유승원

import datetime as dt
import os
import room as rm

time_format = "%Y-%m-%d %H:%M:%S"
my_path = "c:\\room1_2400001"
my_file = "list.txt"
full_path = os.path.join(my_path, my_file)

if __name__ == "__main__":
    if not os.path.isdir(my_path):
        os.mkdir(my_path)
    
    rooms = []
    # 파일이 있으면 읽어서 rooms에 복구한다.
    if os.path.isfile(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            for line in f:
                room, start_time, stop_time = line.strip().split("|")
                start_time = dt.datetime.strptime(start_time, time_format)
                if stop_time == "":
                    stop_time = None
                else:
                    stop_time = dt.datetime.strptime(stop_time, time_format)
                rooms.append(rm.Room1(room, start_time, stop_time))
                
    while True:
        room = input("강의실 호수:").strip()
        if not room:
            break
            
        while True:
            try:
                start_time = input("시작시간:").strip()
                if start_time:
                    start_time = dt.datetime.strptime(start_time, time_format)
                    break
            except:
                pass
                
        while True:
            try:
                stop_time = input("종료시간:").strip()
                if stop_time == "" or stop_time == None:
                    stop_time = None
                    break
                stop_time = dt.datetime.strptime(stop_time, time_format)
                break
            except:
                pass
        
        room_info = rm.Room1(room, start_time, stop_time)
        rooms.append(room_info)

    for room in rooms:
        print(room.num, room.start_time, room.stop_time)
        print(room.diff_seconds())
    
    with open(full_path, "w", encoding="utf-8") as f:
        for room in rooms:
            num = room.num
            start_time = dt.datetime.strftime(room.start_time, time_format)
            if room.stop_time == None or room.stop_time == "":
                stop_time = ""
            else:
                stop_time = dt.datetime.strftime(room.stop_time, time_format)
            f.write(f"{num}|{start_time}|{stop_time}\n")
