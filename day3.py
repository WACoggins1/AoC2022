with open('rucksack.txt', 'r') as input:
    sacks = input.read().split('\n')

def p1(sacks):
    sumPrio1 = 0
    for i in sacks:
        common = (set(i[:len(i)//2]) & set(i[len(i)//2:])).pop()
        sumPrio1 += ord(common) - (96 if common.islower() else 38)
    return sumPrio1

def p2(sacks):
    sumPrio2 = 0
    for i in range(0,len(sacks),3):
        common = (set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2])).pop()
        sumPrio2 += ord(common) - (96 if common.islower() else 38)
    return sumPrio2


print("Part 1: ", p1(sacks))
print("Part 2: ", p2(sacks))






