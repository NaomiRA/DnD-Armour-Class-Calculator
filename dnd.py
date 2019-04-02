"""
DnD Armour Class Calculator

Created by Naomi 18/02/19
"""

def CalcArmourClass(Armour, DexMod, Shield, Misc):
    AC = 10 #Armour Class
    
    if Armour == "padded" or Armour == "leather":
        AC = 11 + DexMod
    elif Armour == "studded leather":
        AC = 12 + DexMod
    elif Armour == "hide":
        if DexMod >= 2:
            AC = 12 + 2
        else:
            AC = 12 + DexMod
    elif Armour == "chain shirt":
        if DexMod >= 2:
            AC = 13 + 2
        else:
            AC = 13 + DexMod
    elif Armour == "scale mail" or Armour == "breastplate":
        if DexMod >= 2:
            AC = 14 + 2
        else:
            AC = 14 + DexMod
    elif Armour == "half plate":
        if DexMod >= 2:
            AC = 15 + 2
        else:
            AC = 15 + DexMod
    elif Armour == "ring mail":
        AC = 14
    elif Armour == "chain mail":
        AC = 16
    elif Armour == "splint":
        AC = 17
    elif Armour == "plate":
        AC = 18
    else:
        AC = 10
    if Shield == True:
        AC = AC + 2
    AC = AC + Misc
    return AC

Shield = False
Armour = input("Enter the type of armour: ")
Armour = Armour.lower()
DexMod = int(input("Enter the Dexterity Modifier: "))
ShieldYN = input("Do you have a shield? Y/N: ")
ShieldYN = ShieldYN.lower()
Misc = int(input("Enter any miscellaneous values. If there are none, enter 0: "))
if ShieldYN == "y":
    Shield = True
else:
    Shield = False

ArmourClass = CalcArmourClass(Armour, DexMod, Shield, Misc)
print("The Armour Class is", ArmourClass)
