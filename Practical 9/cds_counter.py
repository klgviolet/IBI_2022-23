import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
A = re.findall('TGA|TAA', seq)  # find all the coding	sequences
print(len(A))  # count the number
