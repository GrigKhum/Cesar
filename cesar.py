tarer = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def cesar():
    a = input("Enter your message ")
    shift = int(input("Type the shift number "))
    verjnakan_text = ""
    for x in a:
        c = tarer.index(x)
        c += shift
        tar = tarer[c]
        verjnakan_text += tar
    print(verjnakan_text)
            
cesar()