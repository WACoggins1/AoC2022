text = open("day6.txt").read().strip()

#count by groups of 4
def p1():
    p1Counter = 0
    for i in range(len(text)-4):
        p1Counter +=1
        if len(set(text[i:i+4])) == 4:
            print("Part 1:", p1Counter + 3)
            break

#count by groups of 14
def p2():
    p2Counter = 0
    for i in range(len(text) - 14):
        p2Counter +=1
        if len(set(text[i:i+14])) == 14:
            print("Part 2:", p2Counter + 13)
            break

p1()
p2()
