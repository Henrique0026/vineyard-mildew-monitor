temps = [8.5, 11.0, 13.5, 9.0, 15.2, 12.1, 7.8]

for t in temps:
    print(t)

count = 0
for t in temps:
    if t >= 10:
        count = count + 1

print(count)

total = 0
for t in temps:
    total = total + t

average = total / len(temps)
print(average)

highest = temps [0]
for t in temps:
    if t > highest:
        highest = t

print(highest)