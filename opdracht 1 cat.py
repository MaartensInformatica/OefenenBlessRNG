import re


class DNA:

    def setdna(self, seq):
        x = "[ATGCN]"
        seq = open(seq)
        for line in seq:
            if ">" not in line:
                dna_pattern = re.compile(x)
                matches = dna_pattern.finditer(line)
                    self.__seq = seq

    def getdna(self):
        return self.__seq

def main():
    d1 = DNA()
    d1.setdna("testkat.txt")
    print("dna: ", d1.getdna())

main()
