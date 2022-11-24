element = input("What is your element? ")
element_mapping = {
    "Hydrogen": "H",
    "Helium": "He",
    "Lithium": "Li",
    "Beryllium": "Be",
    "Boron": "B",
    "Nitrogen": "N",
    "Oxygen": "O",
    "Fluorine": "F",
    "Neon": "Ne",
    "Sodium": "Na",
    "Magnesium": "Mg",
    "Aluminum": "Al",
    "Silicon": "Si",
    "Phosphorus": "P",
    "Sulfur": "S",
    "Chlorine": "Cl",
    "Argon": "Ar",
    "Potassium": "K",
    "Calcium": "Ca",
    "Scandium":"Sc",
    "Titanium": "Ti",
    "Vanadium": "V",
    "Chromium": "Cr",
    "Manganese": "Mn",
    "Iron": "Fe",
    "Cobalt": "Co",
    "Nickel": "Ni",
    "Copper": "Cu",
    "Zinc": "Zn",
    "Gallium": "Ga",
    "Germanium": "Ge",
    "Arsenic": "As",
    "Selenium": "Se",
    "Bromine": "Br",
    "Krypton": "Kr",
    "Rubidium": "Rb",
    "Strontium": "Sr",
    "Yttrium": "Y",
    "Zirconium": "Zr",
    "Niobium": "Nb",
    "Molybdenum": "Mo",
    "Technetium": "Tc",
    "Ruthenium": "Ru",
    "Rhodium": "Rh",
    "Palladium": "Pd",
    "Silver": "Ag",
    "Cadmium": "Cd",
    "Indium": "In",
    "Tin": "Sn",
    "Antimony": "Sb",
    "Tellurium": "Te",
    "Iodine": "I",
    "Xenon": "Xe",
    "Cesium": "Cs",
    "Barium": "Ba",
    "Lanthanum": "La",
    "Cerium": "Ce",
    "Praseodymium": "Pr",
    "Neodymium": "Nd",
    "Promethium": "Pm",
    "Samarium": "Sm",
    "Europium": "Eu",
    "Gadolinium": "Gd",
    "Terbium": "Tb",
    "Dysprosium": "Dy",
    "Holmium": "Ho",
    "Erbium": "Tr",
    "Thulium": "Tm",
    "Ytterbium": "Yb",
    "Lutetium": "Lu",
    "Hafnium": "Hf",
    "Tantalum": "Ta",
    "Tungsten": "W",
    "Rhenium": "Re",
    "Osmium": "Os",
    "Iridium": "Ir",
    "Platinum": "Pt",
    "Gold": "Au",
    "Mercury": "Hg",
    "Thallium": "Tl",
    "Lead": "Pb",
    "Bismuth": "Bi",
    "Polonium": "Po",
    "Astatine": "At",
    "Radon": "Rn",
    "Francium": "Fr",
    "Radium": "Ra",
    "Actinium": "Ac",
    "Thorium": "Th",
    "Protactinium": "Pa",
    "Uranium": "U",
    "Neptunium": "Np",
    "Plutonium": "Pu",
    "Americium": "Am",
    "Curium": "Cm",
    "Berkelium": "Bk",
    "Californium": "Cf",
    "Einsteinium": "Es",
    "Fermium": "Fm",
    "Mendelevium": "Md",
    "Nobelium": "No",
    "Lawerencium": "Lr",
    "Rutherforium": "Rf",
    "Dubnium": "Db",
    "Seaborgium": "Sg",
    "Bohrium": "Bh",
    "Hassium": "Hs",
    "Meitnerium": "Mt",
    "Darmstadtium": "Ds",
    "Roentgenium": "Rg",
    "Copernicium": "Cn",
    "Nihonium": "Nh",
    "Flerovium": "Fl",
    "Moscovium": "Mc",
    "Livermorium": "Lv",
    "Tennessine": "Ts",
    "Oganesson": "Og"
}
element_charges = {
    "Hydrogen": "1+",
    "Helium": "noble gas",
    "Lithium": "1+",
    "Beryllium": "2+",
    "Boron": "3-, 3+",
    "Nitrogen": "3-",
    "Oxygen": "2-",
    "Fluorine": "1-"
    "Neon":
    "Sodium":
    "Magnesium":
    "Aluminum":
    "Silicon":
    "Phosphorus":
    "Sulfur":
    "Chlorine":
    "Argon":
    "Potassium":
    "Calcium":
    "Scandium":
    "Titanium":
    "Vanadium":
    "Chromium":
    "Manganese":
    "Iron":
    "Cobalt":
    "Nickel":
    "Copper":
    "Zinc":
    "Gallium":
    "Germanium":
    "Arsenic":
    "Selenium":
    "Bromine":
    "Krypton":
    "Rubidium":
    "Strontium":
    "Yttrium":
    "Zirconium":
    "Niobium":
    "Molybdenum":
    "Technetium":
    "Ruthenium":
    "Rhodium":
    "Palladium":
    "Silver":
    "Cadmium":
    "Indium":
    "Tin":
    "Antimony":
    "Tellurium":
    "Iodine":
    "Xenon":
    "Cesium":
    "Barium":
    "Lanthanum":
    "Cerium":
    "Praseodymium":
    "Neodymium":
    "Promethium":
    "Samarium":
    "Europium":
    "Gadolinium":
    "Terbium":
    "Dysprosium":
    "Holmium":
    "Erbium":
    "Thulium":
    "Ytterbium":
    "Lutetium":
    "Hafnium":
    "Tantalum":
    "Tungsten":
    "Rhenium":
    "Osmium":
    "Iridium":
    "Platinum":
    "Gold":
    "Mercury":
    "Thallium":
    "Lead":
    "Bismuth":
    "Polonium":
    "Astatine":
    "Radon":
    "Francium":
    "Radium":
    "Actinium":
    "Thorium":
    "Protactinium":
    "Uranium":
    "Neptunium":
    "Plutonium":
    "Americium":
    "Curium":
    "Berkelium":
    "Californium":
    "Einsteinium":
    "Fermium":
    "Mendelevium":
    "Nobelium":
    "Lawerencium":
    "Rutherforium":
    "Dubnium":
    "Seaborgium":
    "Bohrium":
    "Hassium":
    "Meitnerium":
    "Darmstadtium":
    "Roentgenium":
    "Copernicium":
    "Nihonium":
    "Flerovium":
    "Moscovium":
    "Livermorium":
    "Tennessine":
    "Oganesson":
}
output = ""
for elements in element_mapping:
    for charges in element_charges:
        output = element_mapping.get(element, "!") + element_charges.get(element, "!")
        print(output)
    break
