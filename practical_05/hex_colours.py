"""
Dictionary of Colour Keys and Hex Values
"""

COLOUR_TO_HEX = {"lapis lazuli": "#26619c", "light orange": "#fed8b1",
                 "terra cotta": "#e2725b", "sky blue 1": "#87ceff",
                 "saffron": "#f4c430", "rust": "#b7410e",
                 "saddle brown": "#8b4513", "peach puff 1": "#ffdab9",
                 "pale goldenrod": "#eee8aa", "army green": "#4b5320"}

for colour, hex_code in COLOUR_TO_HEX.items():
    print(f"Colour: {colour:<13}, {hex_code}")

colour_name = input("Enter a colour: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name].lower())
    except KeyError:
        print("Invalid short state. Incorrect key used.")
    colour_name = input("Enter a colour: ").lower()
