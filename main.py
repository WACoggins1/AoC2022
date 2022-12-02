#read in .txt
elfTxt = open('elfCalories.txt', 'r')

#convert to something workable
calories = elfTxt.read().strip().split('\n\n')

elfCals = []

#get a list of sums
for elf in calories:
    meals = elf.split('\n')
    meals = [eval(i) for i in meals]
    elfCals.append(sum(meals))

#get the max
ans1 = max(elfCals)
print("The elf carrying the most has", ans1)

#order it and find the 3 largest sums.
elfCals = sorted(elfCals)
ans2 = sum(elfCals[-1:-4:-1])
print("The sum of the top 3 is", ans2)
