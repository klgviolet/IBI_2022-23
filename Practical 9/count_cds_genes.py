import re
input_seq = input('input(TAA/TGA/TAG):')
if input_seq in ['TAA', 'TAG', 'TGA']:
    input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
    output_file = open(f'{input_seq}_stop_genes.fa', "w")
    now_sequence = ''
    now_gene = ''
    for line in input_file:
        line = line.strip()
        if line.startswith(">"):
            if now_sequence.endswith(input_seq):
                output_file.write(f">{now_gene}  number:"+str(len(re.findall(input_seq,now_sequence)))+f"\n{now_sequence}\n")
            now_gene = line[1:].split()[0]
            now_sequence = ''
        else:
            now_sequence += line

    if now_sequence.endswith(input_seq):
        output_file.write(f">{now_gene}  number:"+str(len(re.findall(input_seq,now_sequence)))+f"\n{now_sequence}\n")
    input_file.close()
    output_file.close()
