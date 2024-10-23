from PIL import Image

colors = {
    'Rouge': 41,
    'Jaune': 42,
    'Vert': 43,
    'Cyan': 44,
    'Bleu': 45,
    'Violet': 46,
    'Magenta': 47,
    'Marron': 48,
    'Gris': 49,
    'Noir': 50,
    'Blanc': 51,
}

def couleur(h, s, v):
    if s < 0.1 and v > 0.9:
        return colors["Blanc"]
    elif v < 0.1:
        return colors["Noir"]
    elif s < 0.1 and 0.3<=v<=0.8:
        return colors["Gris"]
    else:
        if 0 <=h <30 or 330 <=h <=360:
            return colors["Rouge"]
        elif 30 <=h < 45:
            return colors["Marron"]
        elif 45 <=h < 70:
            return colors["Jaune"]
        elif 70 <=h < 150:
            return colors["Vert"]
        elif 150 <=h < 180:
            return colors["Cyan"]
        elif 180 <=h < 255:
            return colors["Bleu"]
        elif 255 <=h < 285:
            return colors["Violet"]
        elif 285 <=h < 330:
            return colors["Magenta"]

def analyse():
    pixels = []
    image = Image.open("/home/ulyx/Travail/Projet-PEI/"+"Chasseur"+".jpg")
    img = image.resize((50,37))
    #img.save("/home/ulyx/Travail/Projet-PEI/"+"Chasseur_2"+".jpg")
    #img.show()

    img_hsv = img.convert('HSV')
    width, height = img_hsv.size

    for y in range(height):
        t = []
        for x in range(width):
            h, s, v = img_hsv.getpixel((x,y))
            t.append(couleur(h,s,v))
        pixels.append(t)

    return pixels

def print_card():
    pixels = analyse()
    for y in pixels:
        for x in y:
            print_colored_square(x)
        print()



def print_colored_square(color_code):
    # Code ANSI pour changer la couleur de fond
    print(f"\033[{color_code}m  \033[0m", end="")



# Exemple avec plusieurs carrés colorés
def print_squares():
    for i in range (75):
        for j in range(75):
            print_colored_square(44)
        print()

print_card()
#analyse()
