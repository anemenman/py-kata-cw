"""
Molecule to atoms

For a given chemical formula represented by a string, count the number of atoms of each element contained in the
molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).

For example:

water = 'H2O'
parse_molecule(water)                 # return {H: 2, O: 1}

magnesium_hydroxide = 'Mg(OH)2'
parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

var fremy_salt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply
count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen
atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
"""


def parse_molecule(formula: str) -> dict:
    def parse_group(i: int):
        counts = {}
        while i < len(formula):
            char = formula[i]

            if char.isupper():
                j = i + 1
                while j < len(formula) and formula[j].islower():
                    j += 1
                elem = formula[i:j]
                i = j

                num_str = ""
                while i < len(formula) and formula[i].isdigit():
                    num_str += formula[i]
                    i += 1
                num = int(num_str) if num_str else 1

                counts[elem] = counts.get(elem, 0) + num

            elif char in "([{":
                inner_counts, i = parse_group(i + 1)

                num_str = ""
                while i < len(formula) and formula[i].isdigit():
                    num_str += formula[i]
                    i += 1
                num = int(num_str) if num_str else 1

                for elem, count in inner_counts.items():
                    counts[elem] = counts.get(elem, 0) + count * num

            elif char in ")]}":
                return counts, i + 1

            else:
                i += 1

        return counts, i

    counts, _ = parse_group(0)
    return counts


assert parse_molecule("H2O") == {'H': 2, 'O': 1}
assert parse_molecule("B2H6") == {'B': 2, 'H': 6}
assert parse_molecule("C6H12O6") == {'C': 6, 'H': 12, 'O': 6}
assert parse_molecule("Mo(CO)6") == {'Mo': 1, 'C': 6, 'O': 6}
assert parse_molecule("Mg(OH)2") == {'Mg': 1, 'O': 2, 'H': 2}
assert parse_molecule("Fe(C5H5)2") == {'Fe': 1, 'C': 10, 'H': 10}
assert parse_molecule("(C5H5)Fe(CO)2CH3") == {'C': 8, 'H': 8, 'Fe': 1, 'O': 2}
assert parse_molecule("Pd[P(C6H5)3]4") == {'Pd': 1, 'P': 4, 'C': 72, 'H': 60}
assert parse_molecule("K4[ON(SO3)2]2") == {'K': 4, 'O': 14, 'N': 2, 'S': 4}
assert parse_molecule("As2{Be4C5[BCo3(CO2)3]2}4Cu5") == {'As': 2, 'Be': 16, 'C': 44, 'B': 8, 'Co': 24, 'O': 48, 'Cu': 5}
assert parse_molecule("{[Co(NH3)4(OH)2]3Co}(SO4)3") == {'Co': 4, 'N': 12, 'H': 42, 'O': 18, 'S': 3}
assert parse_molecule("C2H2(COOH)2") == {'C': 4, 'H': 4, 'O': 4}
