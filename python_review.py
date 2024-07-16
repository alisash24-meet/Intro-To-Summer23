import random
temperatures = []

for i in range(7):
	n = random.randint(26,41)
	temperatures.append(n)
print(temperatures)

days_of_the_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
good_days_count = []


for i in range(7): 
	if temperatures[i] % 2 == 0:
		good_days_count.append(days_of_the_week[i])


print(good_days_count)

high = 0
low = 0

for i in range(7):
	if temperatures[i] > temperatures[high]:
		high = i
	if temperatures[i] < temperatures[low]:
		low = i

highest_temp = temperatures[high]
highest_temp_day = days_of_the_week[high]
lowest_temp = temperatures[low]
lowest_temp_day = days_of_the_week[low]

average = 0

for i in temperatures:
	average += i

average /= 7

above_avg = []

for i in temperatures:
	if i > average:
		above_avg.append(i)


print("The Weather Report:")
for i in range(7):
	print("  ", days_of_the_week[i], ":", temperatures[i])
	print("*")
	print("*")
	print("  ", "Shelly had 4 good days")
	print("*")
	print("*")
	print("  ", highest_temp_day, ":", highest_temp)
	print("  ", lowest_temp_day, ":", lowest_temp)


sorted_list = []
for i in range(7):
	for j in range(i, 7):
		if temperatures[j] < temperatures[i]:
			temp_var = temperatures[i]
			temperatures[i] = temperatures[j]
			temperatures[j] = temp_var

print(sorted_list)