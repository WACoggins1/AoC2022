#noop takes 1 cycle and has no effect
#addx value takes two cycles and changes X by value (can be negative).
#X starts with a value of 1, so addx 3 makes X have a value of 4 in two cycles, (X is still 1 during the 2nd cycle and only updates after)
#X is still 1 during the third cycle, then updates to 4.
#during the 20th cycle and every 40 after that, the signal strength is multipled by the register value. i.e,
#if X has a value of 21 during the 20th cycle, the signal strength is 20*21 = 420.

#add up the signal strengths at the 20th, 60th, 100th, 140th, 180th, and 220th cycle.

with open('day10.txt', 'r') as f:

    data = [line.rstrip() for line in f.readlines()]

X = 1
cycle = 0
pixels = list("."*40*6)




def p1():
    X = 1
    cycle = 0
    signalS = {}
    for line in data:
        line = line.split()

    #one cycle for noop
        if line[0] == "noop":
            cycle += 1
            signalS[cycle] = X*cycle

    #two cycles for addx
        elif line[0] == 'addx':
            cycle +=1
            signalS[cycle] = X*cycle

            cycle +=1
            signalS[cycle] = X*cycle

            X += int(line[1])

    totalSum = sum(signalS.get(i,0) for i in range(20,221,40))
    print("Part 1:", totalSum)


def update_pixels(X, cycle, pixels):


    pos = (cycle-1)%40

    if pos in {X -1, X, X+1}:
        pixels[cycle - 1] = "#"


for line in data:
    line = line.split()


    if line[0] == "noop":
        cycle += 1
        update_pixels(X, cycle, pixels)


    elif line[0] == 'addx':
        cycle +=1
        update_pixels(X,cycle,pixels)

        cycle +=1
        update_pixels(X,cycle,pixels)

        X += int(line[1])


p1()

for i in range(0,201,40):
    print("".join(pixels[i:i+40]))
