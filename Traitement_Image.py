from PIL import Image
import os as os

def analyse(chemin_fichier : str, heigth, width):
    pixels = []
    image = Image.open(chemin_fichier)
    img = image.resize((heigth, width))
    #img.save(chemin_fichier)
    #img.show()

    width, height = img.size

    for y in range(height):
        t = []
        for x in range(width):
            r,g,b = img.getpixel((x,y))
            t.append((r,g,b))
        pixels.append(t)
    return pixels

def print_card(chemin_fichier : str, heigth, width):
    pixels = analyse(chemin_fichier, heigth, width)
    for y in pixels:
        for x in y:
            print_colored_square(x)

            #print_colored_square(x)
        print()



def print_colored_square(rgb):
    r, g, b = rgb[0], rgb[1], rgb[2]
    print(f"\033[48;2;{r};{g};{b}m   \033[0m", end='')


#os.system("clear")
#print_card("./illustration/bandeau.jpg", 50, 30)
