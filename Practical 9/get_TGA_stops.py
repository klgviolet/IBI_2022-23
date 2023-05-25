input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open('TGA_genes.fa', 'w')
content = input_file.read()
content_lines = content.split("\n")
new_content = ""
for line in content_lines:
    if line.startswith(">"):
        new_content += "\n" + line.split(" ")[0] + "\n"
    else:
        new_content += line
new_content_lines = new_content.split("\n")
for i in range(len(new_content_lines)):
    if new_content_lines[i].endswith("TGA"):
        output_file.write(new_content_lines[i-1] + "\n" + new_content_lines[i] + "\n")
input_file.close()
output_file.close()
