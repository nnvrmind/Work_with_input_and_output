with open("rosalind_merge_two_sorted_arrays.txt") as file:
    n = file.readline().strip()
    array1 = list(map(int, file.readline().split()))
    m = file.readline().strip()
    array2 = list(map(int, file.readline().split()))

merged = []
i = 0 # указатель для array1
j = 0 # указатель для array2
while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
        merged.append(array1[i])
        i += 1
    else:
        merged.append(array2[j])
        j += 1

if i < len(array1): # проверка для оставшегося элемента, если длины массивов были разными
    merged.extend(array1[i:])
else:
    merged.extend(array2[j:])

print(merged)