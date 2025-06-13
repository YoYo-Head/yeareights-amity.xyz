import json
import request as scp

t = open('timetable.txt', 'r', encoding='utf-8')

with open('reTimetable.txt', 'w', encoding='utf-8') as Re:
    Re.write("Reformed Timetable!\n")


n = open('reTimetable.txt', 'a', encoding='utf-8')

lines = t.readlines()

t.close()


wordedDays = [day + ':' for day in scp.days]

# Where the first line is that contains the period info
starterLine = 5

totalDays = 10
periods = 8

remove = [' Week A -', ' Week B -']

# For daily periods, its spread out every 12 lines
spreadLined = 12

for days in range(totalDays):
    starter = starterLine + days
    line = lines[starter - 1]

    if days <= 4:
        week = 'A'
    elif days >= 5:
        week = 'B'
    else:
        week = 'Unknown'

    for totalsDays in wordedDays:
        if totalsDays in line:
            day = totalsDays
            n.write(f"\n === Week {week} | {day} === \n")

    for period in range(periods):
        line = lines[starter - 1 + spreadLined * (period)]

        if ":" in line:
            finalLine = line.split(":", 1)[1].strip()
        else:
            finalLine = line.strip()

        n.write(f"Period {period + 1}: {finalLine}\n")
    
n.close()