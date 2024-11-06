from PIL import Image


colors_2 = {
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

colors = {
    'Rouge clair': 196,
    'Rouge foncé': 52,
    'Orange clair': 214,
    'Marron foncé': 94,
    'Jaune clair': 226,
    'Jaune foncé': 100,
    'Vert clair': 46,
    'Vert foncé': 22,
    'Cyan clair': 51,
    'Cyan foncé': 30,
    'Bleu clair': 21,
    'Bleu foncé': 24,
    'Violet clair': 201,
    'Violet foncé': 90,
    'Magenta clair': 201,
    'Magenta foncé': 125,
    'Gris clair': 250,
    'Gris foncé': 235,
    'Noir': 232,
    'Blanc': 255
}

def couleur_2(r,g,b):
    if s < 0.1 and v > 0.9:
        return colors["Blanc"]
    elif v < 0.1:
        return colors["Noir"]
    elif s < 0.1 :
        if 0.5<=v<=0.9:
            return colors["Gris"]
        if 0.2<=v<0.5:
            return colors["Gris"]
    else:
        if 0 <=h <30 or 330 <=h <=360:
            if v < 0.5 :
                return colors["Rouge foncé"]
            return colors["Rouge clair"]
        elif 30 <=h < 45:
            if v < 0.5 :
                return colors["Marron foncé"]
            return colors["Orange clair"]
        elif 45 <=h < 70:
            if v < 0.5 :
                return colors["Jaune foncé"]
            return colors["Jaune clair"]
        elif 70 <=h < 150:
            if v < 0.5 :
                return colors["Vert foncé"]
            return colors["Vert clair"]
        elif 150 <=h < 180:
            if v < 0.5 :
                return colors["Cyan foncé"]
            return colors["Cyan clair"]
        elif 180 <=h < 255:
            if v < 0.5 :
                return colors["Bleu foncé"]
            return colors["Bleu clair"]
        elif 255 <=h < 285:
            if v < 0.5 :
                return colors["Violet foncé"]
            return colors["Violet clair"]
        elif 285 <=h < 330:
            if v < 0.5 :
                return colors["Magenta foncé"]
            return colors["Magenta clair"]


def couleur(r, g, b):
    if r == g == b:
        return colors["Blanc"] if r > 200 else colors["Gris clair"] if r > 100 else colors["Gris foncé"]
    elif r < 50 and g < 50 and b < 50:
        return colors["Noir"]

    if 150 < r <= 255 and 0 <= g < 100 and 0 <= b < 100:
        return colors["Rouge foncé"]
    elif 200 < r <= 255 and 200 < g <= 255 and 0 <= b < 100:
        return colors["Rouge clair"]
    elif 200 < r <= 255 and 100 < g <= 255 and 0 <= b < 50:
        return colors["Orange clair"]
    elif 150 < r <= 255 and 100 < g <= 200 and 0 <= b < 50:
        return colors["Marron foncé"]
    elif 150 < g <= 255 and 0 <= r < 100 and 0 <= b < 100:
        return colors["Vert foncé"]
    elif 200 < g <= 255 and 100 < r <= 255 and 0 <= b < 100:
        return colors["Jaune foncé"]
    elif 200 < g <= 255 and 0 <= r < 100 and 0 <= b < 100:
        return colors["Jaune clair"]
    elif 150 < g <= 255 and 150 < b <= 255 and 0 <= r < 100:
        return colors["Cyan foncé"]
    elif 100 < g <= 255 and 100 < b <= 255 and 0 <= r < 100:
        return colors["Cyan clair"]
    elif 150 < b <= 255 and 0 <= r < 100 and 0 <= g < 100:
        return colors["Bleu foncé"]
    elif 200 < b <= 255 and 0 <= r < 100 and 0 <= g < 100:
        return colors["Bleu clair"]
    elif 100 < b <= 255 and 0 <= r < 100 and 0 <= g < 100:
        return colors["Magenta foncé"]
    elif 0 <= r < 100 and 100 < g <= 255 and 100 < b <= 255:
        return colors["Magenta clair"]
    elif 150 < b <= 255 and 0 <= r < 100 and 0 <= g < 100:
        return colors["Violet foncé"]
    elif 200 < b <= 255 and 0 <= r < 100 and 0 <= g < 100:
        return colors["Violet clair"]

    return colors["Vert foncé"]


def analyse():
    pixels = []
    image = Image.open("/home/ulyx/Travail/Projet-PEI/"+"Chasseur"+".jpg")
    img = image.resize((70, 50))
    img.save("/home/ulyx/Travail/Projet-PEI/"+"Chasseur_2"+".jpg")
    #img.show()

    width, height = img.size

    for y in range(height):
        t = []
        for x in range(width):
            r,g,b = img.getpixel((x,y))
            t.append((r,g,b))
        pixels.append(t)
    return pixels

def print_card():
    pixels = analyse()
    for y in pixels:
        for x in y:
            print_colored_square(x)

            #print_colored_square(x)
        print()



def print_colored_square(rgb):
    r, g, b = rgb[0], rgb[1], rgb[2]
    print(f"\033[48;2;{r};{g};{b}m   \033[0m", end='')




# Exemple avec plusieurs carrés colorés
def print_squares():
    for i in range (75):
        for j in range(75):
            print_colored_square(44)
        print()

print_card()
#analyse()

"""
Rouge clair	(255, 102, 102)	(255, 204, 204)
Rouge foncé	(153, 0, 0)	(204, 0, 0)
Orange clair	(255, 204, 102)	(255, 204, 153)
Marron foncé	(102, 51, 0)	(153, 94, 77)
Jaune clair	(255, 255, 102)	(255, 255, 204)
Jaune foncé	(204, 204, 0)	(255, 255, 102)
Vert clair	(153, 255, 153)	(204, 255, 204)
Vert foncé	(0, 102, 0)	(0, 153, 0)
Cyan clair	(102, 204, 204)	(153, 255, 255)
Cyan foncé	(0, 153, 153)	(0, 204, 204)
Bleu clair	(102, 153, 255)	(153, 204, 255)
Bleu foncé	(0, 0, 102)	(0, 0, 204)
Violet clair	(204, 153, 255)	(255, 204, 255)
Violet foncé	(102, 0, 153)	(153, 0, 204)
Magenta clair	(204, 102, 255)	(255, 153, 255)
Magenta foncé	(153, 0, 102)	(204, 0, 153)
Gris clair	(220, 220, 220)	(255, 255, 255)
Gris foncé	(169, 169, 169)	(192, 192, 192)
Noir	(0, 0, 0)	(50, 50, 50)
Blanc	(255, 255, 255)	(255, 255, 255)
"""
