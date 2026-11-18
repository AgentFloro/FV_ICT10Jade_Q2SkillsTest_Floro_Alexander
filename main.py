from pyscript import document, display
NonMetalicElements = {
        "H": ("Hydrogen", 1, 1008),
        "C": ("Carbon", 6, 1201),
        "N": ("Nitrogen", 7, 1401),
        "O": ("Oxygen", 8, 1600),
        "F": ("Fluorine", 9, 1900),
        "P": ("Phosphorus", 15, 3097),
        "S": ("Sulfur", 16, 3207),
        "Cl": ("Chlorine", 17, 3545),
        "Se": ("Selenium", 34, 7896),
        "Br": ("Bromine", 35, 7990),
        "I": ("Iodine", 53, 12690),
        "He": ("Helium", 2, 4002),
        "Ne": ("Neon", 10, 2018),
        "Ar": ("Argon", 18, 3995),
        "Kr": ("Krypton", 36, 8380),
        "Xe": ("Xenon", 54, 13129),
        "Rn": ("Radon", 86, 22000)
    }


def detailcheck(e):
    document.getElementById("output1").innerHTML = ""   

    Varsity2 = document.getElementById("input1").value
    var2 = dict.get(NonMetalicElements.get(Varsity2), ("Element not found" , " - " , " - "))


    document.getElementById("output1").innerHTML = f"""
     Symbol: {NonMetalicElements}
     Element: {var2[0]}
     Atomic Number: {var2[1]}
     Atomic Mass: {var2[2]}
 """

    
