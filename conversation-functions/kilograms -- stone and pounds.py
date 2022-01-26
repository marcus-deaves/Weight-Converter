def weight(kilograms, stone, pounds):
    if kilograms != 0:
        converted_stone = (kilograms / 6.35029318)
        converted_pounds = int(round(14 * (converted_stone - (converted_stone // 1))))
        print(kilograms, "kilograms equals", int((converted_stone // 1)), "stone and", converted_pounds, "pounds.")

    if kilograms == 0:
        converted_kilograms = round((stone * 6.35029318) + (pounds * 0.45359237), 2)
        print(stone, "stone and", pounds, "pounds equals", converted_kilograms, "kilograms")


weight(abs(meters), abs(feet), abs(inches))
