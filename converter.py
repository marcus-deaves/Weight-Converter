def length(meters, feet, inches):
    if meters != 0:
        converted_feet = int(round(meters * 3, 0))
        converted_inches = int(round(meters * 3.3701, 0))
        if converted_inches > 12:
            while converted_inches > 12:
                converted_inches -= 12
                converted_feet += 1
        print(meters, "meters equals", converted_feet, "feet and", converted_inches, "inches.")

    if meters == 0:
        converted_meters = round((feet * 0.3048) + (inches * 0.0254), 2)
        print(feet, "feet and", inches, "inches equals", converted_meters, "meters")


def weight(kilograms, stone, pounds):
    if kilograms != 0:
        converted_stone = (kilograms / 6.35029318)
        converted_pounds = int(round(14 * (converted_stone - (converted_stone // 1))))
        print(kilograms, "kilograms equals", int((converted_stone // 1)), "stone and", converted_pounds, "pounds.")

    if kilograms == 0:
        converted_kilograms = round((stone * 6.35029318) + (pounds * 0.45359237), 2)
        print(stone, "stone and", pounds, "pounds equals", converted_kilograms, "kilograms")


def choice():
    ans = input("Would you like to convert length or weight.")

    if ans == "length":
        meters = float(input("Enter how many meters you have. enter 0 to skip."))
        feet = float(input("Enter how many feet you have."))
        inches = float(input("Enter how many inches you have."))
        length(abs(meters), abs(feet), abs(inches))

    if ans == "weight":
        kilograms = float(input("Enter how many kilograms you have. enter 0 to skip."))
        stone = float(input("Enter how many stone you have."))
        pounds = float(input("Enter how many pounds you have."))
        weight(abs(kilograms), abs(stone), abs(pounds))


choice()
