a = True
b = False

c = "Ninjas"
type(b)
print(type(b))


c1 = a > 10
c2 = b > 10
r1 = c1 and c2
r2 = c1 or c2
r3 = not(c1)
print(r1)
print(r2)
print(r3)


animals = ['dog', 'cat', 'bird']
for index, animal in enumerate(animals):
    print(f"{index}: {animal}")

for i in range(1, -10, -1):  # Loops from 1 to 9, stepping by 2
    print(i)