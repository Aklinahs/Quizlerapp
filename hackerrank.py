def health_calculator(genes, health, dna):
    gene_health = 0

    for i in range(len(genes)):
        count = 0
        beg = 0
        while dna.find(genes[i], beg) != -1:
            count += 1
            beg = dna.find(genes[i], beg)
            beg += 1
        gene_health += count * health[i]

    return gene_health


genes = ['a', 'b', 'c', 'aa', 'd', 'b']
health = [1, 2, 3, 4, 5, 6]
d = "caaab"
first = 1
last = 5
arr = []

genes = genes[first:last + 1]
health = health[first:last + 1]

arr.append(health_calculator(genes, health, d))

print(f"arr : {arr}")
print(f"{min(arr)} {max(arr)}")
