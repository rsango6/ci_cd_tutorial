# bioinfo.py

def dna_to_rna(dna_sequence):
    """
    Converts a DNA sequence to an RNA sequence.
    Parameters:
    dna_sequence (str): A string containing the DNA sequence.
    Returns:
    str: The RNA sequence.
    """

    if not all(nucleotide in "ATCG" for nucleotide in dna_sequence):
        raise ValueError("Invalid DNA sequence")

    return dna_sequence.replace('T', 'U')

def rna_to_amino_acid(rna_sequence):
    """
    Converts an RNA sequence to an amino acid sequence.
    Parameters:
    rna_sequence (str): A string containing the RNA sequence.
    Returns:
    str: The amino acid sequence.
    """
    codon_table = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
        "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    if 'AUG' not in rna_sequence:
        raise ValueError("No start codon found")

    start_pos = rna_sequence.find('AUG')
    amino_acid_sequence = ""

    for i in range(start_pos, len(rna_sequence)-2, 3):
        codon = rna_sequence[i:i+3]
        if codon in {'UAA', 'UAG', 'UGA'}:  # Stop codons
            break
        amino_acid_sequence += codon_table.get(codon, "?")

    return amino_acid_sequence
