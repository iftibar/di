import random

class Genes:
    def __init__(self):
        self.value = str(random.randint(0, 1))

    def mutate(self):
        return str(random.randint(0, 1))

class Chromosomes(Genes):
    def __init__(self, Genes):
        self.Genes = []
        for x in range(10):
            gene = str(random.randint(0, 1))
            self.Genes.append(gene)

a = Genes()
b = Chromosomes(a)
print(b.Genes)


#
# class DNA(Chromosomes):
#     def __init__(self, gen_list):
#         chr_list = []
#         for x in range(10):
#             chr_list.append(gen_list)
#
#
# class Organ(DNA):
#     def __init__(self, name):
#         self.name = name
#         self.chromosomes = Chromosomes
#
