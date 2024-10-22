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

def analyse():
    i = []
    img = Image.open("/home/ulyx/Travail/Projet-PEI/"+"Chasseur"+".jpg")

    img_hsv = img.convert('HSV')
    pixels = img_hsv.load()
    width, height = img_hsv.size
    h = height//4
    w = width//2
    h_r = height%4
    w_r = width%4
    print(height, width,h,w,h_r,w_r)
    p = []
    for x in range(height):
        t = []
        for y in range(width):
            t.append(pixels[x, y][0])
        p.append(t)


    """for i in range(h_r):
        t2 = []
        for j in range(w_r):
            for k in range(4)
                v = p.pop()

    """



    print(i)
    return i

# Exemple avec plusieurs carrés colorés
def print_squares():
    for i in range (75):
        for j in range(75):
            print_colored_square(44)
        print()

#print_squares()
analyse()
