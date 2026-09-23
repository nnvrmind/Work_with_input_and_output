def read_fasta(path: str) -> dict:
    """
    Функция для чтения fasta-файла
    Parameters
    ----------
    path : str
        путь к файлу
    Returns
    -------
    dna_sequences : dict
        словарь с идентификаторами и последовательностями
    Raises
    ------
    AssertionError
        Входной параметр не является строкой
    """
    assert isinstance(path, str), "Входной параметр не является строкой"

    with open(path) as file:
        lines = [line.strip() for line in file]
        dna_sequences = {}
        for line in lines:
            if line[0] == ">":
                current_id = line[1:]
                dna_sequences[current_id] = ""
            else:
                dna_sequences[current_id] += line
    return dna_sequences

my_dict = read_fasta("rosalind_gc.txt")
gc_contents = {}

for id_seq, seq in my_dict.items():
    perc = (seq.count("G") + seq.count("C")) * 100 / len(seq)
    gc_contents[id_seq] = perc

max_id = max(gc_contents, key=gc_contents.get) # сравнение ключей по значениям, которые им соответствуют

print(max_id)
print(gc_contents[max_id])