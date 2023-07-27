owl_numbers = []

for number in range(0,10000):

    digits = str(number)
    sum_of_digits = sum([int(digit) for digit in digits])

this_total = number + sum_of_digits
if this_total not in owl_numbers:
    owl_numbers.append(this_total)

print(owl_numbers)