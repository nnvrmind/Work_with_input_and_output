with open("rosalind_majority_element.txt") as file:
    k, n = map(int, file.readline().split())
    arrays = []
    for line in file:
        arrays.append(list(map(int, line.split())))
print(arrays)

for i in range(len(arrays)):
    for j in range(len(arrays[i])):
        value = arrays[i][j]
        occurrences = arrays[i].count(arrays[i][j])
        if occurrences > (len(arrays[i]) / 2):
            print(value)
            break
    else:
        print("-1")