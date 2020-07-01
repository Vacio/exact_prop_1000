x = range(10000)
y = []
z = []

## convert numbers to 4 digit strings, save in y
for n in x:
    y.append("{0:0=4d}".format(n))

## if a pair exists in string, save to z
for i in y:
    if i[0] == i[1] or i[0] == i[2] or i[0] == i[3] or i[1] == i[2] or i[1] == i[3] or i[2] == i[3]:
        continue
    else:
        z.append(i)

# print(z)
print(len(z))
