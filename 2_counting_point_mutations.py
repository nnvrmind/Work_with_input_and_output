with open("rosalind_hamm.txt") as file:
    lines = [line.strip() for line in file] # получаем список из двух строк, которые нужно сравнить

cnt = 0

for i in range(len(lines[0])):
    if lines[0][i] != lines[1][i]:
        cnt += 1

print(cnt)