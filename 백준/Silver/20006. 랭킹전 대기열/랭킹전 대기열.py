p, m = map(int, input().split())
rooms = []

for player in range(p):
    level, nickname = input().split()
    level = int(level)

    if len(rooms) == 0:
        rooms.append([level])
        rooms[-1].append((level, nickname))
        continue
    
    find_room = False
    for room in rooms:
        if room[0]-10 <= level and room[0]+10 >= level:   
            if len(room[1:]) < m:
                room.append((level, nickname))
                find_room = True
                break

    if not find_room:
        rooms.append([level])
        rooms[-1].append((level, nickname))
        continue
    # rooms.append([level])
    # rooms[-1].append((level, nickname))

for room in rooms:
    if len(room[1:]) == m:
        print("Started!")
    else:
        print("Waiting!")

    players = room[1:]
    players.sort(key = lambda x : x[1])
    for player in players:
        print(*player)