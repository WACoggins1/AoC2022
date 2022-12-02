elfTxt = open('elfCalories.txt', 'r')

calories = elfTxt.read().strip().split('\n\n')

elfCals = []

for elf in calories:
    meals = elf.split('\n')
    meals = [eval(i) for i in meals]
    elfCals.append(sum(meals))

ans1 = max(elfCals)
print("The elf carrying the most has", ans1)

elfCals = sorted(elfCals)
ans2 = sum(elfCals[-1:-4:-1])
print("The sum of the top 3 is", ans2)
