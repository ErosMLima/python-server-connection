num = int(input("how many numbers ?"))
total_sum = 0

for n in range (num):
    numbers = float(input("Enter any number"))
    total_sum += numbers

avg = total_sum / num

print('The Average number is?'. avg)