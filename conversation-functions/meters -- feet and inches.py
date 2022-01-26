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


length(abs(meters), abs(feet), abs(inches))
