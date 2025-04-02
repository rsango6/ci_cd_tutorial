# test_bioinfo.py

import pytest
from ..script.bioinfo import dna_to_rna, rna_to_amino_acid


def test_basic():
    assert dna_to_rna("ATGCATGC") == "AUGCAUGC"


def test_empty_string():
    assert dna_to_rna("") == ""


def test_all_thymine():
    assert dna_to_rna("TTTT") == "UUUU"


def test_no_thymine():
    assert dna_to_rna("ACGCGCGC") == "ACGCGCGC"


def test_non_dna_input():
    with pytest.raises(ValueError):
        dna_to_rna("ABCXYZ")


def test_basic_conversion():
    assert rna_to_amino_acid("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA") == "MAMAPRTEINSTRING"

def test_no_start_codon():
    with pytest.raises(ValueError, match="No start codon found"):
        rna_to_amino_acid("UUCGGA")

def test_stop_codon():
    assert rna_to_amino_acid("AUGUAA") == "M"

def test_invalid_codon():
    assert rna_to_amino_acid("AUGXYZ") == "M?"

def test_empty_sequence():
    with pytest.raises(ValueError, match="No start codon found"):
        rna_to_amino_acid("")
