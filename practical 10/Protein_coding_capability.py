def capacity(sequence):
    sequence = sequence.upper()
    start_codon = 'ATG'
    stop_codon = 'TGA'
    length = len(sequence)

    start_position = sequence.find(start_codon)
    stop_position = sequence.rfind(stop_codon)

    if start_position == -1 or stop_position == -1:
        return 0.0, 'unclear'

    coding_length = stop_position - start_position + 3
    coding_percent = coding_length / length

    if coding_percent > 0.5:
        coding_capacity = 'protein-coding'
    elif coding_percent < 0.1:
        coding_capacity = 'non-coding'
    else:
        coding_capacity = 'unclear'
    return f"coding percentage: {coding_percent:.2%}", coding_capacity


# An example
a = capacity('atgtgaaaaattatgtttgagtggggggagagagagag')
print(a)
