
filehandle = open('0022_names.txt')

for line in filehandle:
    names = line.split('","')


names[0] = names[0].replace('"','')
names[-1] = names[-1].replace('"','')

names = sorted(names)


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

points = dict()
for i in alphabet:
    points[i] = alphabet.index(i) + 1 

def namePoint(name):
    sum = 0
    for letter in name:
        sum += points[letter]

    return sum

result = 0
for name in names:
    result += namePoint(name) * (names.index(name) + 1)

print(result)