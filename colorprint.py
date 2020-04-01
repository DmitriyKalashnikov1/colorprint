colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "violet": "\033[35m",
    "turquoise": "\033[36m",
    "white": "\033[37m",
    "none": ""
    }
backgrounds = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "violet": "\033[45m",
    "turquoise": "\033[46m",
    "white": "\033[47m",
    "none": ""
    } 
effects = {
    "fatty": "\033[1m",
    "faded": "\033[2m",
    "cursive": "\033[3m",
    "underline": "\033[4m",
    "rblink": "\033[5m",
    "fblink": "\033[6m",
    "none": ""
    }

reset = "\033[0m" 

def cprint(effect, color, background, text):
    global effects
    global colors
    global backgrounds
    if ((effect in effects.keys()) and (color in colors.keys()) and (background in backgrounds.keys())):
        retstr = effects[effect] + colors[color] + backgrounds[background] + "{}" + reset
        print(retstr.format(text))
    else:
              retstr = effects["fatty"] + colors["yellow"] + backgrounds["black"] + "Warring!!! Some of argument in this call cprint is wrong!!!" + reset
              print(retstr)
              print(text)

if __name__ == "__main__":
    for effect in effects.keys():
        for color in colors.keys():
            for background in backgrounds.keys():
                cprint(effect, color, background, "effect = {ef}, color = {col}, background = {b}".format(ef = effect, col = color, b = background))
    print("ENABLE EFFECTS ARE: ", end = "")
    for key in effects.keys():
        print(key, end = ", ")
    print("", end = "\n")
    print("ENABLE COLORS ARE: ", end = "")
    for key in colors.keys():
        print(key, end = ", ")
    print("", end = "\n")
    print("ENABLE BACKGROUNDS ARE: ", end = "")
    for key in backgrounds.keys():
        print(key, end = ", ")
    print("", end = "\n")
