

age = 20

# threshold
age_alcohol = 21
age_drive = 18

if age >= age_alcohol:
    print("you can drink beer!")

elif age < age_drive:
    print("You can't even drive")

else:
    print("you are too young to drink beer but you can drive")

if not 0 < age < 120:
    print("The value is invalid")


# Nane

a = None

if a:
    """
    if a is None -> False
    if a is not None -> True
    """
    print("a has value")
else:
    print("a is None")