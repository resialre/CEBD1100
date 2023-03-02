import random
r_int = []

for n in range(100):
    r_int.append(random.randint(1,1000))

for y in r_int:
    print(y)

min_value = r_int[0]
max_value = 0
total_sum = 0

for n in r_int:
    # total_sum = total_sum + n
    total_sum += n

    if n > max_value:
        max_value = n;

    if n < min_value:
        min_value = n

print(max_value)
print(min(r_int))
print(min_value)

print("Average")
print(total_sum / len(r_int))