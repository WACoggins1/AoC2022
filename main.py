with open('day4.txt', 'r') as input:
    pairs = input.read().strip().split('\n')

    #convert the list into a new list that splits each element pair into distinct elements
    splitList = []
    for k in pairs:
        splitList.extend(k.split(','))

    # converts the list entries into their actual ranges. ,
    #i.e., '4-8' -> '[4, 5, 6, 7, 8]'
    convList = []
    for k in splitList:
        a,b = k.split('-')
        a,b, = int(a), int(b)
        result = list(range(a, b+1))
        convList.append(list((result)))

#function that checks to see if one of the ranges is contained fully within the other (in either direction)
#a.contains(b) or b.contains(a). If either is true, append a counter, otherwise do nothing.
def part1(convList):
    count = 0

    for i in range(0,len(convList),2):
        x = convList[i]
        y = convList[i+1]

        if (set(x).issubset(set(y))):
            count +=1
        if (set(y).issubset(set(x))):
            count +=1
        #removes double counted substs
        if (set(x) == set(y)):
            count -= 1
    return count

#check for any overlap over adjacent pairs
def part2(convList):
    overlap = 0
    for i in range(0,len(convList),2):
        x = convList[i]
        y = convList[i+1]

        #check for ANY overlap at all
        if any(elem in x for elem in y ) or any(elem in y for elem in x):
            overlap += 1
    return overlap

print("Part 1: ",part1(convList))
print("Part 2: ",part2(convList))
