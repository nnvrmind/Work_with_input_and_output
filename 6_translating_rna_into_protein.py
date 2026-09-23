def read_rna_codon_table(path: str) -> dict:
    """Функция для чтения таблицы кодонов
    Parameters
    ----------
    path : str
        путь к файлу
    Returns
    -------
    codon_table : dict
        таблица кодонов
    Raises
    ------
    AssertionError
        входной параметр не является строкой
    """
    assert isinstance(path, str), "Входной параметр не является строкой"

    codon_table = {}
    with open(path) as file:
        for line in file:
            data = line.split()
            for i in range(0, len(data), 2):
                codon_table[data[i]] = data[i + 1]
    return codon_table

with open("rosalind_prot.txt") as file:
    rna = file.readline().strip()

codon_table = read_rna_codon_table("rosalind_rna_codon_table.txt")

protein = ""

for i in range(0, len(rna), 3):
    if codon_table[rna[i:i+3]] == "Stop":
        break
    protein += codon_table[rna[i:i+3]]

print(protein)