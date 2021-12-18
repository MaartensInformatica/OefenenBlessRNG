import re

def peptide_output(path):
    file = open(path)
    peptide_lines = []
    count = 0
    for line in file:
        count += 1
        if ">" not in line:
            peptide_lines.append(line)
        if count == 20:
            break
    return peptide_lines

def proteins(peptides):
    list_of_prots = []
    x = "[ACDEFGHIKLMNPQRSTVWY]*"
    count = 0
    for line in peptides:
        count += 1
        prot = re.search(x, line)
        list_of_prots.append(prot)
        if count == 5:
            break
    return list_of_prots

def main():
    filename = "Mus_musculus.fa"
    peptides = peptide_output(filename)
    print(peptides)
    proteins(peptides)
main()
