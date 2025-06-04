class DNABase:
    def __init__(self, nucleotide):
        self.base = nucleotide

    def get_nucleotide(self):
        return self.nucleotide
    
    def set_nucleotide(self, value):
        
        mapping = {
            'a': 'adenine',
            'c': 'cytosine',
            'g': 'guanine',
            't': 'thymine'
        }
        value = value.lower()
        if value in mapping.keys():
            self.nucleotide = mapping[value]
        elif value in mapping.values():
            self.nucleotide = value
        else:
            raise ValueError("Nucleotide must be either a valid nucleotide or its first letter.")

    def __repr__(self):
        return f"DNABase({self.nucleotide})"

    base = property(fget = get_nucleotide, fset=set_nucleotide)


d1 = DNABase('A')
print(d1.__dict__)
print(d1.base)
print(repr(d1))
print(d1.nucleotide)

