#user input
x = input('Input a number: ')

#normal variables
maxNum = int(x)
total = 0

for n in range(maxNum+1):
  total += n

print(f"The sum of all numbers from 0 to {maxNum} is {total}")
  