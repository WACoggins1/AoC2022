import re, copy

input = open('day5.txt', 'r')

stack, moves = input.read().split("\n\n")

stacks = [[] for _ in range(10)]

#stacks are padded with spaces! so let's only look at position index 1 to get characters we need, and divide index by 4 to get approrpiate stack
#stacks are in reverse order
#THIS IS IMPORTANT - MUST PARSE THE INPUT CORRECTLY.
for line in stack.split("\n"):
    for i in range(0, len(line), 4):
        char = line[i:i+4]
        if '[' in char:
            stacks[i//4].append(char[1])

#reverse the order of the stacks
for i in range(len(stacks)):
    stacks[i] = stacks[i][::-1]

origStacks = copy.deepcopy(stacks)

def p1():
    #regex to parse the move values to integers named step, from, and to.
    for move in moves.split("\n"):
        step, fromI, toJ = [int(x) for x in re.findall(r'\d+', move)]
        fromI -= 1
        toJ -= 1

    #
        while step and stacks[fromI]:
            stacks[toJ].append(stacks[fromI].pop())
            step -= 1

    topRow = ""

    #create row of final blocks (read the "bottom")
    for block in stacks:
        if block:
            topRow += block[-1]

    print("Part 1: " + topRow)

#similar to part1, but now the blocks can be moved in unison, i.e., 3 blocks can be moved at once instead of 1 at a time.
def p2():
    for move in moves.split("\n"):
        step, fromI, toJ = [int(x) for x in re.findall(r'\d+', move)]
        fromI -= 1
        toJ -= 1
        n = len(origStacks[fromI])

        #this part will correct the stacks for part 2
        origStacks[toJ] += origStacks[fromI][n - step:n]
        origStacks[fromI] = origStacks[fromI][:n - step]

    #create another row of blocks
    topRow2 = ""
    for block in origStacks:
        if block:
            topRow2 += block[-1]
    print("Part 2: " + topRow2)

p1()
p2()
