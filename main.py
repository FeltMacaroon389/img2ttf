import fontforge
import sys

IMAGE = "colon_three.svg"
FONT_NAME = "ColonThree"

def main():

    # Create a new font
    font = fontforge.font()
    font.fontname = FONT_NAME
    font.familyname = FONT_NAME
    font.fullname = FONT_NAME

    # Define the glyphs to include
    glyphs = [chr(i) for i in range(32, 127)]  # ASCII characters

    # Create a glyph for the image
    colon_three = font.createChar(ord(":"), ":")
    colon_three.importOutlines(IMAGE)
    colon_three.width = 600

    # Assign glyph to all other characters
    for char in glyphs:
        if char != ':':
            glyph = font.createChar(ord(char))
            glyph.addReference(':', (1, 0, 0, 1, 0, 0))
            glyph.width = 600

    # Generate the font
    font.generate(f"{FONT_NAME}.ttf")

    print(f"{FONT_NAME}.ttf successfully generated from {IMAGE}")

if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        print(f"An error occurred: {error}")
        sys.exit(1)

